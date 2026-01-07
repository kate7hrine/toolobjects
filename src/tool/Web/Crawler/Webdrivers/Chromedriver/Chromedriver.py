from Web.Crawler.Webdrivers.Webdriver import Webdriver
from pydantic import Field

class Chromedriver(Webdriver):
    version: str = Field(default = None)
    revision: str | int = Field(default = None)
