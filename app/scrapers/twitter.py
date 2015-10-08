from TwitterAPI import TwitterAPI

from app.scrapers.keywords import twitter_track


class Twitter:
    def __init__(self):
        self.api = TwitterAPI(
                'LmACQX3XV1c9rA05MfYVbB9OG',
                'ik7nVuZ0AtXffKjnqCjdCN1rTFVmod7Leehwbx1mezEDXCZAx8',
                '2899747854-L4CzMtqL6BJQLsXNjs64xKavFqAPf3bPgspn4Aq',
                '7zy5QY2hIKwzyUbJ5X9gPDluAoLbOzrFongjqFAiMI8dN'
            )

    def data(self):
        return self.api.request('statuses/filter', {'track': twitter_track()})
