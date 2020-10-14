import json
import csv

"""
Домашнее задание PyTest и работа с тестовыми данными Цель: Узнать особенности PyTest, научиться работать с 
различными типами файлов, написать тесты для pytest и собственный контекстный менеджер для файлов. 

Работа с тестовыми данными

1. Скачать приложенные к занятию файлы форматов users.json и books.csv 
2. Написать с помощью контекстных менеджеров скрипт, которых из двух файлов будет читать данные и на их 
основании создаст json файл со структурой из файла example.json 
3. Каждому пользователю нужно добавить одну книгу из списка. Если количество книг меньше количества 
пользователей, то остальным добавить пустой массив. Если книг больше чем пользователей, то просто прекратить 
раздавать книги. 
"""

with open('books-39204-271043.csv') as books:
    book_list = []
    csv_reader = csv.DictReader(books)
    for row in csv_reader:
        book_list.append(row)

with open('books.json', 'w') as books_json:
    json.dump(book_list, books_json, sort_keys=False, indent=2)

with open('books.json') as books_dictionary_json:
    books_data = json.load(books_dictionary_json)
    result_books = []
    results_users_and_books = []
    for book in books_data:
        result_books = []
        result_books.append({'Title': book["Title"], 'Author': book["Author"], 'Height': book["Height"]})
        with open('users-39204-8e2f95.json', 'r') as user_json:
            users_data = json.load(user_json)
            results_data = []
            for item in users_data:
                results_users_and_books.append(
                    {'name': item["name"], 'gender': item["gender"], 'address': item["address"], 'books': result_books})

    with open('users_and_books.json', 'w') as users_and_books:
        json.dump(results_users_and_books, users_and_books, sort_keys=False, indent=2)
