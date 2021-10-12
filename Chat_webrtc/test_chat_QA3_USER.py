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

text = "тестовое сообщение для нагрузки чата !№;%:?*()_+"
host = "qa3.trueconf.net"
cid = "sym"
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

        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.maximize_window()                                   #webdriver.Firefox()
        self.driver.implicitly_wait(10) 		                # 10 сек в качестве максимального таймаута для выполнения методов
        self.base_url = "https://"+host+"/c/"+cid+"/"
        self.base_url_1 = "https://"+host+"/c/"+cid+"/conference"
        self.verificationErrors = []
        self.driver.get(self.base_url)
        driver = self.driver

        #кнопка меню "войти"
        sigin_in_buttn = self.driver.find_element_by_xpath('//*[@id="main-header__buttons-login"]')
        sigin_in_buttn.click()
        
        #кнопка переключения гость/пользователь (кнопка нужна для переключения но почему-то иногда не трубуется переключение хз почему)
        #enter_as_reg_user_buttn = self.driver.find_element_by_xpath('//*[@id="tc-button-136"]')
        #enter_as_reg_user_buttn.click()
        
        #поле для ввода логина
        login_fl = self.driver.find_element_by_xpath('//*[@id="authorization__input-trueconfId"]')
        login_fl.send_keys(user_name)
        
        #поле для ввода пароля
        password_fl = self.driver.find_element_by_xpath('//*[@id="authorization__input-password"]')
        password_fl.send_keys(password)
        
        #кнопка войти
        sigin_in_bt = self.driver.find_element_by_xpath('//*[@id="authorization__button-sing-in"]/span')
        sigin_in_bt.click()

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
	
    def test_stat(self):    # тест: отправка сообщений в чат конференции
        loops = 100
        time.sleep(1)

        #Открыть чат конференции
        open_chat = self.driver.find_element_by_xpath('//*[@id="conference-header__button-showChat"]')
        open_chat.click()
        
        for i in range(loops):
            #вставить и отправить сообщение
            chat_filed = self.driver.find_element_by_xpath('/html/body/section/div[1]/section/section[2]/section/section/label/div/textarea')
            chat_filed.send_keys('Сообщение #' + str(i) + ' '+ text)

            send_bttn = self.driver.find_element_by_xpath('/html/body/section/div[1]/section/section[2]/section/section/button/i')
            send_bttn.click()

            #time.sleep(0.5) #пауза между сообщениями
            
        time.sleep(5)
        
    def tearDown(self): # блок выполняется после запуска тестов
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        


if __name__ == "__main__":
    unittest.main()


