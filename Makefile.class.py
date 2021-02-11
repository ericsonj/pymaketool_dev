import os
from os.path import basename
from pymakelib import git
from pymakelib import MKVARS
from pymakelib import Toolchain as tool
from pymakelib.Addon import Addon
from pymakelib.eclipse_addon import EclipseAddon

# Import addons
from scripts.vscode_addon import vscode_init

# Add addons
Addon(EclipseAddon)
Addon(vscode_init)

from pymakelib import ProjectImp, Makeclass

@Makeclass
class Project(ProjectImp):

    def getProjectSettings(self, **kwargs):
        return {
            'PROJECT_NAME': basename(os.getcwd()),
            'FOLDER_OUT':   'Release/Objects/'
        }

    def getTargetsScript(self, **kwargs):
        PROJECT_NAME = basename(os.getcwd())
        FOLDER_OUT = 'Release/'
        TARGET = FOLDER_OUT + PROJECT_NAME

        TARGETS = {
            'TARGET': {
                'LOGKEY':  'OUT',
                'FILE':    TARGET,
                'SCRIPT':  [MKVARS.LD, '-o', '$@', MKVARS.OBJECTS, MKVARS.LDFLAGS]
            },
            'TARGET_ZIP': {
                'LOGKEY':   'ZIP',
                'FILE':     TARGET + '.zip',
                'SCRIPT':   ['zip', TARGET + '.zip', MKVARS.TARGET]
            }
        }

        return TARGETS


    def getCompilerSet(self, **kwargs):
        return tool.confLinuxGCC()

    def getCompilerOpts(self, **kwargs):
        LIBRARIES = []
        PROJECT_DEF = {
            "__TEST_DEFINE__": 1
        }

        return {
            'MACROS': PROJECT_DEF,
            'MACHINE-OPTS': [
            ],
            'OPTIMIZE-OPTS': [
            ],
            'OPTIONS': [
            ],
            'DEBUGGING-OPTS': [
                '-g3'
            ],
            'PREPROCESSOR-OPTS': [
                '-MP',
                '-MMD'
            ],
            'WARNINGS-OPTS': [
            ],
            'CONTROL-C-OPTS': [
                '-std=gnu11'
            ],
            'GENERAL-OPTS': [
            ],
            'LIBRARIES': LIBRARIES
        }

    def getLinkerOpts(self, **kwargs):
        return {
            'LINKER-SCRIPT': [
                '-Wl,-Map=Release/pymaketool_dev.map',
            ],
            'MACHINE-OPTS': [
            ],
            'GENERAL-OPTS': [
            ],
            'LINKER-OPTS': [
            ],
            'LIBRARIES': LIBRARIES
        }
