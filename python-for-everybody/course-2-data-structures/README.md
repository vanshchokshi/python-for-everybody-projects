# Course 2 – Python Data Structures

This folder contains programs created while completing **Course 2 of the Python for Everybody Specialization**.

The focus of this course was learning how to process and analyze text data using Python data structures such as **lists and dictionaries**.

Key concepts practiced:
- Lists
- Dictionaries
- File input/output
- String parsing
- Sorting data
- Counting patterns in data

---

# Programs

### build_sender_list.py
Reads a mailbox file and prints all sender email addresses from lines that start with `From `.  
Also counts how many sender lines appear in the file.

### sorted_word_list.py
Reads a text file and builds a list of **unique words** found in the file.  
The final list is sorted alphabetically.

### most_frequent_sender.py
Reads a mailbox file and determines which email address sent the most messages.

### parse_text_string.py
Extracts a floating-point number from a text string using string searching and slicing.

### uppercase_file_reader.py
Prompts the user for a filename and prints the contents of the file in uppercase.

### average_spam_confidence.py
Reads a mailbox file and calculates the average value of `X-DSPAM-Confidence`.

### email_hour_histogram.py
Counts how many emails were sent during each hour of the day and prints the results in sorted order.

---

# Master Project

### mbox_analyzer.py

This program combines multiple exercises into a single **mailbox analysis tool**.

The program allows the user to:

1. Display all email senders
2. Find the most frequent sender
3. Show the number of emails sent per hour
4. Calculate the average spam confidence value

This project demonstrates how multiple data processing techniques can be combined into a single Python application.

---

# Skills Practiced

Through these exercises and the master project I practiced:

- Parsing structured text data
- Using dictionaries for frequency analysis
- Sorting and organizing data
- Processing large text files
- Building small command-line data analysis tools