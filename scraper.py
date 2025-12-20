import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('article', class_='product_pod')

book_list = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    book_list.append({"სათაური": title, "ფასი": price})

with open('წიგნები.csv', 'w', newline = '', encoding = 'utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["სათაური", "ფასი"])
    writer.writeheader()
    writer.writerows(book_list)

print("მონაცემები შენახულია წიგნები.csv ფაილში!")
print(f"სულ {len(book_list)} წიგნი მოიძებნა")