from Web.Feeds.Protocols.FeedProtocol import FeedProtocol
from Web.Feeds.Elements.Channel import Channel
from Web.Feeds.Elements.Link import Link
from Web.Feeds.Elements.Entry import Entry
from Web.Feeds.Elements.EntryContent import EntryContent
from Web.Feeds.Elements.Author import Author
from Web.Feeds.Elements.Category import Category
from typing import ClassVar, Generator, AsyncGenerator
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone

class Atom(FeedProtocol):
    protocol_name = 'atom'

    async def _get_channels(self, data):
        channels = list()
        for item in data.find_all('feed', recursive=False):
            channel = Channel()

            if item.find('title') != None:
                channel.obj.name = item.find('title').text

            for link in item.find_all('link'):
                channel.link_items.append(self._get_link(link))

            if item.find('updated') != None:
                channel.obj.created_at = self._date_to_str(item.find('updated').text)

            if item.find('id') != None:
                channel.id = item.find('id').text

            channels.append(channel)

        return channels

    async def _get_entries(self, channel: Channel, data, i) -> AsyncGenerator[Entry]:
        for entry in data.find_all('entry'):
            yield await self._get_entry(entry)

    def _get_link(self, data):
        _self = Link()
        for key in ['href', 'rel', 'type', 'hreflang', 'title', 'length']:
            set_key = key
            if key == 'href':
                set_key = 'value'

            setattr(_self, set_key, data.get(key))

        return _self

    def _get_author(self, data):
        _self = Author()
        if data.find('name') != None:
            _self.name = data.find('name').text
        if data.find('email') != None:
            _self.email = data.find('email').text
        if data.find('uri') != None:
            _self.uri = data.find('uri').text

        return _self

    def _get_category(self, data):
        _self = Category()
        if data.get('term'):
            _self.term = data.get('term')
        if data.get('label'):
            _self.label = data.get('label')

        return _self

    def _date_to_str(self, val: str):
        for fmt in [
            "%Y-%m-%dT%H:%M:%SZ",
            "%Y-%m-%dT%H:%M:%S%z",
            "%Y-%m-%dT%H:%M:%S",
        ]:
            try:
                _val = datetime.strptime(val, fmt).astimezone(timezone.utc)
                return _val
            except ValueError:
                continue

    async def _get_entry(self, data):
        _title = data.find('title')
        _summary = data.find('summary')
        _content = data.find('content')

        entry = Entry()

        if _title != None:
            entry.obj.name = _title.text
        if _summary != None:
            entry.summary = _summary.text
        if _content != None:
            entry.content = EntryContent(
                type = _content.get('type'),
                content = _content.text,
            )
            await entry.content.update()

        for link in data.find_all('link'):
            entry.link_items.append(self._get_link(link))

        for author in data.find_all('author'):
            entry.author.append(self._get_author(author))

        for item in data.find_all('category'):
            entry.category.append(self._get_category(item))

        _published = data.find('published')
        _edited = data.find('updated')
        if _published != None:
            entry.obj.created_at = self._date_to_str(_published.text)
            if _edited != None:
                entry.obj.updated_at = self._date_to_str(_edited.text)
        else:
            if _edited != None:
                entry.obj.created_at = self._date_to_str(_edited.text)

        return entry
