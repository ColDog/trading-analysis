from app.classifiers.spam import Spam

spam = Spam()
assert spam.classifier is not None, spam.classifier
