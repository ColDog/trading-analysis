keywords = {
    'aaii','return','downgrades','invest','stock','markets','bullish','ebitda','traded','assets',
    'dividends','suzeorman','trader','macd','investors','doji','charts','declines','investigation',
    'investment','commission','roi','profit','returned','aaii.com','tarp','analyst','stockmarket','losers',
    'brokerage','reversal','trading','derivatives','amex','valuations','breakouts','rich','chart','derivative',
    'daytrader','bond','bonds','buffettology','quarter','cboe','etf','broker','corporation','engulfing','djia',
    'stocks','candlestick','madoff','wealth','tips','breakout','bearish','antitrust','commodities','brokers',
    'profitability','harami','bluechip','stochastics','market','returns','trade',
    'wall street','buffet','reit','mortgage','crude','oil','s&p','technical analysis'
}


def twitter_track():
    st = ''
    for word in keywords:
        st += word + ','
    return st
