from Web.Pages.Crawler.Original import Original

# it is supposed to be a crawler that moves all styles to inline
class Plain(Original):
    async def _after_crawl(self, page, i):
        pass
