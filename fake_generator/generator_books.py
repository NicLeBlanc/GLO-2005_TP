from fake_generator.data import books_raw
import random
from faker import Faker

# url used : https://raw.githubusercontent.com/bvaughn/infinite-list-reflow-examples/master/books.json

# List of titles
title = []
for item in books_raw:
    title.append(item.get('title'))

# List of ISBN
isbn = []
for item in books_raw:
        random_key = random.randint(1, 10000)
        isbn.append(item.get('isbn', random_key))

# List of Authors
authors = []
for item in books_raw:
    all_authors = item.get('authors')
    first_author = all_authors[0]
    authors.append(first_author)

# List of year of publication (si pas d'années de publication, on met random entre 1995 et 2021)
year_publication = []
for item in books_raw:
    try:
        date_publication = item.get('publishedDate').get('$date')
        year_publication.append(date_publication[:4])
    except:
        random_year = random.randint(1995, 2021)
        year_publication.append(random_year)

# List of short description (si pas de courte description, on génère du faux texte)
short_description = []
fake_data = Faker()
random_text = fake_data.text()
random_text[:499]
for item in books_raw:
    try:
        desc = item.get('shortDescription')
        short_desc = desc[:499]
        short_description.append(short_desc)
    except:
        random_text = fake_data.text()
        short_fake_description = random_text[:499]
        short_description.append(short_fake_description.replace('\n', ' '))

# List of books
books = []
book_list = [isbn, title, authors, year_publication, short_description]
for x in range(len(isbn)):
    books.append([item[x] for item in book_list])
print(books)