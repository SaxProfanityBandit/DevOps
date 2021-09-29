#!/usr/bin/env python3
#Yell.py!
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Yell something out!")
    #group = parser.add_mutually_exclusive_group()

    parser.add_argument('-y', '--yell', help="Yell a string with exclemation marks.", action="store_true")
    parser.add_argument('-q', '--question', help="Makes it a question that you yell!", action="store_true")
    #parser.add_argument('line', nargs=argparse.REMAINDER)
    parser.add_argument('text', help="The input that you want to yell.")
    

    arguments = parser.parse_args()

    
    if (len(arguments.text) > 0):
        if (arguments.yell and arguments.question):
            print(arguments.text.upper() + "!?!?!?")
        elif (arguments.yell):
            print(arguments.text.upper() + "!!!")
        elif (arguments.question):
            print(arguments.text.upper() + "???")
        else:
            print(arguments.text.upper())
    else:
        print("You didn't enter anything to yell!")