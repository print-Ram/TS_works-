from datetime import datetime as dt
import pandas as pd

stockdata = input('\n\t\t\t\t****Select any Company Name****\n')

# Prompt the user to enter the first date in the format YYYY-MM-DD HH:MM:SS
date_str1 = input("Enter the start date in the format YYYY-MM-DD: ")
date_str2 = input("Enter the end date in the format YYYY-MM-DD: ")

date_obj1 = (dt.strptime(date_str1, '%Y-%m-%d'))
date_obj2 = (dt.strptime(date_str2, '%Y-%m-%d'))

# Get the timestamps from the datetime objects
tstamp1 = date_obj1.timestamp()
tstamp2 = date_obj2.timestamp()

tstr1 = int(tstamp1)
tstr2 = int(tstamp2)

ts1 = str(tstr1)
ts2 = str(tstr2)

interval = input('Enter the interval from 1d to 1mo :\n\t daywise = 1d\n\t weekwise = 1wk\n\t monthwise = 1mo\n')

#interval = '1d' , '1wk' ,'1mo'
events = input('Want to Print a Historical data or Dividened ? \n')

#events = 'history','split'
Stockurl = 'https://finance.yahoo.com/quote/'+stockdata+'/history?p='+stockdata+''

print('\n\nTo view it Click here :')
print(Stockurl)

Stock_downurl = 'https://query1.finance.yahoo.com/v7/finance/download/' + stockdata + '?period1='+ ts1 + '&period2=' + ts2 + '&interval=' + interval + '&events'+ events
company_data = pd.read_csv(Stock_downurl)
print('\n\nThe Download link is here :')
print(Stock_downurl)
#////Hence you Can change the "date interval" at line no.4 and 5 in code and try
with open('output.ini', 'w') as f:
    f.write(f"Company Name: {stockdata}\n")
    f.write(f"Stock Data:\n{company_data}\n")
    f.write(f"Download Link: {Stock_downurl}\n")
    df = pd.DataFrame(company_data, columns=['Date', 'Open', 'High'])
    print(df)





