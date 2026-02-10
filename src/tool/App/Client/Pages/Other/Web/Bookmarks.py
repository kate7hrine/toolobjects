from App.Client.Displayment import Displayment

class Bookmarks(Displayment):
    for_object = 'Web.Bookmarks.Bookmarks'

    async def render_as_collection(self, orig_items, args, orig_collection = None):
        self.context.update({
            'items': orig_items,
        })
        return self.render_string('Other/Web/bookmarks.html')
