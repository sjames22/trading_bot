from yfinance import data

from data import dataF


def signal_generator(df):
    open = df.Open.iloc[-1]
    close = df.Close.iloc[-1]
    previous_open = df.Open.iloc[-2]
    previous_close = df.Close.iloc[-2]

    # Bearish Pattern
    if (open > close and
            close < previous_open < previous_close <= open):
        return 1

    # Bullish Pattern
    elif (open < close and
          close > previous_open > previous_close >= open):
        return 2

    # No clear pattern
    else:
        return 0


signal = [0]
for i in range(1, len(dataF)):
    df = dataF[i - 1:i + 1]
    signal.append(signal_generator(df))
signal_generator(data)
dataF["signal"] = signal

dataF.signal.value_counts()

