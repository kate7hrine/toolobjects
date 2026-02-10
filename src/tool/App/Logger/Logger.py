from App.Objects.Object import Object
from App.Console.Console import Console
from .Log import Log
from .LogKind import LogKind, LogKindEnum
from .LogSection import LogSection
from .LogPrefix import LogPrefix
import traceback

class Logger(Object):
    class _Hooks(Object._Hooks):
        @property
        def events(self) -> list:
            return ['log']

        def __init__(self):
            super().__init__()

            def _mount():
                from App import app
                traceback.print_list(traceback.extract_stack())

                #app.Config.updateCompare()
                logger = Logger(
                    #skip_file = app.Config.get("logger.output.to_file"),
                    #limiter = LogLimiter(skip_categories = app.Config.get("logger.output.filters")),
                )

                app.mount('Logger', logger)

            self.add('loaded', _mount)

    def constructor(self):
        if True:
            self.hooks.add('log', Console.printLog)

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
            self.hooks.trigger('log', to_print = msg)

        return msg
