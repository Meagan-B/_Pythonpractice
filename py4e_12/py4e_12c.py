# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document. Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.
# >>>>>>>>>>>>>>>>>>>>>>>
import re
import urllib.request
# import time

# ----

usr_host = str(input('enter URL below\n>>> '))
usr_host = usr_host.rstrip()

# ----

with urllib.request.urlopen(usr_host) as response :
    html = response.read()
    links = re.findall(b'href="(http[s]?://.*?)"', html)
    for link in links :
        print(links.decode())



# ----


# print(type(usr_host), usr_host)
# ----
# data_collect = str()
#
# count = 0
# while True :
#     # time.sleep(0.05)
#     if len(data) < 1 : break
#     count += len(data)
#     print(data[:30].decode())
# print('{0} characters total, including HEADER'.format(count))
    # data_collect = data_collect.write(data.decode())

# ----

# links = re.findall(b'href="(http[s]?://.*?)"', u_fhand)
# for link in links :
#     print(links.decode())

# ----

# ----

# ----

# ----

# ...........................
