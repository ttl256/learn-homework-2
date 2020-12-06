"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    list_=[{"name": "a", "age": "20", "job": "ja"},
    {"name": "b", "age": "21", "job": "jb"},
    {"name": "c", "age": "22", "job": "jc"},
    {"name": "d", "age": "23", "job": "jd"}]

    with open("export.csv", "w", encoding="utf-8") as f:
        fields = ["name", "age", "job"]
        writer = csv.DictWriter(f, fields, delimiter = ";")
        writer.writeheader()
        for i in list_:
            writer.writerow(i)

if __name__ == "__main__":
    main()
