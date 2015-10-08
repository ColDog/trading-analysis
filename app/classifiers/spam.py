import nltk
from app.db import get_spam_trainers
from app.utils import freq


class Spam:

    @staticmethod
    def feature_set(entry):
        data = entry.to_dict()
        print('feature', data)
        data.update(words=freq(entry['text']))
        return data

    def __init__(self):
        self.classifier = None
        self.train()

    def train(self):
        training_set = []
        trainers = get_spam_trainers()
        print('trainers', trainers)
        if trainers:
            for trainer in trainers:
                verdict = trainer.pop('verdict')
                training_set.append((trainer, verdict))
            self.classifier = nltk.NaiveBayesClassifier.train(training_set)

    def check(self, entry):
        if self.classifier:
            return self.classifier.classify(self.feature_set(entry))
