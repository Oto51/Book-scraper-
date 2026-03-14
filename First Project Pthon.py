import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("span", class_="titleline")

for title in titles:
    print(title.text)