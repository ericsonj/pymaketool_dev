from pymakelib import pym
from pymakelib import project

pym.add_library (
    name="lib",
    outputdir=project.get_base_build()
)
