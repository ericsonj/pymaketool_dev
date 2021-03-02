from pymakelib import Module
from pymakelib import Project

@Module.ModuleClass
class Lib(Module.AbstractModule):
    
    def getSrcs(self):
        return self.getAllSrcsC()

    def getIncs(self):
        return self.getAllIncsC()
    
    def getCompilerOpts(self):
        opts = Project.getCompilerOpts()
        opts['CONTROL-C-OPTS'] = ['-std=c99']
        return opts
