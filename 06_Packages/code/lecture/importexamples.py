# Imports everything but keeps it inside the namespace of the module.
import os
import statistics

# Imports only a specific function or variable
from statistics import mode
from os import uname

# Imports everything. Don't use this unless you are sure what you do.
from statistics import *
from os import *

# Imports a specific submodule (only works with packages (wait for it))
import os.path
# import statistics.mode  # This does not work!