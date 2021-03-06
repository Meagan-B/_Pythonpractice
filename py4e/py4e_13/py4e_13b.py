# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1154833.json (Sum ends with 33)
#
# You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
#
#
# Enter location: http://py4e-data.dr-chuck.net/comments_42.json
# Retrieving http://py4e-data.dr-chuck.net/comments_42.json
# Retrieved 2733 characters
# Count: 50
# Sum: 2...
# >>>>>>>>>>>>>>>>>>>>>>>

import urllib.request
import json
import ssl
import time

# ----

# url = 'http://py4e-data.dr-chuck.net/comments_42.json'
# url = 'http://py4e-data.dr-chuck.net/comments_1154833.json'
url = input('enter URL below\n>>> ')

# ----

# Ignore SSL certificate errors (from PY4E, because i do not understand, but need to use this code to test example)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# ----

response = urllib.request.urlopen(url, context=ctx)

data = json.loads(response.read())
# print(data)
# print(type(data))

# ----

# print('GATHERING, {0}'.format(url))
print('GATHERING')
time.sleep(.5)
print('......')
time.sleep(1)
print('...')
time.sleep(1)

# ----

counts = 0
sum = 0

for i in data['comments'] :
    # count += 1
    # print(i, type(i))
    c = int((i["count"]))
    counts += 1
    sum += c

# ----

print('number of users : {0}\nsum of all comments made: {1}'.format(counts, sum))

# ...........................
