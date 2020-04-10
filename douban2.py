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
            print(f'{title}:{link}')

doubanParser = DoubanParser()
new_page = 'https://book.douban.com/tag/%E7%BC%96%E7%A8%8B'
doubanParser.parse(new_page)