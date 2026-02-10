from App.Objects.Test import Test
from Data.Checkmarks.AddCheckmark import AddCheckmark

class CheckmarkTest(Test):
    async def implementation(self, i):
        _i = AddCheckmark()
        await _i.execute({
            'list': 'content_7410337505641365504',
            'label': '{\"value\":\"66\"}'
        })
