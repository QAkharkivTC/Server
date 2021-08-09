from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import unittest, time
import logging
import time


t = str(time.time())
logging.basicConfig(filename="test_log_cheak_link "+t+".log", format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO)
logging.info(" Cheak link")
start = time.monotonic()
'''
"/admin/general/info/",
"/admin/general/config/",
"/admin/network/address/",
"/admin/network/smtp/",
"/admin/network/federation/",
"/admin/gateways/sip/",
"/admin/gateways/h323/",
"/admin/gateways/transcoding/",
"/admin/web/settings/",
"/admin/web/security/",
"/admin/web/https/",
"/admin/users/list/",
"/admin/group/list/",
"/admin/users/aliases/",
"/admin/users/storage/",
"/admin/conferences/list/",
"/admin/templates/list/",
"/admin/conferences/streaming/",
"/admin/api/clients/#/",
"/admin/logs/events/",
"/admin/logs/calls/",
"/admin/logs/chats/",
"/admin/logs/settings/",
"/admin/logs/recordings/",
"/admin/connections/list/",
"/admin/storage/settings/",
"/admin/conferences/recordings/",
"/admin/addons/directory/",
"/docs/admin/"
'''
class Test3(unittest.TestCase):
    def setUp(self):                                                    # блок выполняется перед запуском тестов
        self.driver = webdriver.Chrome() #webdriver.Firefox() 		# указываем драйвер браузера, можно также указать webdriver.Chrome('./chromedriver')
        self.driver.implicitly_wait(10) 		                # 10 сек в качестве максимального таймаута для выполнения методов
        self.base_url = "http://localhost"
        self.verificationErrors = []
        '''
        self.driver.get(self.base_url + "/guest/login" )
        driver = self.driver
        #time.sleep(3)
        
        #авторизуемся на гостевой странице qa
        login_form = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div/div/div[1]/input')  #//*[@id="login__input-container__input-username"]
        login_form.send_keys("apukhtin")
        password_form = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/div/div/div/div[2]/input')  #//*[@id="login__input-container__input-password"]
        password_form.send_keys("XvA8LXTu")
        button = self.driver.find_elements_by_xpath('//*[@id="login__button"]/span')
        for elem in button:
            elem.click()
            '''
        self.driver.get(self.base_url + "/admin/users/aliases/" ) # открываем страницу списка конференций

	
    def test_stat(self):        # тест для проверки врмени загрузки страницы конференций
        
        loops=500 # число переоткрытий страниц
        driver = self.driver
        total_time = 0
        #driver.get("https://localhost/admin/conferences/list/")

        for j in range(loops):
            driver.refresh()
            #time.sleep(6)   # ждем 3 сек загрузку страницы, раскомментировать для Chrome! получаем число миллисекунд для браузерного события onload
            try:
                alias = self.driver.find_element_by_xpath('//*[@id="add-alias"]/div[1]/label/input')
                alias.send_keys("101"+str(j))
                user = self.driver.find_element_by_xpath('//*[@id="add-alias-tc-id"]')
                user.send_keys("user"+str(j))
                button = self.driver.find_elements_by_xpath('//*[@id="add-alias"]/a')
                for elem in button:
                    elem.click()
                #start = time.monotonic() #запускаем таймер попытки
                #element = WebDriverWait(driver, 250).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div[1]/section/div/div[2]/div/div[2]/div[2]/div/div/div[1]/button[1]")))
            finally:
                result = time.monotonic() - start
                total_time += result
                logging.info(" Cheak link "+self.base_url+"/admin/general/info/ " +" loading: "+str(j+1) + " Time loading: "+ str(result) + " sec.")
        logging.info(" Cheak link "+self.base_url+"/admin/general/info/ " +" loading all : "+str(loops) + " Average load time: "+ str(total_time/loops) + " sec.")
        
    def tearDown(self): # блок выполняется после запуска тестов
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        


if __name__ == "__main__":
    unittest.main()

result = time.monotonic() - start
logging.info("All time: " + str(result) + " seconds.")

