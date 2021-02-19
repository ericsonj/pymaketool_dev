from pymakelib.Module import ModuleHandle, ModuleClass, AbstractModule
from pymakelib.Module import GCC_CompilerOpts

@ModuleClass
class App(AbstractModule):

    def getSrcs(self, m: ModuleHandle):
        srcs = m.getAllSrcsC();
        return srcs

    def getIncs(self, m: ModuleHandle):
        return m.getAllIncsC()

    def getCompilerOpts(self, m:ModuleHandle):
        opts = GCC_CompilerOpts(m.getGeneralCompilerOpts())
        return opts