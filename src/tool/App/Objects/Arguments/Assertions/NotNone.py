from .Assertion import Assertion
from ..Argument import Argument

class NotNone(Assertion):
    def check(self, argument: Argument):
        if argument.default == None:
            assert argument.inputs != None, argument.not_passed_message.format(argument.name)

        assert argument.current != None, argument.none_message.format(argument.name, argument.inputs)
