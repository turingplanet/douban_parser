import csv
from bs4 import BeautifulSoup
from selenium import webdriver

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
doubanParser.parse(new_page)

doubanParser.write_to_csv('books.csv')