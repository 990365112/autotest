import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestUi():
    def setup(self):
        chrome_option = Options()
        chrome_option.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize(("a","b"),[("王者荣耀","王者荣耀_百度搜索"),("英雄联盟","英雄联盟_百度搜索")])
    def test_baidu(self,a,b):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys(a)
        time.sleep(3)
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        assert b==self.driver.title
if __name__ == '__main__':
    pytest.main()