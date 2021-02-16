from pymakelib.Module import ModuleHandle
from pymakelib.Module import GCC_CompilerOpts


def getSrcs(m: ModuleHandle):
    return m.getAllSrcsC()


def getIncs(m: ModuleHandle):
    return m.getAllIncsC()

def getCompilerOpts( m:ModuleHandle):
    opts = GCC_CompilerOpts(m.getGeneralCompilerOpts())
    return opts