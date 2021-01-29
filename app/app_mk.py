from pymakelib.Module import ModuleHandle


def getSrcs(m: ModuleHandle):
    return m.getAllSrcsC()


def getIncs(m: ModuleHandle):
    return m.getAllIncsC()