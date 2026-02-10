from App.Objects.Object import Object
from pydantic import Field
from App.Logger.Log import Log

class HideCategory(Object):
    '''
    Object of logger.hide_sections param that allows to hide some messages from logging

    section: section that not will be showed
    wildcard: will check first items of section, if section of log contains them so its true

    section=["App", "Index"] wildcard=False input_section=["App", "Index", "LoadedObject"] === no
    section=["App", "Index"] wildcard=True input_section=["App", "Index", "LoadedObject"] === yes

    unused: do not count this hidecategory

    where: may be console, web, file or smth
    '''

    section: list = Field(default = [])
    kind: list = Field(default = None)
    where: list[str] = Field(default = None)
    wildcard: bool = Field(default = False)
    unused: bool = Field(default = False)

    def isLogMeets(self, log: Log, context: str = None) -> bool:
        '''
        Does log needs to be hidden (true or false)
        '''
        section_meets = False
        context_meets = True

        if self.unused == True:
            return False

        if self.wildcard == False:
            section_meets = ".".join(log.section.value) == ".".join(self.section)
        else:
            section_meets = ".".join(log.section).startswith(".".join(self.section))

        if self.where != None and context not in self.where:
            context_meets = False

        if section_meets and context_meets:
            if self.kind != None:
                return log.kind.value.value in self.kind

            return True
