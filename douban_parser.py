import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from urllib.request import urlopen

class DoubanParser:

    driver = webdriver.Chrome()
    book_dict = {}

    def parse(self, page_url):
        self.driver.get(page_url)
        html = self.driver.page_source
        page_soup = BeautifulSoup(html, features='lxml') 
        book_titles = page_soup.find_all('div', {'class': 'info'})
        for title in book_titles:
            book_link = title.h2.a
            title = book_link.get_text().replace(" ", "").replace("\n", "")
            link = book_link["href"]
            print(f'{title}:{link}')
            book_description = self.get_book_description(link)
            self.book_dict[title] = book_description 
        self.write_to_csv(f'douban/book_info_{page_url[-3:]}.csv')

    def get_book_description(self, page_url):
        self.driver.get(page_url)
        html = self.driver.page_source
        page_soup = BeautifulSoup(html, features='lxml') 
        book_description = page_soup.find('div', {'class': 'intro'})
        text = book_description.p.get_text()
        return text

    def write_to_csv(self, file_name):
        with open(file_name, 'w', newline='') as file:
            write = csv.writer(file)
            write.writerow(['book_title', 'description'])
            for title, description in self.book_dict.items():
                write.writerow([title, description])

doubanParser = DoubanParser()
new_page = 'https://book.douban.com/tag/%E7%BC%96%E7%A8%8B'
doubanParser.test(new_page)
# for i in range(5, 50):
#     new_page = 'https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=0' + str(i * 20)
#     doubanParser.parse(new_page)

doubanParser.write_to_csv('douban/all_books.csv')