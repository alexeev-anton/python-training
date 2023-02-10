from datetime import date
from math import sin


def print_value(value):
    print(value)


print_value("Hello")


date_today = date.today()
date_future = date(2023, 2, 28)


def count_dates(x, y):
    res = x - y
    return res


print_value(count_dates(date_future, date_today))


print_value(sin(456586.1451))
