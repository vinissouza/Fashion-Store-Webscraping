import time
import numpy    as np
import pandas   as pd
import requests

from bs4                          import BeautifulSoup
from datetime                     import datetime
from random_user_agent.params     import SoftwareName, OperatingSystem
from random_user_agent.user_agent import UserAgent


class DataCollect:

    scrapy_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __init__(self, url: str):
        self.url = url
        self.scrapy_datetime = datetime.now().strftime('%Y-%n-%d %H:%M:%S')

    def api_request(self):
        # get random user agent string
        software_names = [SoftwareName.CHROME.value]

        operating_systems = [OperatingSystem.WINDOWS.value]

        user_agent_rotator = UserAgent(software_names=software_names,
                                       operating_systems=operating_systems,
                                       limit=100)

        # get list of user agents
        user_agent = user_agent_rotator.get_random_user_agent()

        headers = {'User-Agent': user_agent}

        page = requests.get(url=self.url, headers=headers)

        return page

    def beautifulsoup_object(self, page):
        # built beautiful soup object
        soup = BeautifulSoup(page.text, 'html.parser')

        return soup

    def number_of_products(self, soup: BeautifulSoup):
        # html from pagination
        total_items = soup.find('h2', class_='load-more-heading').get('data-total')

        page_number = np.ceil(int(total_items)/36)

        return page_number

    def showroom_products(self, page_number):
        # assemble url from all products
        page_size = '?page-size=' + str(int(page_number * 36))

        url = self.url + page_size

        self.url = url

        # API request and beautiful soup object
        page = self.api_request()

        soup = self.beautifulsoup_object(page)

        # html from products list
        products = soup.find('ul', class_='products-listing small')

        products_list = products.find_all('article', class_='hm-product-item')

        # product id
        product_id = [p.get('data-articlecode') for p in products_list]

        # product category
        product_category = [p.get('data-category') for p in products_list]

        # product name
        product_name = [p.find('a', class_='link').get_text() for p in products_list]

        # product price
        product_price = [p.find('span', class_='price regular').get_text() for p in products_list]

        # product href
        url_site = 'https://www2.hm.com'
        product_href = [url_site + p.find('a', class_='link').get('href') for p in products_list]

        # assemble showroom products dataframe
        data_showroom = pd.DataFrame(
            data=[product_id, product_category, product_name, product_price, product_href]
        ).T
        data_showroom.columns = ['product_id', 'product_category', 'product_name',
                                 'product_price', 'product_link']

        # record scrapy time
        data_showroom['scrapy_datetime'] = self.scrapy_datetime

        data_showroom.to_csv(f'../Datasets/data_showroom', index=False)

        return data_showroom

    def product_color(self, data_showroom: pd.DataFrame):
        # empty color dataframe
        data_color = pd.DataFrame()

        # iterable to get all color options from each showroom product
        for i in range(len(data_showroom)):
            # get all url from showroom products
            self.url = data_showroom['product_link'][i]

            # API request and beautiful soup object
            page = self.api_request()

            soup = self.beautifulsoup_object(page)

            # html from color options
            color_list = soup.find_all('a', class_='filter-option')

            # color name
            color_name = [p.get('data-color') for p in color_list]

            # product id
            product_id = [p.get('data-articlecode') for p in color_list]

            # product href
            url_site = 'https://www2.hm.com'
            product_href = [url_site + p.get('href') for p in color_list]

            # assemble color dataframe
            df_color = pd.DataFrame([product_id, color_name, product_href]).T
            df_color.columns = ['product_id', 'color_name', 'product_link']

            # join all colors dataframes
            data_color = pd.concat([data_color, df_color], axis=0, ignore_index=True)

        # record scrapy time
        data_color['scapy_datetime'] = self.scrapy_datetime

        data_color.to_csv(f'../Datasets/data_color', index=False)

        return data_color

    def product_attributes(self, data_color: pd.DataFrame):
        # empty attributes options list
        attributes = []

        # iterable to get all possible attributes from products
        for i in range(len(data_color)):
            # get urls from all products
            self.url = data_color['product_link'][i]

            # API request and beautiful soup object
            page = self.api_request()

            soup = self.beautifulsoup_object(page)

            # html from products description
            attributes_list = soup.find_all( 'div', class_='pdp-description-list-item' )

            attributes = attributes + [att.find( 'dt' ).get_text() for att in attributes_list]

        # empty attributes dataframe with all possible options
        attributes_columns = list( set(attributes) )

        data_attributes = pd.DataFrame( columns= attributes_columns )

        # iterable to get attributes from all products
        for j in range(len(data_color)):
            # get urls from all products
            self.url = data_color['product_link'][j]

            # API request and beautiful soup object
            page = self.api_request()

            soup = self.beautifulsoup_object(page)

            # html from products description
            attributes_list = soup.find_all( 'div', class_='pdp-description-list-item' )

            # attributes options
            attributes = [att.find( 'dt' ).get_text() for att in attributes_list]

            # attributes values
            attributes_values = [att.find( 'dd' ).get_text() for att in attributes_list]

            # assemble attributes dataframe
            df_attributes = pd.DataFrame( attributes_values ).T

            df_attributes.columns = attributes

            # product price
            product_price = soup.find('div', class_='primary-row').get_text()

            # join product price with product attribute data
            attribute_price = pd.DataFrame({'Price': [product_price]})

            df_attributes = pd.concat([df_attributes, attribute_price], axis=1)

            # join all attributes dataframes
            data_attributes = pd.concat([data_attributes, df_attributes], axis=0, ignore_index=True)

        # record scrapy time
        data_attributes['scrapy_datetime'] = self.scrapy_datetime

        data_attributes.to_csv(f'../Datasets/data_attributes', index=False)

        return data_attributes

    def join_data(self, data_showroom, data_color, data_attributes):

        data_details = pd.concat([data_color, data_attributes], axis=1)

        # data_details['model_code'] = data_details['product_id'].apply(lambda x: x[:-3])
        #
        # data_showroom['model_code'] = data_showroom['product_id'].apply(lambda x: x[:-3])

        data_raw = data_details.merge(data_showroom[['product_id', 'product_category', 'product_name']],
                                      how='left', on='product_id')

        data_raw['scrapy_datetime'] = self.scrapy_datetime

        data_raw.to_csv(f'../Datasets/data_raw_{datetime.now().strftime( "%Y-%m-%d-%H-%M-%S" )}', index=False)

        return data_raw
