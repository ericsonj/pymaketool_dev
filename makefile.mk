# Copyright (c) 2020, Ericson Joseph
# 
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright notice,
#       this list of conditions and the following disclaimer in the documentation
#       and/or other materials provided with the distribution.
#     * Neither the name of pyMakeTool nor the names of its contributors
#       may be used to endorse or promote products derived from this software
#       without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


## Local functions
define logger-compile
	@printf "%6s\t%-30s\n" $(1) $(2)
endef

define logger-compile-lib
	@printf "%6s\t%-25s %-30s\n" $(1) $(2) $(3)
endef

.DEFAULT_GOAL := all

CSRC  =
ASSRC = 
INCS  = 
COMPILER_FLAGS =
SLIBS_OBJECTS = 
SLIBS_NAMES = 
SRC_DIRS =

include vars.mk
include srcs.mk

OBJECTS = $(CSRC:%.c=$(PROJECT_OUT)/%.o) $(ASSRC:%.s=$(PROJECT_OUT)/%.o)

include targets.mk

%.o : CFLAGS = $(COMPILER_FLAGS)


$(PROJECT_OUT)/%.o: %.c
	$(call logger-compile,"CC",$<)
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) $(INCS) -o $@ -c $<


$(PROJECT_OUT)/%.o: %.s
	$(call logger-compile,"AS",$<)
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) $(INCS) -o $@ -c $<


all: $(TARGETS)

clean: clean_targets
	@echo 'CLEAN'
	rm -f $(addsuffix /*, $(addprefix $(PROJECT_OUT)/,$(SRC_DIRS)))

cleanlibs:
	rm -rf $(SLIBS_OBJECTS:%.a=%.cksum)	

.PHONY: clean cleanlibs

-include $(OBJECTS:.o=.d)

.FORCE:
