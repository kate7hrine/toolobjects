from App.Objects.Extractor import Extractor
import asyncio

class ExtractorTest(Extractor):
    async def implementation(self, i):
        for its in range(0, 10):
            self.append(self.log(str(its)))

            await asyncio.sleep(12)
