from app.scrapers.twitter import Twitter
from app.db import redis_trainer
from app.classifiers.spam import Spam
from app.entry import Entry
import uuid


def new_spam_trainer(entry):
    uid = uuid.uuid4().hex
    redis_trainer.hmset('trainer:spam:' + uid, entry)
    redis_trainer.lpush('trainer:spam:keys', 'trainer:spam:' + uid)


def train_spam():
    res = Twitter().data()
    for twt in res:
        try:
            print(twt['user']['name'], twt['text'])
            verdict = input('Spam (1 = yes, 0 = no): ')
            new_spam_trainer(
                Spam.feature_set(
                    Entry(
                        {'text': twt['text'], 'author': twt['user']['name'], 'verdict': verdict}
                    )
                )
            )
        except KeyboardInterrupt:
            break
