import csv
import json
from files import JSON_FILE_PATH_HW
from files import CSV_FILE_PATH

new_books = []

with open(CSV_FILE_PATH, 'r') as k:
    books_list = csv.DictReader(k)

    for book_unit in books_list:
        new_books_title = book_unit['Title']
        new_books_author = book_unit['Author']
        new_books_pages = int(book_unit['Pages'])
        new_books_genre = book_unit['Genre']

        new_books.append({
            'title': new_books_title,
            'author': new_books_author,
            'pages': new_books_pages,
            'genre': new_books_genre
        })

with open(JSON_FILE_PATH_HW, 'r') as s:
    users_list = json.load(s)

    new_users = []
    b = 0

    for users_unit in users_list:
        new_users_name = users_unit['name']
        new_users_gender = users_unit['gender']
        new_users_address = users_unit['address']
        new_users_age = int(users_unit['age'])

        books = []
        i = 0

        while i*len(users_list)+b < len(new_books):
            books.append(new_books[i*len(users_list)+b])
            i += 1

        new_users.append({
            'name': new_users_name,
            'gender': new_users_gender,
            'address': new_users_address,
            'age': new_users_age,
            'books': books
        })

        b += 1

with open('result.json', 'w') as file_new_json:
    json.dump(new_users, file_new_json, indent=4)
