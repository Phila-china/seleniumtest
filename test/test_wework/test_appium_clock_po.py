
import pytest

from page.androidwork.clock_page import ClockPage


class TestClock:

    def setup(self):
        self.clock = ClockPage()

    def teardown(self):
        self.clock.close()

    @pytest.mark.parametrize('city',[
        'beijing',
        'tokyo',
        'hongkong',
    ])
    def test_city_clock(self, city):
        self.clock.check_clock_via_city(city)

    def test_stopwatch(self):
        self.clock.stopwatch()



