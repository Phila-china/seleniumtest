from datetime import datetime

import pytest

from page.wework.main_page import MainPage


class TestContact:

    def setup_class(self):
        self.main = MainPage()
        self.contact = self.main.to_contact()

    def teardown(self):
        self.contact.refresh()

    @pytest.mark.parametrize('name, account, mobile', [
        ['seveniruby1', 'seveniruby1', ''],
        ['seveniruby2', 'seveniruby2', ''],
    ])
    def test_add_member(self, name, account, mobile):
        r = str(datetime.now().timestamp())[0:10]
        name = name + r
        account = account + r
        mobile = '1' + r
        assert account in self.contact.add_member(name=name, account=account,mobile=mobile).search(account).get_first_search_result()['account']





