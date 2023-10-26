import calendar
import time

current_GMT = time.gmtime()

time_stamp = calendar.timegm(current_GMT)
print("current timestamp",time_stamp)
