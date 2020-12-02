"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, timedelta, datetime

def print_days():
    delta1 = timedelta(days=1)
    delta30 = timedelta(days=30)
    today = date.today()
    date1 = today - delta1
    date2 = today - delta30
    print(f"Today is {today}")
    print(f"Yesterday it was {date1}")
    print(f"30 days ago it was {date2}")

def str_2_datetime(date_string):
    datetime_obj = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return datetime_obj

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
