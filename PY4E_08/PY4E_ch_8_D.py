# Exercise 4: Find all unique words in a file
#
# List all unique words, sorted in alphabetical order,
# that are stored in a file romeo.txt containing a subset of Shakespeare’s work.
#
# download a copy of the file www.py4e.com/code3/romeo.txt.
# Create a list of unique words, which will contain the final result.
# Write a program to open the file romeo.txt and read it line by line. For each line,
# split the line into a list of words using the split function. For each word,
# check to see if the word is already in the list of unique words. If the word is not in the list of unique words,
# add it to the list. When the program completes, sort and print the list of unique words in alphabetical order.

ss_uniq_wrds = []

usr_inp = input('enter file name >>> ')
fhandle = open(usr_inp)

for lines in fhandle :
    words = lines.split()
    ss_uniq_wrds += words

print(ss_uniq_wrds)
