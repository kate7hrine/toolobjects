from App.Objects.Extractor import Extractor
from App.Objects.Arguments.Argument import Argument
from App.Objects.Arguments.Assertions.NotNone import NotNone
from Data.Types.Int import Int
from Data.Types.Float import Float
from App.Objects.Arguments.ArgumentDict import ArgumentDict
import random

class GetInt(Extractor):
    @classmethod
    def _arguments(cls):
        return ArgumentDict(items=[
            Argument(
                name = "min",
                default = 0,
                orig = Float,
                assertions = [
                    NotNone()
                ]
            ),
            Argument(
                name = "max",
                default = 100,
                orig = Float,
                assertions = [
                    NotNone()
                ]
            )
        ])

    async def _implementation(self, i) -> None:
        objects = Int()
        objects.value = self.randomInt(int(i.get('min')), int(i.get('max')))

        self.append(objects)

    def randomInt(self, min: int, max: int):
        return random.randint(min, max)

    def randomFloat(self, min: float, max: float):
        return random.uniform(min, max)
