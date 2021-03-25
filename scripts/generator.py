import tarfile
import tempfile
import re
import datetime
from pathlib import Path
from pkg_resources import resource_filename

class Generator:

    def __init__(self, temp_name, temp_gzip_file, temp_files, temp_tokens):
        self.temp_name = temp_name
        self.temp_gzip_file = temp_gzip_file
        self.temp_files = temp_files
        self.temp_tokens = temp_tokens

    def copyFile(self, input_file, output_file, tokens: dict):
        p = Path(output_file.parent)
        p.mkdir(parents=True, exist_ok=True)
        input_file = open(input_file, 'r')
        output_file = open(output_file, 'w')
        for line in input_file:
            for token, value in tokens.items():
                line = re.sub("<%=[ ]*" + token + "[ ]*%>", value, line)
            output_file.write(line)

    def generate(self, ouput_folder):

        gzipfile = Path(self.temp_gzip_file)
        if not  gzipfile.exists():
            print(f"File {str(gzipfile)} not found")
            exit(1)

        tmpdir = tempfile.TemporaryDirectory()
        gzipobj = tarfile.open(gzipfile)
        gzipobj.extractall(tmpdir.name)
        gzipobj.close()

        dir_tmptemp = Path(Path(tmpdir.name) / Path(self.temp_name))

        for tp in temp_files:
            fin = Path(dir_tmptemp / Path(tp))
            if fin.exists():
                fout = Path(Path(output_dir) / Path(tp))
                print("{0} > {1}".format(str(fin), str(fout)))
                if fin.is_dir():
                    fout.mkdir(parents=True, exist_ok=True)
                else:
                    self.copyFile(fin, fout, temp_tokens)


output_dir = '/tmp/c_temp'

temp_name = 'c_project'

temp_files = [
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

temp_tokens = {
    'author':       'Ericson Joseph',
    'date':         datetime.datetime.now().strftime('%b-%d-%I%M%p-%G'),
    'project_name': 'c_temp'

}

g = Generator("c_project", "/tmp/c_project.tar.gz", temp_files, temp_tokens)
g.generate(output_dir)