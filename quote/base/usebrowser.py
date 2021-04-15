import time

from selenium import webdriver
class UseBrowser:
    driver = None

    def __init__(self):
      self.driver = webdriver.Chrome()
      self.driver.maximize_window()
      self.driver.implicitly_wait(10)
      UseBrowser.driver = self.driver


    @classmethod
    def quit(cls):
        time.sleep(3)
        cls.driver.quit()


if __name__ == '__main__':
    ub = UseBrowser()
    time.sleep(3)
    UseBrowser.quit()

