from pymakelib.Module import ModuleClass, ModuleHandle, AbstractModule
from abc import abstractmethod
import sys
from pathlib import Path

def define(key, value):
    print(f"#define {key:24} {value}")

def enum(names, values):
    resp = ''
    resp += "enum {\n"
    idx = 0
    for n in names:
        v = None
        try:
            v = values[idx]
        except:
            pass
        if v:
            resp += f"    {n} = {v},\n"
        else:
            resp += f"    {n},\n"
        idx += 1
    resp += "};\n"
    return resp


def enum_sf(strformat, range, init=0):
    values = []
    for r in range:
        values.append(strformat.format(r))
    return enum(values, [init])


def cstrarray(name, values):
    resp = ''
    resp += f"const char* {name}[{len(values)}] = "+"{\n"
    for v in values:
        resp += f"    \"{v}\",\n"
    resp += "};\n"
    return resp


def iheader(fun):
    name = str(Path(__file__).name)
    name = name.replace('.h', '_H')
    name = name.replace('.py', '')
    name = name.upper()
    name = f"_{name}_"
    # ifndef _LIB_H_
    # define _LIB_H_
    print(f"#ifndef {name}")
    print(f"#define {name}")
    print('\n')
    fun()
    print(f"#endif // {name}")


class PyGenHeaderFile(AbstractModule):

    def init(self, mh: ModuleHandle):
        filename = self.getFileName()
        filename = filename.replace('_mk.py', '.h')
        # print(filename)
        # stdout_ = sys.stdout #Keep track of the previous value.
        # sys.stdout = open(filename, 'w') # Something here that provides a write method.
        name = filename.replace('/', '_')
        name = name.replace('.h', '_H')
        name = name.upper()
        name = f"_{name}_"
        print(f"#ifndef {name}")
        print(f"#define {name}")
        print('\n')
        self.generateFile(mh)
        print('\n')
        print(f"#endif // {name}")
        # sys.stdout = stdout_ # restore the previous stdout.
        return super().init(mh)

    def getSrcs(self, mh: ModuleHandle) -> list:
        return None

    def getIncs(self, mh: ModuleHandle) -> list:
        return None

    @abstractmethod
    def getFileName(self) -> str:
        pass

    @abstractmethod
    def headerFile(self, mh: ModuleHandle):
        pass


@ModuleClass
class Mods(PyGenHeaderFile):
    
    def getFileName(self) -> str:
        return __file__

    def headerFile(self, mh: ModuleHandle):
        d = mh.getGeneralCompilerOpts().opts['MACROS']
        
        modules = [
            'mod',
        ]

        for m in modules:
            if m in d:
                define(m, f"_MODULE({m})")
