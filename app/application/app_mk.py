from pymakelib import module

@module.ModuleClass
class App(module.AbstractModule):

    def getSrcs(self):
        return self.getAllSrcsC()

    def getIncs(self):
        return self.getAllIncsC()

    # def getCompilerOpts(self):
    #     opts = GCC_CompilerOpts(m.getGeneralCompilerOpts())
    #     return opts