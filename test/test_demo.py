

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSearch():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)

    def teardown_method(self):
        self.driver.quit()


    def test_search(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.CSS_SELECTOR, '#search-button[title=搜索]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.show-advanced-search').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input.search-query').send_keys('selenium')
        self.driver.find_element(By.CSS_SELECTOR, '.search-bar .search-cta').click()
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.topic-title')))
        assert 'selenium' in self.driver.find_element(By.CSS_SELECTOR, '.topic-title').text.lower()

