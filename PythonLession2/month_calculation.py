from datetime import datetime
from datetime import date
#from dateutil import relativedelta
birthdate = input("Please input your day of birth(dd/mm/yyyy): ")
start_date = datetime.strptime(birthdate,'%d/%m/%Y')
end_date = datetime.today()
difference = (abs(((start_date.year * 12) + start_date.month) - ((end_date.year * 12) + start_date.month)))
print("You are {} months old!".format(difference))


