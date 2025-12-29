import requests
from bs4 import BeautifulSoup
import csv

url = "http://quotes.toscrape.com/"
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # CSV ფაილის შექმნა
    with open('quotes.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ციტატა', 'ავტორი', 'თეგები'])

        # ყველა ციტატის პოვნა
        quotes = soup.find_all('div', class_='quote')

        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            tags = ', '.join(
                [tag.get_text() for tag in quote.find_all('a', class_='tag')]
            )

            # CSV ფაილში ჩაწერა
            writer.writerow([text, author, tags])

    print("მონაცემები შენახულია quotes.csv ფაილში!")
else:
    print("შეცდომა: გვერდის ჩამოტვირთვა ვერ მოხერხდა!")
