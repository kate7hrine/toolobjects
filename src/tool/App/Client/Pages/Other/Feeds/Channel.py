from App.Client.Displayment import Displayment

class Channel(Displayment):
    for_object = 'Web.Feeds.Elements.Channel'

    async def render_as_collection(self, orig_items, args, orig_collection = None):
        self.context.update({
            'items': orig_items,
            'args': args,
        })
        return self.render_string('Other/Feeds/feed.html')
