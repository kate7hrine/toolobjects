from App.Client.Displayment import Displayment

class SearchOnlyIds(Displayment):
    for_object = 'App.DB.Search.SearchOnlyIds'

    async def render_as_collection(self, orig_items, args, orig_collection = None):
        self.context.update({
            'items': orig_items,
            'args': args
        })
        return self.render_string('Explorer/only_ids.html')
