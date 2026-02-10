from Data.Random.GetInt import GetInt
from Data.Types.Float import Float

class GetFloat(GetInt):
    async def _implementation(self, i) -> None:
        objects = Float()
        objects.value = self.randomFloat(i.get('min'), i.get('max'))

        self.append(objects)
