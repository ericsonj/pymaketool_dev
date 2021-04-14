####################################################
#                  mods/mod_mk.py                  #
####################################################


INCS += -Imods



####################################################
#                  lib/lib_mk.py                   #
####################################################
CSRC += lib/src/lib.c

SRC_DIRS += lib/src

INCS += -Ilib/inc

Release/Objects/lib/src/lib.o : CFLAGS = -D__TEST_DEFINE__=1 -Dmod -Dmod2=web.h -g3 -MP -MMD -std=c99


####################################################
#            app/application/app_mk.py             #
####################################################
CSRC += app/application/main.c

SRC_DIRS += app/application

INCS += -Iapp/application



####################################################
#               extlib/extlib_mk.py                #
####################################################
MODULELIB_NAME = modulelib
MODULELIB_OUTPUT = Release
MODULELIB_AR = Release/libmodulelib.a

MODULELIB_CSRC += /PROJECTS/PYTHON/test_module_lib/module_lib/src/module_lib.c


INCS += -I/PROJECTS/PYTHON/test_module_lib/module_lib/inc


MODULELIB_OBJECTS = $(MODULELIB_CSRC:%.c=$(MODULELIB_OUTPUT)/%.o) $(MODULELIB_CSRC:%.s=$(MODULELIB_OUTPUT)/%.o)

$(MODULELIB_OUTPUT)/%.o: %.c
	$(call logger-compile-lib,"CC","Release/libmodulelib.a",$<)
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) $(INCS) -o $@ -c $<

$(MODULELIB_AR): $(MODULELIB_OBJECTS)
	$(call logger-compile,"AR",$@)
	$(AR) -rc $@ $(filter %.o,$(MODULELIB_OBJECTS))


SLIBS_NAMES += -LRelease -lmodulelib 
SLIBS_OBJECTS += Release/libmodulelib.a

$(MODULELIB_OUTPUT)//PROJECTS/PYTHON/test_module_lib/module_lib/src/module_lib.o : .FORCE



####################################################
#             staticlib/esp_libs_mk.py             #
####################################################
APP_TRACE_NAME = app_trace
APP_TRACE_OUTPUT = build/app_trace
APP_TRACE_AR = build/app_trace/libapp_trace.a





$(APP_TRACE_AR):
	$(call logger-compile,"AR",$@)
	make -f ESP_Makefile /home/ericson/PROJECTS/ESP32/esp32hello/build/app_trace/libapp_trace.a


SLIBS_NAMES += -Lbuild/app_trace -lapp_trace -u esp_app_desc
SLIBS_OBJECTS += build/app_trace/libapp_trace.a

