import yfinance as yf

companyInfo = yf.Ticker("MSFT").info
for key, value in companyInfo.items():
    print(key, value)