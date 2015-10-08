from app.scrapers import *
from app.classifiers import *
from app.db import redis_client as redis
from app.entry import Entry


def run():
    for twt in twitter.data():
        Entry({'text': twt['text'], 'author': twt['user']['name']}).process()
