from pymakelib.Module import AbstractModule, ModuleClass, ModuleHandle, StaticLibrary
from pymakelib.Module import getModuleInstance, cleanModuleInstance
import importlib.util
import copy
from pymakelib import log
from abc import ABC,abstractmethod

class ExternalModule(AbstractModule):
    
    def __init__(self, path):
        super().__init__(path)
        try:
            modPath = self.getModulePath()
            if not modPath.endswith("_mk.py"):
                raise AttributeError(f"{modPath} is not a valid module path")
            lib = importlib.util.spec_from_file_location(str(modPath), str(modPath))
            mod = importlib.util.module_from_spec(lib)
            rep = lib.loader.exec_module(mod)
            obj = getModuleInstance()[0]
            log.debug(f"create copy of module object {obj.__class__}")
            self.remoteModule = copy.deepcopy(obj)
            cleanModuleInstance()
        except Exception as ex:
            log.exception(ex)
            exit(-1)
    
    @abstractmethod
    def getModulePath(self)->str:
        pass

    def init(self, mh:ModuleHandle):
        try:
            return self.remoteModule.init(mh)
        except AttributeError as ae:
            log.debug(ae)
        except Exception as ex:
            log.exception(ex)
            exit(-1)

    def getSrcs(self, mh:ModuleHandle):
        return self.remoteModule.getSrcs(mh)
        
    def getIncs(self, mh:ModuleHandle):
        return self.remoteModule.getIncs(mh)
    
    def getCompilerOpts(self, mh:ModuleHandle):
        try:
            return self.remoteModule.getCompilerOpts(mh)
        except AttributeError as ae:
            log.debug(ae)
        except Exception as ex:
            log.exception(ex)
            exit(-1)
    
@ModuleClass
class ExtLib(ExternalModule):
    
    def init(self, mh:ModuleHandle):
        return StaticLibrary("modulelib", "Release", rebuild=True)
    
    def getModulePath(self)->str:
        return '/PROJECTS/PYTHON/test_module_lib/module_lib/module_lib_mk.py'
    
  