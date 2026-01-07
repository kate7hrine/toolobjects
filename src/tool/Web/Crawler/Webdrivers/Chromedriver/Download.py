from App.Objects.Act import Act
from App.Objects.Arguments.ArgumentDict import ArgumentDict
from App.Objects.Arguments.Argument import Argument
from App.Objects.Arguments.LiteralArgument import LiteralArgument
from Web.Crawler.Webdrivers.Chromedriver.Chromedriver import Chromedriver
from App.Objects.Responses.ObjectsList import ObjectsList
from Data.String import String
from App import app
from pathlib import Path
import aiohttp
import platform
import zipfile

class Download(Act):
    @classmethod
    def _arguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            LiteralArgument(
                name = 'channel',
                values = ['Stable', 'Beta', 'Canary', 'Dev'],
                orig = String,
                strict = True,
                default = 'Stable'
            )
        ])

    async def implementation(self, i):
        _bin = app.Storage.get('bin')

        channels = await self._get_versions()
        channel = channels.get(i.get('channel'))

        item = Chromedriver()
        item.platform = self._get_platform()
        item.version = i.get('version')
        item.revision = i.get('revision')

        downloads = channel.get('downloads')
        # chrome = downloads.get('chrome')

        driver_item = None
        shell_item = None

        for _item in downloads.get('chromedriver'):
            if _item.get('platform') == item.platform:
                driver_item = _item

        for _item in downloads.get('chrome-headless-shell'):
            if _item.get('platform') == item.platform:
                shell_item = _item

        assert driver_item != None
        assert shell_item != None

        _unit = _bin.storage_adapter.get_storage_unit()

        _root: Path = _unit.get_root()
        _driver_path = _root.joinpath('driver')
        _shell = _root.joinpath('chrome')

        zip_driver_name = ''
        shell_name = ''

        self.log('downloading driver to driver.zip')

        _item = app.DownloadManager.addURL(driver_item.get('url'), str(_root), 'driver.zip')
        await _item.start()

        with zipfile.ZipFile(str(_root.joinpath('driver.zip')), 'r') as zip_ref:
            _names = zip_ref.namelist()
            zip_driver_name = _names[0].split('/')[0]
            zip_ref.extractall(_root)

        _root.joinpath(zip_driver_name).rename(_driver_path)

        self.log_success('chromedriver is downloaded')
        _root.joinpath('driver.zip').unlink()

        self.log('downloading shell to shell.zip')
        _item = app.DownloadManager.addURL(shell_item.get('url'), str(_root), 'shell.zip')
        await _item.start()

        with zipfile.ZipFile(str(_root.joinpath('shell.zip')), 'r') as zip_ref:
            _names = zip_ref.namelist()
            shell_name = _names[0].split('/')[0]
            zip_ref.extractall(_shell)

        _root.joinpath(shell_name).rename(_shell)
        self.log('shell is downloaded')
        _root.joinpath('shell.zip').unlink()

        _unit.save()

        item.file = item.link(_unit).toInsert()
        item.flush(_bin)

        return ObjectsList(items = [item], unsaveable = True)

    async def _get_versions(self):
        version = "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json"

        async with aiohttp.ClientSession() as session:
            async with session.get(version) as response:
                channels = await response.json()

        channel = channels.get('channels')

        return channel

    def _get_platform(self):
        version = ['', '']
        system_type = platform.system().lower()
        architecture = platform.machine().lower() 

        if architecture in ['x86_64', 'amd64']:
            version[1] = '64'
        elif architecture in ['i386', 'i686', 'x86']:
            version[1] = '32'
        elif architecture in ['arm64', 'aarch64']:
            version[1] = 'arm64'
        else:
            version[1] = architecture

        match system_type:
            case "darwin":
                if architecture in ['arm64', 'aarch64']:
                    version[1] = "arm64"
                else:
                    version[1] = "x64"

                version[0] = 'mac-'
            case "windows":
                version[0] = 'win'
            case _:
                version[0] = 'win'

        return ''.join(version)
