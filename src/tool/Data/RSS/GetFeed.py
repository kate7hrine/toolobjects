from App.Objects.Extractor import Extractor
from App.Arguments.ArgumentDict import ArgumentDict
from App.Arguments.Types.String import String
from App.Arguments.Assertions.NotNoneAssertion import NotNoneAssertion
from App.Responses.ObjectsList import ObjectsList
from Data.RSS.Channel import Channel
from Data.RSS.ChannelItem import ChannelItem
from pydantic import Field

class GetFeed(Extractor):
    # Should it be in Web category or in Data? dont know
    channel: Channel = Field(default = None)

    @classmethod
    def getArguments(cls) -> ArgumentDict:
        return ArgumentDict(items = [
            String(
                name = 'url',
                assertions = [NotNoneAssertion()]
            )
        ])

    async def implementation(self, i):
        import aiohttp, xmltodict

        url = i.get('url')
        response_xml = None

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response_xml = await response.text()

        self.log(f"url: {url}")
        rss_response = xmltodict.parse(response_xml)
        rss = rss_response.get('rss')
        _channel = rss.get('channel')
        self.channel = Channel(
            title = _channel.get('title'),
            description = _channel.get('description'),
            channel_link = _channel.get('link'),
            generator = _channel.get('generator'),
            copyright = _channel.get('copyright'),
            language = _channel.get('language'),
        )
        self.link(self.channel)

        for item in _channel.get('item'):
            _item = ChannelItem.model_validate(item, by_alias = True)
            self.channel.link(_item)
            self.append(_item)

    async def sift(self, response: ObjectsList) -> ObjectsList:
        _new = ObjectsList()
        for item in response.getItems():
            print(item)
            _new.append(item)

        return _new
