#!/usr/bin/env python3

"""Imports"""

import os
import sys
import argparse

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

"""Formatting and filtering"""
formated_processes = list()

for line in process_raw:

    if "python3" in line or "/bin/sh" in line or "grep" in line:
        continue

    process = line.split()
    line_args = process[11:]
    arg_string = ""
    for arg in line_args:
        arg_string += arg + " "

    formated_processes.append(
        {
            'pid'     : process[1],
            'user'    : process[0],
            'cpu'     : process[2],
            'mem'     : process[3],
            'started' : process[8],
            'elapsed' : process[9],
            'path'    : process[10],
            'args'    : arg_string                    
        }
    )

"""Kill logic and printing."""
if len(formated_processes) == 0:
    print("Couldn't find the process you were looking for!")

elif len(formated_processes) > 1 or " -i " in args:
    for process in formated_processes:
        print(
        "[{}] {} (User) {}% (CPU) {}% (Mem) {} (Started) {} (Elapsed) {} {}".format(
        process['pid'], process['user'], process['cpu'], process['mem'], process['started'], process['elapsed'], process['path'], process['args']
        )
    )

elif len(formated_processes) == 1:
    os.system("kill {}".format(formated_processes[0]['pid']))
    print("Terminated process with PID: {}".format(formated_processes[0]['pid']))
    
    
    