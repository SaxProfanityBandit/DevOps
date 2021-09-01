from datetime import datetime
now = datetime.now()

#Lession Taught Way
print("{}/{}/{} {}:{}:{}".format(now.day, now.month, now.year, now.hour, now.minute, now.second))

#Industry way:
print(now.strftime('%d/%m/%Y %H:%M:%S'))
