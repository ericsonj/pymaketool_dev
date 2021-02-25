from pymakelib.Module import ExternalModule, ModuleClass, ModuleHandle, StaticLibrary


@ModuleClass
class ExtLib(ExternalModule):
    
    def init(self, mh:ModuleHandle):
        return StaticLibrary("modulelib", "Release", rebuild=True)
     
    def getModulePath(self)->str:
        return '/PROJECTS/PYTHON/test_module_lib/module_lib/module_lib_mk.py'
     
