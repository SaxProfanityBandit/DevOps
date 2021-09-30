#!/usr/bin/env python3
#KillByName v2 - Class Refactored.
#import os
import argparse
import process

if __name__ == "__main__":
    """Using argparse instead of sys.argv"""
    process_name = list()
    parser = argparse.ArgumentParser(description="Find/kill one or several processes by name.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i', '--info', help="Display information about a process rather than killing it.", action="store_true")
    group.add_argument('-f', '--force', help="Force kill all processes with the provided name. WARNING: Dangerous", action="store_true")
    parser.add_argument('processes', nargs=argparse.REMAINDER)
    arguments = parser.parse_args()


def main(proc):
    if arguments.info:
        proc.display_info()
        return "Info"
    elif arguments.force:
        proc.kill_all()
        return "Force"
    else:
        proc.kill()
        return "Kill"

current_process = process.Process(arguments.processes)
result = main(current_process)
