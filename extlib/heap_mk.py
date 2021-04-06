from pymakelib.module import ModuleHandle


ESP_PATH = '/home/ericson/esp/esp-idf/components/'

heap = f"{ESP_PATH}heap"
srcs = f"{heap}"

def getSrcs(mk: ModuleHandle):
    return [
        f"{srcs}/heap_caps.c",
        f"{srcs}/heap_caps_init.c",
        f"{srcs}/multi_heap.c",
        f"{srcs}/heap_tlsf.c",
    ]
    
def getIncs(mk: ModuleHandle):
    return [
        f"{heap}/include",
        f"{heap}"
    ]


def getCompilerOpts(mk: ModuleHandle):
    opts = mk.getGeneralCompilerOpts()
    opts.setOption('OPTIONS', ['-DMULTI_HEAP_FREERTOS'])
    return opts