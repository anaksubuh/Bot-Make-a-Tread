from __future__ import print_function
from lib2to3.pgen2.pgen import PgenGrammar
from operator import length_hint
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

def use(target):
    print('='*47)
    print()
    keyword = input('[+] kekyword : ')
    print()
    master_link = (f'https://shopee.co.id/search?keyword={keyword}&page=0&sortBy=sales')

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
    os.system('title MAKE TREAD http://192.168.1.207/thread')
    print('='*25)
    print()

    loop = 15
    driver.get(master_link)
    print(f'[+] {master_link}')

    while True:
        try:
            link = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/a').get_attribute('href')
        except:
            continue
        else:
            break

    f = open('link_produk.txt','w')
    f.write('')
    f.close()
    for i in range(loop):
        p = i+1
        try:
            link = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[{p}]/a').get_attribute('href')
        except:
            print('[+] Maaf kamu gagal mendapatkan link (error)')
        else:
            print(link)
            f = open('link_produk.txt','a')
            f.write(link+'\n')
            f.close()

    bil = random.randint(0, loop)
    master_link_image = driver.find_element_by_xpath(f'/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[{bil}]/a').get_attribute('href')
    driver.get(master_link_image)
    time.sleep(3)

    while True:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/div[1]').screenshot('A1_image.png')
        except:
            continue
        else:
            break

    delay_input_data_twibot = 0

    driver.get('http://192.168.1.207/threads')

    # memilih akun
    print(f'[+] choise {target}')
    print()
    driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[2]/div[1]/div/span/span[1]/span/span[2]').click()

    for i in range(10):
        p = i+1
        try:
            accaount_twiter = driver.find_element_by_xpath(f'/html/body/span/span/span[2]/ul/li[{p}]').text
            print(f'[+] {p}.{accaount_twiter}')
        except:
            pass

    print()

    for i in range(10):
        p = i+1
        try:
            accaount_twiter = driver.find_element_by_xpath(f'/html/body/span/span/span[2]/ul/li[{p}]').text
        except:
            pass
        else:
            if accaount_twiter == target:
                print(f'[+] sukses memilih sesuai target [{accaount_twiter}]')
                driver.find_element_by_xpath(f'/html/body/span/span/span[2]/ul/li[{p}]').click()

    # input gambar
    try:
        driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[2]/div[2]/div/div/form/div').click()
        time.sleep(1)
        auto.write("D:\sinau python\system 15 'scraping web'\Bot twibots\A1_image.png")
        time.sleep(1)
        auto.press('enter')
    except:
        print('[+] gagal')
    else:
        print('[+] sukses')

    time.sleep(delay_input_data_twibot)

    # get trending in twiter
    try:
        trending = driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[2]/form/div[1]/div/textarea').text
    except:
        print('[+] error in input trendings')
    else:
        print(f'[+] {trending}')

    time.sleep(delay_input_data_twibot)

    # input caption
    panjang_nama_produk = len(keyword)
    max_trending = 150-panjang_nama_produk
    trending = trending[0:max_trending]
    try:
        driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[2]/form/div[2]/div/textarea').send_keys(f'{keyword} {trending}')
    except:
        print('[+] gagal input caption')
    else:
        print('[+] sukses input caption')

    time.sleep(delay_input_data_twibot)

    # input tulisan Link :
    try:
        driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[2]/form/div[3]/div/textarea').send_keys('\n\nLink : ')
    except:
        print('[+] gagal input (link : )')
    else:
        print('[+] sukses input (link : )')

    time.sleep(delay_input_data_twibot)

    # input url produk shopee
    # Using readlines()
    file1 = open('link_produk.txt', 'r')
    Lines = file1.readlines()
    
    count = 0
    # Strips the newline character
    try:
        for line in Lines:
            count += 1
            text = line.strip()
            try:
                driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/div[2]/form/div[4]/div/textarea').send_keys(text+'\n')
            except:
                print('[+] gagal input (link : )')
            else:
                time.sleep(0.1)
    except:
        pass

    # submit
    try:
        driver.find_element_by_id('submit-url').click()
    except:
        print('[+] gagal click submit produk')
    else:
        print('[+] sukses submit produk')

    while True:
        try:
            driver.find_element_by_xpath('/html/body/div[7]/div/div[4]/div/button').click()
        except:
            continue
        else:
            time.sleep(5)
            driver.quit()