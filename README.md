
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website to scrape - Books to Scrape (public site allowed for scraping)
url = "http://books.toscrape.com/catalogue/page-1.html"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

books = []
for book in soup.find_all('article', class_='product_pod'):
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    rating = book.p['class'][1]
    books.append([title, price, rating])

# Create custom dataset
df = pd.DataFrame(books, columns=['Title', 'Price', 'Rating'])
df.to_csv('CodeAlpha_WebScraped_Dataset.csv', index=False)
print("Dataset Created Successfully!")
print(df.head())