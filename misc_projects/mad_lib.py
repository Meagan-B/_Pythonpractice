#http://data.pr4e.org/romeo.txt

# >>>>>>>>>>>>>>>>>>>>>>>

import urllib.request
# ----
usr_host = str(input('enter URL below\n>>> '))
usr_host = usr_host.rstrip()
# ----
with urllib.request.urlopen(usr_host) as response :
    html = response.read()
    html = html.decode()
    # print(type(html))