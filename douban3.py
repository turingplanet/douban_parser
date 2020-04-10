from bs4 import BeautifulSoup
from selenium import webdriver

class DoubanParser:

    driver = webdriver.Chrome()

    def parse(self, page_url):
        self.driver.get(page_url)
        html = self.driver.page_source
        page_soup = BeautifulSoup(html, features='lxml') 
        book_titles = page_soup.find_all('div', {'class': 'info'})
        for title in book_titles:
            book_link = title.h2.a
            title = book_link.get_text().replace(" ", "").replace("\n", "")
            link = book_link["href"]
            book_description = self.get_book_description(link)
            print(f'{title}:{book_description}')

    def get_book_description(self, page_url):
        self.driver.get(page_url)
        html = self.driver.page_source
        page_soup = BeautifulSoup(html, features='lxml') 
        book_description = page_soup.find('div', {'class': 'intro'})
        text = book_description.p.get_text()
        return text

doubanParser = DoubanParser()
new_page = 'https://book.douban.com/tag/%E7%BC%96%E7%A8%8B'
doubanParser.parse(new_page)