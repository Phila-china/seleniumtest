import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class SearchPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def search(self, keyword) -> 'SearchPage':
        query = self.driver.find_element(By.CSS_SELECTOR, 'input.search-query')
        query.clear()
        query.send_keys(keyword)
        self.driver.find_element(By.CSS_SELECTOR, '.search-bar .search-cta').click()
        return self

    def get_search_result1(self):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.topic-title')))
        title_list = []
        for element in self.driver.find_elements(By.CSS_SELECTOR, '.topic-title'):
            title_list.append(element.text)
        return title_list

    def get_search_result2(self):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.category-name')))
        title_list = []
        for element in self.driver.find_elements(By.CSS_SELECTOR, '.category-name'):
            title_list.append(element.text)
        return title_list

    def get_search_result3(self):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.username')))
        title_list = []
        for element in self.driver.find_elements(By.CSS_SELECTOR, '.username'):
            title_list.append(element.text)
        return title_list

    def select_search_type(self, title):
        time.sleep(3)
        ac = ActionChains(self.driver)
        # 鼠标移动到<下拉>按钮上
        ac.move_to_element(self.driver.find_element(By.CSS_SELECTOR, '#search-type [href="#caret-down"]')).perform()
        ac.click(self.driver.find_element(By.CSS_SELECTOR, '#search-type [href="#caret-down"]')).perform()
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.select-kit-collection')))
        command = 'self.driver.find_element(By.CSS_SELECTOR, \'.select-kit-collection > li[title="{}"]\')'.format(title)
        eval(command).click()

    def get_current_search_type(self):
        type = self.driver.find_element(By.CSS_SELECTOR, '#search-type summary').get_attribute("data-name")
        return type

    def search_poster(self, keyword):
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '#search-posted-by').click()
        time.sleep(1)
        query = self.driver.find_element(By.CSS_SELECTOR,'div #search-posted-by-filter input')
        query.send_keys(keyword)
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.select-kit-collection')))
        self.driver.find_element(By.CSS_SELECTOR, '[data-index="0"]').click()

    def click_search_and_check_heading(self):
        self.driver.find_element(By.CSS_SELECTOR,'.search-bar span.d-button-label').click()
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.result-count')))
        result = self.driver.find_element(By.CSS_SELECTOR,'.search-page-heading span.term').text
        return result

    def select_post_time(self, title, date):
        time.sleep(3)
        ac = ActionChains(self.driver)
        # 鼠标移动到<下拉>按钮上
        ac.move_to_element(self.driver.find_element(By.CSS_SELECTOR, '#postTime [href="#caret-down"]')).perform()
        ac.click(self.driver.find_element(By.CSS_SELECTOR, '#postTime [href="#caret-down"]')).perform()
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.select-kit-collection')))
        command = 'self.driver.find_element(By.CSS_SELECTOR, \'.select-kit-collection > li[title="{}"]\')'.format(title)
        eval(command).click()
        self.driver.find_element(By.CSS_SELECTOR, 'input#search-post-date').send_keys(date)

    def check_grouped_control_field(self, field):
        time.sleep(3)
        command = 'self.driver.find_element(By.CSS_SELECTOR, \'.grouped-control-field  input#{}\')'.format(field)
        eval(command).click()

    def close(self):
        self.driver.quit()



