import re
import uuid
from app.classifiers import *
from app.db import redis_client as redis


class Entry:
    def __init__(self, entry):
        self.entry = entry
        self.spam = spam.check(entry)
        self.relevance = None
        self.sentiment = None
        self.stories = None
        self.symbols = [rr.replace('$', '') for rr in re.findall('\$[A-Z]+', self.entry['text'])]
        self.id = uuid.uuid4().hex

    def __getitem__(self, item):
        return self.to_dict().get(item, None)

    def check_relevance(self):
        self.relevance = relevance.check(self)
        return self

    def check_sentiment(self):
        self.sentiment = sentiment.check(self)
        return self

    def check_stories(self):
        self.stories = stories.check(self)
        return self

    def add_to_stocks(self):
        for sym in self.symbols:
            redis.lpush(sym, self.id)
        return self

    def to_dict(self):
        data = self.entry
        meta = {
            'spam': self.spam,
            'relevance': self.relevance,
            'sentiment': self.sentiment,
            'stories': self.stories,
            'symbols': self.symbols
        }
        data.update(meta=meta)
        return data

    def save(self):
        redis.hmset(self.id, self.to_dict())
        return self

    def process(self):
        self.check_relevance()\
            .check_sentiment()\
            .check_stories()\
            .add_to_stocks()\
            .save()
        return self
