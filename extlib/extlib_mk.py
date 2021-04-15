from pymakelib import module

@module.ModuleClass
class ExtLib(module.ExternalModule):
    
    def init(self):
        return module.StaticLibrary("modulelib", "Release", rebuild=True, orden=1)
     
    def getModulePath(self)->str:
        return '/SURIX/IPAC/nipac2/Middlewares/surix-lib/codecs/g722/g722_mk.py'
     
