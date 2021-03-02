from pymakelib import Module

@Module.ModuleClass
class mod(Module.AbstractModule):

    def getSrcs(self):
        return self.findSrcs(Module.SrcType.C)
    
    def getIncs(self):
        return self.findIncs(Module.IncType.C)
