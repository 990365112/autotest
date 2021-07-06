import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestUI():
    def setup(self):
        chrome_option = Options()
        chrome_option.add_argument("--headless")
        self.driver=webdriver.Chrome(options=chrome_option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    def test_a(self):
        self.driver.get("https://www.baidu.com")
        time.sleep(3)
        assert self.driver.title=="百度一下，你就知道"
if __name__ == '__main__':
    pytest.main()
