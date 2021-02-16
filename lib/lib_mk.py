from pymakelib.Module import AbstractModule, ModuleClass, ModuleHandle

@ModuleClass
class Lib(AbstractModule):

    def getSrcs(self, m: ModuleHandle):
        return m.getAllSrcsC()

    def getIncs(self, m: ModuleHandle):
        return m.getAllIncsC()
    
    def getCompilerOpts(self, m:ModuleHandle):
        opts = m.getGeneralCompilerOpts()
        opts.setOption('CONTROL-C-OPTS', ['-std=c99'])
        return opts