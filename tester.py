import datetime

t1 = datetime.datetime.now()
t2 = datetime.datetime(t1.year, t1.month, t1.day, t1.hour, t1.minute, t1.second+5, t1.microsecond)
t3 = t2-t1

while t3 !=0 and 0<=t3.days:
	t1 = datetime.datetime.now()
	t3 = t2-t1
print('finished')
print(t2-t1)
