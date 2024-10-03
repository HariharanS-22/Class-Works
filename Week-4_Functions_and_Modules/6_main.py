from datetime import datetime

date_format = "%d/%m/%Y"
date1 = input("Enter the first date (DD/MM/YYYY): ")
date2 = input("Enter the second date (DD/MM/YYYY): ")
date1 = datetime.strptime(date1, date_format)
date2 = datetime.strptime(date2, date_format)
no_of_days = date2 - date1
print(f"Number of days between {date1.strftime(date_format)} and {date2.strftime(date_format)} : {no_of_days.days} days")


