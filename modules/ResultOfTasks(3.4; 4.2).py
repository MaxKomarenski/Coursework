import datetime
import calendar
import json
import pytumblr
from tumblr_keys import *
from time import gmtime, strftime
import time
from datetime import datetime

prime_dict = {}

client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    token_key,
    token_secret
)

class TumblerProgram():
    def __init__(self, tag):
        self.tag = tag

    def exact_time(self):
        """
        This method returns exact time.
        """
        date = strftime("%d.%m.%Y %H:%M:%S", gmtime())
        return date

    def code_time(self):
        """
        This method returns number of coded time by timestamp coding.
        """
        d = datetime.strptime(self.exact_time(), "%d.%m.%Y %H:%M:%S")
        ts = time.mktime(d.timetuple())
        return int(ts)

    def main_list(self):
        """
        This method returns list of whole information what has to be worked out.
        """
        return client.tagged(self.tag)

    def main_dict(self):
        """
        This method returns dictionary where keys are count of notes
        and values are links of posts.
        """
        for i in self.main_list():
            if i['note_count'] not in prime_dict:
                prime_dict[i['note_count']] = set()
                prime_dict[i['note_count']].add(i["post_url"])
            else:
                prime_dict[i['note_count']].add(i["post_url"])
        return prime_dict

    def result(self):
        """
        This method returns strings of notes and links on posts
        """
        for i in reversed(sorted(self.main_dict().keys())):
            for j in self.main_dict()[i]:
                print i, "-", j

a = TumblerProgram('lol')
print a.result()
