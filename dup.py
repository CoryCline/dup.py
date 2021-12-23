#!/usr/bin/python3

import sys

file = sys.argv[1]

def display(line):
    print(line)

def log(file, line):
    with open(file, 'a+') as f:
        f.write(line)

line = sys.stdin.read()
display(line)
log(file, line)
