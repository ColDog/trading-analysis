from ftplib import FTP

from app.db import redis


class Reader:
    def __init__(self):
        self.raw = ''
        self.symbols = {}

    def read(self, s):
        self.raw += str(s)

    def parse(self):

        def strip_name(name):
            remove_list = ['Corp.', 'Inc.', 'Common', 'Stock', ',', 'Ltd.', '-', ' ']
            word_list = name.split(' ')
            return ' '.join([i for i in word_list if i not in remove_list]).replace(',', '')

        for line in self.raw.split("\\r\\n"):
            spl = line.split('|')
            if spl[0].split(':')[0] == 'File Creation Time':
                break
            self.symbols[spl[1]] = strip_name(spl[2])
        return self.symbols


def run():
    ftp = FTP('ftp.nasdaqtrader.com')
    ftp.login()
    ftp.cwd('SymbolDirectory')
    reader = Reader()
    ftp.retrbinary('RETR nasdaqtraded.txt', reader.read)
    ftp.quit()

    reader.parse()
    redis.hmset('symbols', reader.symbols)
    print('finished set', len(reader.symbols), 'symbols')
