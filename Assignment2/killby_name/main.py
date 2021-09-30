"""Imports - check requirements.txt"""

import os
import sys
import subprocess




#processes = os.system('ps aux')
#os.system('clear')
#print(processes)
#process = subprocess.run(['ps aux'], capture_output=True)
#print(process)

processes = subprocess.run(["ps", "aux"], capture_output=True)
print(processes)