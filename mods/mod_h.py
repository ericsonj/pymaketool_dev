from pymakelib import pycodegen as p


@p.HEADER_FILE(name = __file__)
def header_file():

    if p.defined('mod'):
        p.out("#define mod      _MODULE(mod)")

    if p.defined('mod2'):
        p.out("#define mod2     _MODULE(mod2)")

    p.comment("""
    Key map
    """)

    p.enum_sf("KEY_{}", range(1,20), init=1)

    p.enum_str_map("HTTP_REQUEST", {
        'HTTP_200': 'OK'
    })