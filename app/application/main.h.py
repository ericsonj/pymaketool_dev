from pathlib import Path

def define(key, value):
    return f"#define {key} {value}"

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


def iheader(filename, *args):
    name = str(Path(filename).name)
    name = name.replace('.h', '_H')
    name = name.replace('.py', '')
    name = name.upper()
    name = f"_{name}_"
    # ifndef _LIB_H_
    # define _LIB_H_
    print(f"#ifndef {name}")
    print(f"#define {name}")
    print('\n')
    for a in args:
        print(a)
        print('\n')

    print(f"#endif // {name}")

#######################################
# main.h.py
#######################################




iheader(__file__,
        define('MAIN', 1),
        define('CONST', 5),
        enum(["ENUM1", "ENUM2"], [1]),
        enum_sf("KEY_{0}_{0}", range(1, 30), init=1)
        )


## main.h.py ----> main.h