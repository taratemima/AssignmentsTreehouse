import datetime
import pytz
'''Create time zone differences based on location'''
moscow = datetime.timezone(datetime.timedelta(hours=+4))
pacific = datetime.timezone(datetime.timedelta(hours=-8)) 
india = datetime.timezone(datetime.timedelta(hours=+5, minutes=+30))

naive = datetime.datetime(2015, 10, 21, 4, 29)
pacific = datetime.timezone(datetime.timedelta(hours=-8))
hill_valley = datetime.datetime(2015, 10, 21, 4, 29, tzinfo=pacific)
euro = datetime.timezone(datetime.timedelta(hours=+1))
paris = hill_valley.astimezone(euro)

fmt = '%m-%d %H:%M %Z%z'
starter = datetime.datetime(2015, 10, 21, 4, 29)
pacific = pytz.timezone('US/Pacific')
local = pacific.localize(starter)
pytz_string = local.strftime(fmt)



