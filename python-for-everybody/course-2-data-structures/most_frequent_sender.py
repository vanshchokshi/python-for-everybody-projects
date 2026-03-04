# 9.4 Write a program to read through the mbox-short.txt and 
# figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word 
# of those lines as the person who sent the mail. The program 
# creates a Python dictionary that maps the sender's mail 
# address to a count of the number of times they appear in the 
# file. After the dictionary is produced, the program reads 
# through the dictionary using a maximum loop to find the most 
# prolific committer.

emails = {}

name = input("Enter file name: ")
handle = open(name)

for line in handle:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        emails[email] = emails.get(email, 0) + 1

count = 0
email_count = None
for key,value in emails.items():
    if value > count:
        count = value
        email_count = key
print(email_count,count)