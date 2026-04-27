from datetime import date, time, datetime
today=date.today()
now=datetime.now()
print("todays date is", today)
print("\ntodays time is", now)
print("\ndatecomponents", today.day,today.year,today.month)