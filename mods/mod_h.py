from pymakelib.pycodegen import *

@HEADER_FILE(name=__file__)
def header_file():

    if defined('mod'):
        out("#define mod      _MODULE(mod)")

    if defined('mod2'):
        out("#define mod2     _MODULE(mod2)")

    comment("""
    Key map
    """)
    
    enum_sf("KEY_{}", range(1,20), init=1)

    cstrarray("names", ["NAME1", "NAME2"])