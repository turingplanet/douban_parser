from selenium import webdriver

class DoubanParser:

    driver = webdriver.Chrome()

    def test(self, page_url):
        self.driver.get(page_url)

doubanParser = DoubanParser()
new_page = 'https://book.douban.com/tag/%E7%BC%96%E7%A8%8B'
doubanParser.test(new_page)