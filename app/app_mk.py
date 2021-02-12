from pymakelib.Module import ModuleHandle


def getSrcs(m: ModuleHandle):
    return m.getAllSrcsC()


def getIncs(m: ModuleHandle):
    return m.getAllIncsC()

def getCompilerOpts( m:ModuleHandle):
    opts = m.getGeneralCompilerOpts()
    opts.setOption('CONTROL-C-OPTS', ['-std=gnu11'])
    return opts