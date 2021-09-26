#!/usr/bin/env python3

"""Imports"""

import os
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    args = ""

    """Handles multiple arguments for different processes."""
    if len(arguments) > 1:
        for argument in arguments:
            args += " -e " + argument
    else:
        args = arguments[0]

"""Instead of a loop through the entire process list, I grab what the user is looking for directly."""
process_raw = os.popen('ps aux | grep {}'.format(args)).read().splitlines()

"""Formatting"""
formated_processes = list()

for line in process_raw:
        process = line.split()
        formated_processes.append(
            {
                'pid'     : process[1],
                'user'    : process[0],
                'cpu'     : process[2],
                'mem'     : process[3],
                'started' : process[8],
                'elapsed' : process[9],
                'path'    : process[10]
            }
        )


"""Kill logic and printing."""
if len(arguments) > 1:
    for process in formated_processes:
        print(
        "[{}] {} (User) {}% (CPU) {}% (Mem) {} (Started) {} (Elapsed) {}".format(
        process['pid'], process['user'], process['cpu'], process['mem'], process['started'], process['elapsed'], process['elapsed']
        )
    )
else:
    #print("pkill {}".format(formated_processes[0]['pid']))
    os.system("kill {}".format(formated_processes[0]['pid']))
    print("Process killed!")