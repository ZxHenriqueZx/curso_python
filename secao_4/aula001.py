from datetime import datetime

data = datetime(2005, 5, 6, 18, 59, 59)
data_br = datetime.strptime('06-05-2005', '%d-%m-%Y')
data_now = datetime.now()
print(data_br)
print(data_now)
