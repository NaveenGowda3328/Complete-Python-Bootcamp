# Two types of modules in Python:
# 1. Built-in modules: These are part of the  Python standard library and can be imported directly.
# 2. External modules: These are third-party  libraries that can be installed via package managers like pip.
# List of all the bulit-in modules in Python:
# https://docs.python.org/3/py-modindex.html

import math  
# import os    
# print(os.getcwd())  # Output: Current working directory
print(math.sqrt(16))  # Output: 4.0
# os.abort # This will raise an OSError, terminating the program

#importing a module
import mymodule  
mymodule.hello()  # Assuming mymodule has a function hello()
# Importing specific functions from a module
# import requests # pip libraries
# r = requests.get('https://www.google.com') its not working in my computer


