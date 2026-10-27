
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website to scrape - Books to Scrape (public site allow
ed for scraping)
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
__________________________________________________________
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample sales data - creating dummy data
data = {
    'Month': ['Jan','Feb','Mar','Apr','May','Jun'],
    'Sales': [12000, 15000, 13000, 18000, 20000, 22000],
    'Profit': [3000, 4000, 3200, 5000, 6000, 7000],
    'Category': ['A','B','A','C','B','A']
}
df = pd.DataFrame(data)

# Set style
sns.set_style("whitegrid")

# 1. Bar Chart
plt.figure(figsize=(8,5))
sns.barplot(x='Month', y='Sales', data=df, palette='viridis')
plt.title('Monthly Sales - CodeAlpha Task 3', fontsize=14)
plt.savefig('1_monthly_sales.png')
plt.show()

# 2. Line Chart with Profit
plt.figure(figsize=(8,5))
plt.plot(df['Month'], df['Sales'], marker='o', label='Sales')
plt.plot(df['Month'], df['Profit'], marker='s', label='Profit')
plt.title('Sales vs Profit Trend')
plt.legend()
plt.savefig('2_sales_profit_trend.png')
plt.show()

# 3. Pie Chart
plt.figure(figsize=(6,6))
df.groupby('Category')['Sales'].sum().plot.pie(autopct='%1.1f%%')
plt.title('Sales by Category')
plt.savefig('3_category_pie.png')
plt.show()

print("All 3 dashboards created - Ready for submission!")
____________________________________________________________
import pandas as pd
from textblob import TextBlob

# Sample Amazon reviews data
reviews = [
    "I love this product, it is amazing!",
    "Worst purchase ever, totally waste of money.",
    "Product is okay, not bad but not great.",
    "Excellent quality and fast delivery!",
    "Very disappointing, broke in 2 days."
]

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0: return 'Positive'
    elif polarity < 0: return 'Negative'
    else: return 'Neutral'

df = pd.DataFrame(reviews, columns=['Review'])
df['Sentiment'] = df['Review'].apply(get_sentiment)
df['Polarity'] = df['Review'].apply(lambda x: TextBlob(x).sentiment.polarity)

df.to_csv('CodeAlpha_Sentiment_Analysis.csv', index=False)
print(df)