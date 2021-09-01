from datetime import datetime
now = datetime.now()

print("{}/{}/{} {}:{}:{}".format(now.day, now.month, now.year, now.hour, now.minute, now.second))
