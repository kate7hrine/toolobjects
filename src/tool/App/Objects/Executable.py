from .Object import Object
from .Validable import Validable
from App.Arguments.ArgumentValues import ArgumentValues
from App.Responses.Response import Response
from App.Objects.Variableable import Variableable
from typing import ClassVar, Optional
from pydantic import Field
from App import app
import asyncio

class Executable(Object, Variableable, Validable):
    '''
    Object that has "execute()" interface, single entrypoint.
    
    getArguments(): validation
    '''

    id: int = 0
    self_name: ClassVar[str] = 'Executable'

    @classmethod
    def getClassEventTypes(cls) -> list:
        return ['before_execute', 'after_execute']

    async def implementation(self, i: dict) -> Response:
        '''
        Entry point, must be overriden in your class
        '''
        pass

    async def implementation_wrap(self, i: dict) -> Response:
        '''
        another checks before implementation(). Can be overriden
        '''

        if asyncio.iscoroutinefunction(self.implementation):
            return await self.implementation(i)
        else:
            return self.implementation(i)

    async def execute(self, 
                      i: ArgumentValues | dict, 
                      check_arguments: bool = True, 
                      raise_on_assertions: bool = True) -> Response:
        '''
        Internal method. Calls module-defined implementation() and returns what it returns
        '''

        self.id = app.app.executables_id.getIndex()
        if type(i) == dict:
            i = ArgumentValues(values = i)
        else:
            i.modified = True

        args = self.getAllArguments()
        vals = i.toDict()
        passing = args.compareWith(
            inputs = vals,
            check_arguments = check_arguments,
            raise_on_assertions = raise_on_assertions,
        )

        if i.modified == False:
            self.args = vals

        await self.awaitTriggerHooks('before_execute', i = passing)

        response = await self.implementation_wrap(i = passing)

        # assert response != None, 'implementation() returned nothing'

        await self.awaitTriggerHooks('after_execute', i = passing)

        return response
