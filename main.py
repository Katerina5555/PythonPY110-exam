# encoding = "utf-8"
import random
from faker import Faker
import json
from conf import MODEL
"""импортируем переменную из конф"""
from faker.providers.isbn import isbn

Faker.seed(random)
fake = Faker()

def title() -> str:
    """определние автора из файла тхт"""
    with open("books.txt") as file:
        return random.choice(file.readlines())

def year() -> int:
    """подбор года из заданного диапозона"""
    return random.randint(1100, 2021)

def pages() -> int:
    """определние кол-во страниц из диапозона"""
    return random.randint(1, 1500)

def isbn13(separator: str = "-"):
    """рандом для isbn"""
    for _ in range(5):
        return fake.isbn13()

def rating() -> float:
    """рандом для рейтинга от 0 до 5"""
    return random.randrange(0, 500) / 100

def price() -> float:
    """рандом цены ограничение в 9 999,99"""
    return random.randrange(0, 1000000) / 100

def author() -> str:
    """рандом для подбора автора из списка"""
    authors = ("Е.Ю. Хрусталева", "Дон Тапскотт", "В.В. Ткачук")
    return random.choice(authors)

def main():
    dict_all = []
    for pk in range(1, 101):

        dict_1 = {"MODEL": MODEL,
            "pk": pk,
            "fields": {
                  "title": title(),
                  "year": year(),
                  "pages": pages(),
                  "isbn": isbn13(),
                  "rating": rating(),
                  "price": price(),
                  "author": author()
                  }
            }
        dict_all.append(dict_1)
        with open("package.json", "w") as f:
            json.dump(dict_all, f, indent=4, ensure_ascii=False)
        pk += 1
        continue


if __name__ == '__main__':
    # print(f'"title": {title()}')    # check title
    # print(f'"year": {year()}')    # check year
    # print(f'"pages": {pages()}')    # check page
    # print(f'"isbn": {isbn13()}')    # check isbn
    # print(f'"rating": {rating()}')  # check rating
    # print(f'"price": {price()}')  # check price
    # print(f'"author": {author()}')  # check author
    main()

