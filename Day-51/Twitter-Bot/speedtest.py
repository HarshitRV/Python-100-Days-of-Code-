from selenium import webdriver
import time

class Speedtest:
    def __init__(self,path):
        '''Takes one required parameter chrome driver path: type(str)'''
        self.path = path
        self.driver = webdriver.Chrome(executable_path = self.path)
        self.driver.get("https://www.speedtest.net/")
        self.results = self.test_speed()
    
    def test_speed(self):
        self.driver.find_element_by_class_name("start-text").click()
        time.sleep(50)
        self.result_list = self.driver.find_elements_by_class_name("result-data")
        self.result_data = [data.text for data in self.result_list]
        self.driver.quit()
        return [self.result_data[i] for i in range(3,6)]