import PixelClass
import WebAccess
import sys
import datetime
from time import gmtime, strftime
import pytz

gmt = pytz.timezone('GMT')
eastern = pytz.timezone('US/Eastern')

WebAccess.PostMessage(str(strftime('%H:%M:%S %m-%d-%Y', gmtime().astimezone(eastern))))
