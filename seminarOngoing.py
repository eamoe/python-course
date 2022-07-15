from importlib.resources import path
from pickle import TRUE
from turtle import clear
from typing import List
import library

#Reading a file
def file_reader(path, is_header = False):
    
    file = open(path, 'r')    
    lines = []

    if is_header == True:
        lines.append(file.readline().replace('\n', '').split(','))
    else:
        file.readline()
        for line in file:
            lines.append(line.replace('\n', '').split(','))
    
    file.close()
    
    return lines


#Main Program

path = 'issues.csv'

#Read the file header
header = file_reader(path, True)

#Read the file body
body = file_reader(path, False)

print(header)

for line in body:
    print(line)