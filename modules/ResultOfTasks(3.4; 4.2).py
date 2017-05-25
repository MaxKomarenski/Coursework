import datetime
import calendar
import json
import pytumblr
from tumblr_keys import *
from time import gmtime, strftime
import time
from datetime import datetime

def check_time():
    """
    This function return exact time.
    """
    date = strftime("%d.%m.%Y %H:%M:%S", gmtime())
    return date

def code_time():
    """
    This function return coded time by timestamp coding
    """
    d = datetime.strptime(check_time(), "%d.%m.%Y %H:%M:%S")
    ts = time.mktime(d.timetuple())
    return int(ts)

print check_time()
print code_time()


# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    token_key,
    token_secret
)

main_list = client.tagged('sience', before=code_time())

prime_dict = {}
for i in main_list:
    if i['note_count'] not in prime_dict:
        prime_dict[i['note_count']] = set()
        prime_dict[i['note_count']].add(i["post_url"])
    else:
        prime_dict[i['note_count']].add(i["post_url"])


for i in reversed(prime_dict.keys()):
    for j in prime_dict[i]:
        print i, "-", j
