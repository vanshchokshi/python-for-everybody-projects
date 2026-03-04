# 10.2 Write a program to read through the mbox-short.txt and 
# figure out the distribution by hour of the day for each of 
# the messages. You can pull the hour out from the 'From ' line 
# by finding the time and then splitting the string a second 
# time using a colon. From stephen.marquard@uct.ac.za Sat Jan  
# 5 09:14:16 2008 Once you have accumulated the counts for 
# each hour, print out the counts, sorted by hour as shown 
# below.

fname = input("Enter a file name: ")
ofile = open(fname)
char = dict()
for line in ofile:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        hour = time.split(":")[0]
        char[hour] = char.get(hour, 0) + 1
list1 = list()
for key,value in char.items():
    tup = (key,value)
    list1.append(tup)
list1 = sorted(list1)
for key,value in list1:
    print(key,value)