import time

from page.main_page import MainPage


class TestSearchPO:

    def setup_class(self):
        self.main = MainPage()

    def setup(self):
        self.search = self.main.to_search_advance()

    def teardown_class(self):
        self.main.close()

    def test_search(self):
        assert 'selenium' in str(self.search.search('selenium').get_search_result1()[0]).lower()

    def test_search_type1(self):
        self.search.select_search_type("话题/帖子")
        assert "话题/帖子" == self.search.get_current_search_type()
        assert 'selenium' in str(self.search.search('selenium').get_search_result1()[0]).lower()

    def test_search_type2(self):
        self.search.select_search_type("类别/标签")
        assert "类别/标签" == self.search.get_current_search_type()
        assert 'python' in str(self.search.search('python').get_search_result2()[0]).lower()

    def test_search_type3(self):
        self.search.select_search_type("用户")
        assert "用户" == self.search.get_current_search_type()
        assert 'python' in str(self.search.search('python').get_search_result3()[0]).lower()

    def test_set_poster_and_post_time(self):
        self.search.search_poster("hogwarts")
        self.search.select_post_time("晚于", "002023-01-01")
        time.sleep(3)
        assert "hogwarts" in self.search.click_search_and_check_heading()
        assert "after:2023-01-01" in self.search.click_search_and_check_heading()

    # login required before testing
    def test_grouped_control_field(self):
        self.search.check_grouped_control_field("matching-title-only")
        assert "in:title" in self.search.click_search_and_check_heading()







