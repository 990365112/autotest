import time
import pytest
from selenium import webdriver
class TestUI():
    def test_a(self):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com")
        time.sleep(10)
        driver.quit()
if __name__ == '__main__':
    pytest.main()
