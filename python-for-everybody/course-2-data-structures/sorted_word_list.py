# 8.4 Open the file romeo.txt and read it line by line. For 
# each line, split the line into a list of words using the 
# split() method. The program should build a list of words. 
# For each word on each line check to see if the word is 
# already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting 
# words in python sort() order as shown in the desired output.
# You can download the sample data at 
# http://www.py4e.com/code3/romeo.txt

file_name = input("Enter the file name: ")
open_file = open(file_name)
list1 = []
for line in open_file:
    words = line.split()
    for word in words:
        list1.append(word)
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
list2.sort()
print(list2)