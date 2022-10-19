from lib2to3.pgen2.pgen import PgenGrammar
import os
import time
import warnings
import random
import pyautogui as auto
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver import Keys
from selenium.webdriver.common import by
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.ui import WebDriverWait


#pembuka = random.choice('Ada baru nih gengs','Produk unggulan terbaru jenis','Produk terbaik jenis')
#ungkapan = random.choice('terkeren','terbaru','terbaik','tercakep','Produk terbaik')

#keyword = input('[+] kekyword : ')
keyword = 'baju dinas'
master_link = (f'https://shopee.co.id/search?keyword={keyword}')

try:
    from devtools import debug
except ImportError: 
    def debug(*args, **kwargs):
        pass
warnings.filterwarnings("ignore", category=DeprecationWarning) # bersihin informasi gak penting
# modul scraping
chrome_options = Options()
chrome_options.headless = False
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
chrome_options.add_argument('user-agent='+user_agent)
chrome_options.add_argument(r'--user-data-dir=D:\\sinau python\\system 4 selenium headlees\\selenium google\\Profile\\twibot')
driver = uc.Chrome(driver_executable_path="Driver\chromedriver.exe", use_subprocess=True, options=chrome_options)
os.system('title Find accaount twiter in twibots')
driver.get('http://192.168.1.207/threads')

driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div/span/span[1]/span/span[2]').click()
for i in range(10):
    p = i+1
    try:
        accaount_twiter = driver.find_element_by_xpath(f'/html/body/span/span/span[2]/ul/li[{p}]').text
        print(f'[+] {p}.{accaount_twiter}')
        f = open(f'AC_{accaount_twiter}.py','w')
        f.write(f"import master_upload as up"+'\n')
        f.write(f"up.use('{accaount_twiter}')")
        f.close()
    except:
        pass