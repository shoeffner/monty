# Errata:
# Instead of using these two statements:
#
#     import mazesolver.io
#     import mazesolver.solver
#
# It is besser to use the directory relative statements:

from . import io
from . import solver

# This basically allows to import mazesolver in the following directory
# structure:
#
#     working_directory
#     - solution
#         - mazesolver
#             - __init__.py
#             - io.py
#             - solver.py
#
# With the above mentioned imports, it's impossible to do:
#
#    import solution.mazesolver
#
# The corrected version with the dot notation (from . import...) allows this.
#
# For more information, please refer to PEP 328:
#
#     https://www.python.org/dev/peps/pep-0328/
#
