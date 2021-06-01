# Exercise 4: Add code to the above program to figure out who has the most messages in the file.
# After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop
# (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.
#
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
#
# Enter a file name: mbox.txt
# zqian@umich.edu 195
#
#  >>>>>>>>>>>>>>>>>>>>>


usr_inp = input('enter file name >>> ')
fhandl = open(usr_inp)

prsd_lines = list()
count = 0
for line in fhandl:
    l_splt = line.split()
    # print(words)
    # if len(words) < 1 or words == '' or words[0] != 'From':
    #     print('IGNORE', words)
    if len(l_splt) < 1 or l_splt == '' or l_splt[0] != 'From': continue
    else :
        prsd_lines.append(l_splt[1])
        count += 1
if count == 0 :
        print('NOT DETECTED')


d = dict()
for words in prsd_lines :
    d[words] = d.get(words,0) + 1


def dct_max_fun(d) :
    max_val = 0
    max_key = None
    for key,count in d.items():
# code from PY4E discussion, by Arran Patterson
# if max is None or count > bigcount:
        if count > max_val :
            max_val = count
            max_key = key
    # print(max_key, max_val)
    print('the MOST emails, {0}, were sent by {1}'.format(max_val, max_key))


def dct_min_fun(d) :
    min_val = 1
    min_key = None
    for key,count in d.items():
        if count == 1 or count < min_val :
            min_val = count
            min_key = key
    # print(min_key, min_val)
    print('the LEAST emails, {0}, were sent by {1}'.format(min_val, min_key))


dct_max_fun(d)
dct_min_fun(d)
#  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
### geeks for geeks
## Using min() + list comprehension + values()
## Finding min value keys in dictionary
# temp = min(test_dict.values())
# res = [key for key in test_dict if test_dict[key] == temp]