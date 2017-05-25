import datetime
import calendar
import json
import pytumblr
from tumblr_keys import *
from time import gmtime, strftime
import time
from datetime import datetime

date = strftime("%d.%m.%Y %H:%M:%S", gmtime())
print date

d = datetime.strptime(date, "%d.%m.%Y %H:%M:%S")
ts = time.mktime(d.timetuple())
print int(ts)


# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    token_key,
    token_secret
)

main_list = client.tagged('sience', before=ts)

prime_dict = {}
for i in main_list:
    print i['note_count'],' -> ', i['post_url']
    if i['note_count'] not in prime_dict:
        prime_dict[i['note_count']] = set()
        prime_dict[i['note_count']].add(i["post_url"])
    else:
        prime_dict[i['note_count']].add(i["post_url"])


print prime_dict
