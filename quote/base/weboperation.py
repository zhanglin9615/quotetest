import time

from quote.base.usebrowser import UseBrowser


class WebOperation:

    def __init__(self,driver):
        self.driver = driver

    # 打开网址
    def open_url(self,url):
        self.driver.get(url)

    # 通过name输入文本
    def input_text_name(self,name_locator,text):
        self.driver.find_element_by_name(name_locator).send_keys(text)

    # 通过xpath输入文本
    def input_xpath_name(self,xpath_locator,text):
        self.driver.find_element_by_xpath(xpath_locator).send_keys(text)

    # 通过xpath点击
    def click_xpath(self,xpath_locator):
        self.driver.find_element_by_xpath(xpath_locator).click()

    # 通过name清空
    def clear_name(self,name):
        self.driver.find_element_by_name(name).clear()

    # 获取文本信息
    def get_text_xpath(self,xpath_locator):
        return self.driver.find_element_by_xpath(xpath_locator).text

    # 通过name获取文本信息
    def get_text_name(self,name_locator):
        return self.driver.find_element_by_name(name_locator).text

    # 切换frame
    def change_frame(self,xpath_locator):
        self.driver.switch_to.default_content()
        element = self.driver.find_element_by_xpath(xpath_locator)
        self.driver.switch_to.frame(element)

    # 切窗体
    def change_window(self,title):
        for window in self.driver.window_handles:
            self.driver.switch_to.window(window)
            if self.driver.title == title:
                break

# if __name__ == '__main__':
#     ub = UseBrowser()
#     op = WebOperation(UseBrowser.driver)
#     op.open_url('http://localhost:8080/JavaPrj_6/')
#     op.input_text_name('username','admin')
#     op.input_text_name('password','123456')
#     ub.quit()
