# from datetime import datetime
# today = datetime.today()
# year  = datetime(today.year, today.month, 1)

# print(year[0:6])


from datetime import datetime

year , month = str(datetime.today().year) , str(datetime.today().month)

if len(month) == 1:
    month = "0" + month


time_now = year + "-" + month if len(month) == 1 else month

print(time_now)