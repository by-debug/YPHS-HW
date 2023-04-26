from YPHS.mydatabase import get_current_time
import datetime
import os

def countdown(date):
      current_time = get_current_time()
      current_time = datetime.datetime.strptime(current_time, '%Y/%m/%d')
      date = datetime.datetime.strptime(date, '%Y/%m/%d')
      return str((date - current_time).days)

