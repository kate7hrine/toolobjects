from App.Client.Displayment import Displayment
from Media.Media import Media
from App import app

class Get(Displayment):
    for_object = 'Media.Get'

    async def render_as_page(self, args = {}):
        media_types = list()

        for item in app.ObjectsList.getObjectsByCategory(['Media']):
            _module = item.getModule()
            if _module.isInMRO(Media) and _module._getNameJoined() != 'Media.Media':
                media_types.append(_module)

        #for item in items.getItems():
            #item.local_obj.make_public()

        self.context.update({
            'media_types': media_types
        })

        return self.render_template('Other/Media/get.html')
