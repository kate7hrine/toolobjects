from App.Objects.Object import Object
from App.Console.PrintLog import PrintLog
from App.Logger.HideCategory import HideCategory
from .Log import Log
from .LogKind import LogKind, LogKindEnum
from .LogSection import LogSection
from .LogPrefix import LogPrefix
import traceback

from pydantic import Field

class Logger(Object):
    '''
    Class that prints messages (Log's) into hooked functions
    '''

    log_to_console: bool = Field(default = True)
    hidden_categories: list[HideCategory] = Field(default = [])

    @classmethod
    def getClassEventsTypes(cls) -> list:
        return ['log']

    @classmethod
    def mount(cls):
        from App import app

        logger = cls(
            #skip_file = app.Config.get("logger.output.to_file"),
            hidden_categories = app.Config.get("logger.hide_sections"),
        )

        app.mount('Logger', logger)

    def constructor(self):
        if self.log_to_console == True:
            async def print_log(to_print, check_categories):
                should_print = True
                for category in check_categories:
                    if category.isLogMeets(to_print, 'console') == True:
                        should_print = False

                if should_print == True:
                    items = PrintLog()
                    await items.implementation({'log': to_print})

            self.addHook('log', print_log)

    def log(self, 
            message: str | Exception, 
            section: str | list = ['Nonce'],
            kind: str = LogKindEnum.message.value,
            prefix: dict[str, int] = None, 
            exception_prefix: str = '',
            trigger: bool = True):

        write_message = message
        if isinstance(message, Exception):
            exc = traceback.format_exc()
            write_message = exception_prefix + type(message).__name__ + " " + exc

        msg = Log(
            message = write_message,
        )
        msg.section = LogSection(value = section)
        msg.kind =  LogKind(value = kind)
        if prefix != None:
            msg.prefix = LogPrefix(**prefix)

        if trigger == True:
            self.triggerHooks('log', to_print = msg, check_categories = self.hidden_categories)

        return msg

    @classmethod
    def getSettings(cls):
        from App.Arguments.Objects.List import List
        from App.Arguments.Objects.Orig import Orig

        return [
            List(
                name = 'logger.hide_sections',
                default = [],
                orig = Orig(
                    name = 'logger.hide_section',
                    orig = HideCategory
                )
            )
        ]
