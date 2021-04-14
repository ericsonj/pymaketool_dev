from pymakelib import module
from pymakelib import project
from pymakelib import Logger

log = Logger.getLogger()

@module.ModuleClass
class Lib(module.StaticLibraryModule):
    
    def get_name(self) -> str:
        return "lib"

    def get_output_dir(self) -> str:
        return "Release"

    def getSrcs(self):
        return self.getAllSrcsC()

    def getIncs(self):
        return self.getAllIncsC()
