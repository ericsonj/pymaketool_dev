from pymakelib import module
from pymakelib.module import StaticLibrary
import subprocess


# class ESPComponentLib(module.AbstractModule):
#     # make -f ESP_Makefile /home/ericson/PROJECTS/ESP32/esp32hello/build/app_trace/libapp_trace.a

#     def init(self):
#         staticLib = StaticLibrary(name='app_trace', outputDir="build/app_trace/")
#         try:
#             if mh.getGoal() == 'all':
#                 subprocess.call('make', '-f', 'ESP_Makefile', '/home/ericson/PROJECTS/ESP32/esp32hello/build/app_trace/libapp_trace.a')  
#         except Exception as e:
#                 print(e)
#         return staticLib

#     def getSrcs(m):
#         return None

#     def getIncs(m):
#         return None


@module.ModuleClass
class app_trace(module.AbstractModule):
    def init(self):
        staticLib = StaticLibrary(name='app_trace', outputDir="build/app_trace/", lib_linked_opts="-u esp_app_desc", orden=2)
        staticLib.lib_objs = ""
        staticLib.lib_objs_compile = ""
        command = "make -f ESP_Makefile /home/ericson/PROJECTS/ESP32/esp32hello/build/app_trace/libapp_trace.a"
        staticLib.lib_compile = f"$({staticLib.mkkey}_AR):\n\t$(call logger-compile,\"AR\",$@)\n\t{command}"
        return staticLib

    def getSrcs(m):
        return None

    def getIncs(m):
        return None