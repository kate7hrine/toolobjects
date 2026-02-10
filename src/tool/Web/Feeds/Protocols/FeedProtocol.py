from App.Objects.Protocol import Protocol
import xml.etree.ElementTree as ET
from abc import abstractmethod

class FeedProtocol(Protocol):
    @abstractmethod
    async def parse(self, data: ET):
        ...
