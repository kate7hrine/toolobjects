from App.Client.Displayment import Displayment
from Data.Types.String import String

class Audio(Displayment):
    for_object = 'Media.Audios.Audio'

    async def render_as_page(self, request, context):
        query = request.rel_url.query
        self.context.update({
            'items': self.get_objs(query.get('uuids').split(',')),
        })

        return self.render_template('Other/Media/audio_page.html')
