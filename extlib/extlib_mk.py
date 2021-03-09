from pymakelib import module

@module.ModuleClass
class ExtLib(module.ExternalModule):
    
    def init(self):
        return module.StaticLibrary("modulelib", "Release", rebuild=True)
     
    def getModulePath(self)->str:
        return '/PROJECTS/PYTHON/test_module_lib/module_lib/module_lib_mk.py'
     
