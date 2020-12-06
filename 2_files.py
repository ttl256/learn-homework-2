"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print(type(content))
        print(f"The length of the string is: {len(content)}")

    with open('referat.txt', 'r', encoding='utf-8') as f:
        wc = 0
        for line in f:
            #print(f"NEW LINE: {line}")
            wc += len(line.split())
        print(f"The number of words in the file is: {wc}")

    with open('referat.txt', 'r', encoding='utf-8') as file_from:
        with open('referat2.txt', 'w', encoding='utf-8') as file_to:
            for line in file_from:
                line = line.replace(".", "!")
                #print(line)
                file_to.write(line)
       
if __name__ == "__main__":
    main()