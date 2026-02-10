from App.Client.Displayment import Displayment
from Data.Types.String import String

class Text(Displayment):
    for_object = 'Media.Text.Text'

    async def render_as_page(self, request, context):
        query = request.rel_url.query
        self.context.update({
            'items': self.get_objs(query.get('uuids').split(',')),
            'String': String,
        })

        return self.render_template('Other/Media/text_page.html')
