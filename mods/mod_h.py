from pymakelib import pycodegen as p
from pymakelib import Project

@p.HEADER_FILE(name = __file__)
def header_file():

    if Project.isdefined('mod'):
        p.out("#define DECL_MOD      _MODULE(mod)")

    if Project.define('mod2') == 'web2.h':
        p.out("#define DECL_MOD2     _MODULE(mod2)")

    p.comment("""
    Key map
    """)

    p.enum_sf("KEY_{}", range(1,20), init=1)

    p.enum_str_map("HTTP_REQUEST", {
        'HTTP_200': 'OK'
    })