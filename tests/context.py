import os
import sys

pwd = os.path.dirname(__file__)
wtf = os.path.join(pwd, os.path.pardir)
parent_directory = os.path.abspath(wtf)
sys.path.insert(0, parent_directory)

import power_functions
