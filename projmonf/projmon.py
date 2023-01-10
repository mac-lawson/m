import os
import sys
def err(skk): print("\033[91m {}\033[00m" .format(skk))
def fix(skk): print("\033[92m {}\033[00m" .format(skk))

os.mkdir("./Projects/" + sys.argv[1])

directory = ("./Projects/" + sys.argv[1])
file_name = 'class.m++'
file_path = os.path.join(directory, file_name)

try:
    with open(file_path, 'w') as f:
        pass
    fix(f'Successfully created a new M++ project in the project directory {directory}')
except:
    err(f'An error occurred while creating a new M++ project')
