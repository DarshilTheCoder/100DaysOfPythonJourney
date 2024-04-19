import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
date2 = now.date()

print(year)
print(month)
print(date2)
print(now)

setdate = dt.datetime(year=2024,month=12,day=15)
print(setdate)