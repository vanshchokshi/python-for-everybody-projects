# 7.1 Write a program that prompts for a file name, then opens
# that file and reads through the file, and print the contents 
# of the file in upper case. Use the file words.txt to produce 
# the output below.
# You can download the sample data at 
# http://www.py4e.com/code3/words.txt

file_name = input("Enter the name of the file: ")
open_file = open(file_name)
for line in open_file:
    line = line.rstrip()
    upper_case = line.upper()
    print(upper_case)