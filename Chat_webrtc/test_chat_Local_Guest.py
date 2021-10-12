from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import unittest, time
import logging
import time

#python -m pip install selenium

text = "test data"
host = "10.130.2.209"
cid = "chat"
user_name = "artem"
password = "11"

class Test3(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 2,      # 1:allow, 2:block 
            "profile.default_content_setting_values.media_stream_camera": 2    # 1:allow, 2:block 
            #"profile.default_content_setting_values.geolocation": 1,          # 1:allow, 2:block 
            #"profile.default_content_setting_values.notifications": 1         # 1:allow, 2:block 
          })

        self.driver = webdriver.Chrome(chrome_options=options)          #webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10) 		                # 10 сек в качестве максимального таймаута для выполнения методов
        self.base_url = "https://"+host+"/c/"+cid+"/"
        self.base_url_1 = "https://"+host+"/c/"+cid+"/conference"
        self.verificationErrors = []
        self.driver.get(self.base_url)
        driver = self.driver
        
        #принять имя гостя (лописать потом возможность задавать имя гостя)
        save_buttn_guest_name = self.driver.find_element_by_xpath('//*[@id="user-connection-no-authorized-button"]/span')
        save_buttn_guest_name.click()

        #####conect
        
        #подключиться webrtc
        self.driver.implicitly_wait(10)
        webrtc_bttn = self.driver.find_element_by_xpath('//*[@id="connection__webrtc-link"]')
        webrtc_bttn.click()
        
        #подключиться к конференции
        self.driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
        connect_bttn = self.driver.find_element_by_xpath('/html/body/section/div[1]/div/div/button')
        connect_bttn.click()

        return self
	
    def test_stat(self):
        loops = 100 #количество сообщений
        time.sleep(1)
        
        open_chat = self.driver.find_element_by_xpath('//*[@id="conference-header__button-showChat"]')
        open_chat.click()
        
        for i in range(loops):
            chat_filed = self.driver.find_element_by_xpath('/html/body/section/div[1]/section/section[2]/section/section/label/div/textarea')
            chat_filed.send_keys('Сообщение #' + str(i) + ' '+text)

            send_bttn = self.driver.find_element_by_xpath('/html/body/section/div[1]/section/section[2]/section/section/button/i')
            send_bttn.click()

            #time.sleep(0.5) #пауза между сообщениями
            
        time.sleep(5)
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        


if __name__ == "__main__":
    unittest.main()


