import datetime
import calendar
import json
import pytumblr
from tumblr_keys import *
from time import gmtime, strftime
import time
from datetime import datetime

date = strftime("%d.%m.%Y %H:%M:%S", gmtime()) #exact time.

def code_time():
    """
    This function return number of coded time by timestamp coding.
    """
    d = datetime.strptime(date, "%d.%m.%Y %H:%M:%S")
    ts = time.mktime(d.timetuple())
    return int(ts)

client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    token_key,
    token_secret
)

main_list = client.tagged("lol") # Here you have to write the topic,that you wont to see

prime_dict = {}

def main_dict():
    """
    This function return dictionary where keys are count of notes
    and values are links of posts.
    """
    for i in main_list:
        if i['note_count'] not in prime_dict:
            prime_dict[i['note_count']] = set()
            prime_dict[i['note_count']].add(i["post_url"])
        else:
            prime_dict[i['note_count']].add(i["post_url"])
    return prime_dict

def result():
    """
    This function return sorted top of posts of current topic. 
    """
    for i in reversed(sorted(main_dict().keys())):
        for j in main_dict()[i]:
            print i, "-", j

print result()
