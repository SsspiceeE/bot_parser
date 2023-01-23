import requests
from bs4 import BeautifulSoup
import re
import csv


def parse_prices():
    url = 'https://a-progress.ru/catalog/stroymaterialy/sukhie_smesi/shtukaturki/?set_filter=y&yclid=511558728836221632'


    products_data = []


    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    products = soup.find_all('div', class_='inner')

    for product in products:
        product_name = product.find('div', class_='name').find('a')
        product_title = product.getText().strip()
        product_url = 'https://a-progress.ru' + product_name.get('href').strip()
        product_price = product.find('div', class_='soloprice').find('span').getText().strip()
        products_data.append((product_title, product_url, product_price))



    with open('shtukaturka.csv', 'w', encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow((
            'Наименоание товара',
            'Цена',
            'URL'
        ))
        for product in products_data:
            writer.writerow((
                product[0],
                product[2],
                product[1]
            ))


