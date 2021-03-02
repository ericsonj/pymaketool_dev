from pymakelib import Module
from pymakelib import log

@Module.ModuleClass
class mod(Module.AbstractModule):

    def getSrcs(self, mh: Module.ModuleHandle) -> list:
        log.info("HOLA")
        return self.findSrcs(Module.SrcType.C)
    
    def getIncs(self, mh: Module.ModuleHandle) -> list:
        return self.findIncs(Module.IncType.C)