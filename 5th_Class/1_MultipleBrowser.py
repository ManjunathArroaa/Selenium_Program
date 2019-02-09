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

driver.get('https://facebook.com')
driver.maximize_window()
driver.find_element_by_id('email').send_keys('Manjunath')
driver.find_element_by_id('pass').send_keys('password')
driver.find_element_by_id('u_0_2').click()

