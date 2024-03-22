import requests
from bs4 import BeautifulSoup
import pandas as pd

current_page = 1

data = []

proceed = True

while(proceed):
    print('Currently Scraping page: '+str(current_page))
    url = 'https://books.toscrape.com/catalogue/page-'+str(current_page)+'.html'

    page = requests.get(url)

    soup = BeautifulSoup(page.text,'html.parser')

    if soup.title.text == '404 Not Found':
        proceed = False
    else:
        all_books = soup.find_all('li',class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

        for book in all_books:
            item = {}

            item['Title'] = book.find('img').attrs['alt']

            item['Link'] = book.find('a').attrs['href']

            item['Price'] = float(book.find('p', class_='price_color').text[2:])  # Convert price to float

            data.append(item)

    current_page += 1

# Convert the data list into a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
df.to_csv('books_data.csv', index=False)

print(df.head())




