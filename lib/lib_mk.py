from pymakelib import module
from pymakelib import project
from pymakelib import Logger

log = Logger.getLogger()

@module.ModuleClass
class Lib(module.AbstractModule):
    
    def getSrcs(self):
        return self.getAllSrcsC()

    def getIncs(self):
        return self.getAllIncsC()
    
    def getCompilerOpts(self):
        opts = project.getCompilerOpts()
        opts['CONTROL-C-OPTS'] = ['-std=c99']
        return opts
