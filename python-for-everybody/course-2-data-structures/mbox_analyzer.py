def show_all_senders():
    fname = input("Enter a file name: ")
    ofile = open(fname)
    senders = dict()
    for line in ofile:
        if line.startswith("From "):
            words = line.split()
            sender = words[1]
            senders[sender] = senders.get(sender,0) + 1
    print(senders)

def Show_most_frequent_sender():
    fname = input("Enter a file name: ")
    ofile = open(fname)
    senders = dict()
    for line in ofile:
        if line.startswith("From "):
            words = line.split()
            sender = words[1]
            senders[sender] = senders.get(sender,0) + 1
    count = 0
    email_count = None
    for key,value in senders.items():
        if value > count:
            count = value
            email_count = key
    print(email_count,count)

def Show_email_count_by_hour():
    fname = input("Enter a file name: ")
    ofile = open(fname)
    emails = dict()
    for line in ofile:
        if line.startswith("From "):
            words = line.split()
            time = words[5]
            hour = time.split(":")[0]
            emails[hour] = emails.get(hour,0) + 1
    list1 = list()
    for key,value in emails.items():
        tup = (key,value)
        list1.append(tup)
    list1 = sorted(list1)
    for key,value in list1:
        print(key,value)

def Show_average_spam_confidence():
    fname = input("Enter a file name: ")
    ofile = open(fname)
    count = 0
    total = 0
    for line in ofile:
        if line.startswith("X-DSPAM-Confidence: "):
            count = count + 1
            value = float(line.split(":")[1])
            total = total + value
    if count > 0:
        average = total/count
        print("The total spam confidence is:",average)
    else:
        print("Data of spam confidence not found")

while True:
    print("\n1. Show all senders \n2. Show most frequent sender \n3. Show email count by hour \n4. Show average spam confidence \n5. Exit")
    
    try:
        choice = int(input("Enter your choice: ")) 
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue

    if choice == 1:
        show_all_senders()
    elif choice == 2:
        Show_most_frequent_sender()
    elif choice == 3:
        Show_email_count_by_hour()
    elif choice == 4:
        Show_average_spam_confidence()
    elif choice == 5:
        print("Ending")
        break
    else:
        print("Selection out of range. Try again.")