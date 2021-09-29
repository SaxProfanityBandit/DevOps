#Seperating the kill_by_name.py in multiple files/modules.

import os
import copy as c
#from dataclasses import dataclass

class Process(object):
    #ps_aux = list()
    #result = list()
    #args = ""

    def __init__(self, search):
        if len(search) > 1:
            for argument in search:
                self.args += " -e " + argument
        else:
            self.args = search[0]

        self.result = list()
        self.ps_aux = os.popen('ps aux | grep {}'.format(self.args)).read().splitlines()
        #print(self.ps_aux[0])

        for line in self.ps_aux:
            """Ignoring the script itself and the grep running as they will false flag for what we are looking for."""
            if "python3" in line or "/bin/sh" in line or "grep" in line:
                continue

            process = line.split()
            line_args = process[11:]
            arg_string = ""
            for arg in line_args:
                arg_string += arg + " "
                
            self.result.append(
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
            #print(self.result)
        

    def display_info(self):
        for process in self.result:
            print(
            "[{}] {} (User) {}% (CPU) {}% (Mem) {} (Started) {} (Elapsed) {} {}".format(
            process['pid'], process['user'], process['cpu'], process['mem'], process['started'], process['elapsed'], process['path'], process['args']
            )
        )
        return None
    
    def kill(self):
        if len(self.result) > 0:
            os.system("kill -9 {}".format(self.result[0]['pid']))
            print("Terminated process with PID: {}".format(self.result[0]['pid']))
        else:
            print("Couldn't find the process you were looking for. Shutting down.")
            return None
    
    def kill_all(self):
        if len(self.result) > 0:
            verify = input("Are you sure you want to kill all processes with name(y/n): {}\n".format(self.result[0]['path']))
            if len(verify) > 0:
                if verify.lower() == 'y':
                    print("Killing all proccesses with same name:")
                    os.system("killall -I {}".format((self.result[0]['path'])))
                else:
                    print("Aborted.")
                    return None
            else:
                print("You didn't type y or n, shutting down.")
                return None
        else:
            print("Couldn't find the process you were looking for. Shutting down.")
            return None
