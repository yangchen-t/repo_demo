from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from wxauto import WeChat
import time
import yaml 

wx = WeChat()
# wx.show()

config:str = "./cfg.yaml"
def read_config(config) -> map:
    with open(config, encoding='utf-8') as f:
        cfg = yaml.safe_load(f)
        f.close()
    return cfg
g_config=read_config(config)

number=g_config["NUMBER"]
chromedriver_path = g_config["PATH"]

url = "https://caonima.de/"
service = Service(executable_path=chromedriver_path)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("blink-settings=imagesEnabled=false")

browser = webdriver.Chrome(service=service, options=chrome_options)
browser.get(url)



def get_msg():

    # 等待页面元素加载
    try:
        element_present = EC.presence_of_element_located((By.ID, 'span_random_max'))
        WebDriverWait(browser, 10).until(element_present)
    except TimeoutException:
        print("check network && page is error")
        return

    flash = browser.find_element(By.ID, 'span_random_max')
    flash.click()
    time.sleep(0.05)  # 确保元素渲染完成
    text_content = browser.execute_script("return document.getElementById('txt_nmsl').innerText;")

    return text_content

for i in range(number):
    msg =get_msg()
    who = g_config["WHO"]
    at = g_config["AT"]
    wx.SendMsg(msg=msg, who=who, at=at)

browser.quit()