import datetime as date


def diff_date(day1, month1, year1, day2, month2, year2):
    return date.date(year2, month2, day2) - date.date(year1, month1, day1)


birth_date, birth_month, birth_year = input("Enter your birthday in dd/mm/yyyy format separated by '/' : ").split('/')

cd = date.datetime.now()
diff_year = diff_date(int(birth_date), int(birth_month), int(birth_year), cd.day, cd.month, cd.year).days
year, days = int(diff_year / 365), int(diff_year % 365)
print("You are ", year, " years and ", days, " days old")
