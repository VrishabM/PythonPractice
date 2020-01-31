import datetime as d


def diff_date(day1, month1, year1, day2, month2, year2):
    return d.date(year2, month2, day2) - d.date(year1, month1, day1)


d1, m1, y1 = input("Enter date 1 separated by '/' in dd/mm/yyyy format : ").split('/')
d2, m2, y2 = input("Enter date 2 separated by '/' in dd/mm/yyyy format : ").split('/')

print("Difference between two dates -> ", diff_date(int(d1), int(m1), int(y1), int(d2), int(m2), int(y2)).days)
