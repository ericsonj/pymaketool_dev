import os
from os.path import basename
from pymakelib import AbstractMake, Makeclass
from pymakelib import MKVARS
from pymakelib import toolchain as tool
from pymakelib import addon
from pymakelib.eclipse_addon import EclipseAddon
from pymakelib import Define as D
from pymakelib import pym

# Import addons
from scripts.vscode_addon import vscode_init

# Add addons
addon.add(EclipseAddon)
addon.add(vscode_init)

@Makeclass
class Project(AbstractMake):

    LIBRARIES = []

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
            'TARGET_TEST': {
                'LOGKEY':  'TEST',
                'FILE':     'hola.text',
                'SCRIPT': ['touch', 'hola.text']
            },
            'TARGET': {
                'LOGKEY':  'OUT',
                'FILE':    TARGET,
                'SCRIPT':  [MKVARS.LD, '-o', '$@', MKVARS.OBJECTS, MKVARS.LDFLAGS, MKVARS.STATIC_LIBS]
            },
            'TARGET_ZIP': {
                'LOGKEY':   'ZIP',
                'FILE':     TARGET + '.zip',
                'SCRIPT':   ['zip', TARGET + '.zip', MKVARS.TARGET]
            }
        }

        return TARGETS


    def getCompilerSet(self, **kwargs):
        return tool.get_gcc_linux()

    def getCompilerOpts(self, **kwargs):
        PROJECT_DEF = {
            "__TEST_DEFINE__":   1,
            'mod':               None,
            'mod2':              D('web.h'),
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
            'LIBRARIES': self.LIBRARIES
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
            'LIBRARIES': self.LIBRARIES
        }


pym.add_library(
    "test",
    "Release",
    srcs=[
        'test.c'
    ],
    incs=[
        "inc"
    ]
)