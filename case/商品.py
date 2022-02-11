'''
 1.实现商品添加的流程自动化
    复制选中的行数，默认是一行，ctrl+d
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

number='4'
driver=webdriver.Chrome()
driver.maximize_window()
sleep(3)
driver.get('http://39.98.138.157/shopxo/index.php')
driver.find_element('link text','登录').click()
sleep(1)
driver.find_element('name','accounts').send_keys('hongx666')
sleep(1)
driver.find_element('name','pwd').send_keys('123456')
sleep(1)
driver.find_element('xpath','//button[text()="登录"]').click()

#搜索手机商品
driver.find_element('id','search-input').send_keys('手机')
sleep(2)
driver.find_element('id','ai-topsearch').click()
sleep(2)
driver.find_element('xpath','//div[@class="items"]/a[1]').click()
sleep(2)

#切换到商品详情页
handles=driver.window_handles
sleep(1)
driver.close()
sleep(1)
driver.switch_to.window(handles[1])
sleep(2)
#添加商品属性
driver.find_element('xpath','//li[@data-value="套餐一"]').click()
sleep(1)
driver.find_element('xpath','//li[@data-value="金色"]').c