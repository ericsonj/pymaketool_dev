from pymakelib import Module

@Module.ModuleClass
class App(Module.AbstractModule):

    def getSrcs(self):
        return self.getAllSrcsC()

    def getIncs(self):
        return self.getAllIncsC()

    # def getCompilerOpts(self):
    #     opts = GCC_CompilerOpts(m.getGeneralCompilerOpts())
    #     return opts