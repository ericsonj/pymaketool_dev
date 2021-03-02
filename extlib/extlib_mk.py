from pymakelib import Module

@Module.ModuleClass
class ExtLib(Module.ExternalModule):
    
    def init(self):
        return Module.StaticLibrary("modulelib", "Release", rebuild=True)
     
    def getModulePath(self)->str:
        return '/PROJECTS/PYTHON/test_module_lib/module_lib/module_lib_mk.py'
     
