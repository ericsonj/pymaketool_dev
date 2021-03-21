import datetime
import os
from pathlib import Path
from pymakelib import nproject

class Cproject(nproject.BasicGenerator):

    def info(self):
        return {
            "name": "C Project",
            "desc": "C Project Template"
        }

    def temp_files(self):
        return [
            'app/inc/main.h',
            'app/src/main.c',
            'app/app_mk.py',
            'makefile.mk',
            'Makefile',
            'Makefile.py',
            ".project",
            ".pymakeproj/.cproject_template",
            ".pymakeproj/.language.settings_template",
            ".settings",
        ]

    def get_attrs(self) -> dict:

        temp_tokens = {
            'author':       'Ericson Joseph',
            'date':         datetime.datetime.now().strftime('%b-%d-%I%M%p-%G'),
            'project_name': 'c_temp'
        }
        temp_tokens['name']         = input("Your name: ")
        temp_tokens['project_name'] = input("Your project name: ")

        output_dir = Path( Path(os.getcwd()) / Path(temp_tokens['project_name'])) 

        return {
            "temp_name":        "c_project",
            "temp_gzip_file":   "/home/ericson/PROJECTS/PYTHON/pynewproject_c/pynewproject_c_project/templates/c_project.tar.gz",
            "temp_files":       self.temp_files(),
            "temp_tokens":      temp_tokens,
            "output_folder":    output_dir,
        }
