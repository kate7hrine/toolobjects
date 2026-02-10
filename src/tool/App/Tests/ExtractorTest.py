from App.Objects.Extractor import Extractor

class ExtractorTest(Extractor):
    async def implementation(self, i):
        for its in range(0, 10):
            self.append(self.log(str(its)))
