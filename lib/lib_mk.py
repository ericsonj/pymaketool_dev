from pymakelib import module

def add_library(name, outputdir):

    @module.ModuleClass
    class _(module.BasicCModule, module.StaticLibraryModule):
        
        def get_module_name(self):
            return str(name).capitalize()

        def get_name(self) -> str:
            return name

        def get_output_dir(self) -> str:
            return outputdir

add_library(name="Lib", outputdir="Release")
