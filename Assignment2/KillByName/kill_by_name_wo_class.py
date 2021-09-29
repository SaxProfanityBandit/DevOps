#!/usr/bin/env python3

"""Imports"""
#import sys
import os
import argparse

if __name__ == "__main__":
    """Using argparse instead of sys.argv"""
    process_name = list()
    parser = argparse.ArgumentParser(description="Find/kill one or several processes by name.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i', '--info', help="Display information about a process rather than killing it.", action="store_true")
    group.add_argument('-f', '--force', help="Force kill all processes with the provided name. WARNING: Dangerous", action="store_true")
    parser.add_argument('processes', nargs=argparse.REMAINDER)
    arguments = parser.parse_args()
    args = ""

    """Handles multiple arguments for different processes. 
    To make grep understand we want to look for all of those,
    I loop through the arguments and format them into one single string
    called args, and they have then:
    Example:
    ./kill_by_name.py nano vim firefox
    -e nano -e vim -firefox
    meaning that grep can find them properly as it needs -e for more than one argument.
    """
    if len(arguments.processes) > 1:
        for process in arguments.processes:
            args += " -e " + process
    else:
        args = arguments.processes[0]

"""Instead of a loop through the entire process list, I grab what the user is looking for directly."""
process_raw = os.popen('ps aux | grep {}'.format(args)).read().splitlines()

"""Formatting and filtering"""
formated_processes = list()

for line in process_raw:

    """Ignoring the script itself and the grep running as they will false flag for what we are looking for."""
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
elif len(formated_processes) > 1 and arguments.force:
    print("Killing all proccesses with same name:")
    os.system("killall -I {}".format(formated_processes[0]['path']))
elif len(formated_processes) > 1 or arguments.info:
    for process in formated_processes:
        print(
        "[{}] {} (User) {}% (CPU) {}% (Mem) {} (Started) {} (Elapsed) {} {}".format(
        process['pid'], process['user'], process['cpu'], process['mem'], process['started'], process['elapsed'], process['path'], process['args']
        )
    )
elif len(formated_processes) == 1:
    os.system("kill {}".format(formated_processes[0]['pid']))
    print("Terminated process with PID: {}".format(formated_processes[0]['pid']))