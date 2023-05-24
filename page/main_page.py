

from selenium import webdriver
from selenium.webdriver.common.by import By

from page.search_page import SearchPage


class MainPage:

    def __init__(self):
        self.driver = webdriver.Chrome()


    def get_topic_list(self):
        ...

    def to_search_advance(self) -> SearchPage:
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.CSS_SELECTOR, '#search-button[title=搜索]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.show-advanced-search').click()
        return SearchPage(self.driver)

    def close(self):
        self.driver.quit()

if __name__ == '__main__':
    main = MainPage()
    main.to_search_advance("用户")