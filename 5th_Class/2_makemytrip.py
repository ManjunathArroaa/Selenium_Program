import time
from selenium import  webdriver

browser ='Chrome'

if browser == 'Chrome':
    driver=webdriver.Chrome(executable_path='C:/Users/MANJUNATH T/PycharmProjects/first prgm/drivers/chromedriver.exe')
elif browser == 'Firefox':
    driver = webdriver.Chrome(executable_path='C:/Users/MANJUNATH T/PycharmProjects/first prgm/drivers/geckodriver.exe')
elif browser =='IE':
    driver = webdriver.Chrome(executable_path='C:/Users/MANJUNATH T/PycharmProjects/first prgm/drivers/IEDriverServer.exe')
else:
    print('Provide appropriate browser name')


driver.get('https://makemytrip.com/')
driver.maximize_window()
driver.find_element_by_id('header_tab_hotels').click()
time.sleep(5)
driver.back()
