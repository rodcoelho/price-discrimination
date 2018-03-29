#!/usr/bin/env python3

from pyvirtualdisplay import Display
import time, requests, random, os, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from writeout import write_out_to_log
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

url_ip_location = 'http://ipinfo.io/json'
r = requests.get(url_ip_location).json()
r = r['city']

website = 'https://www.google.com/flights/#search;f=JFK,EWR,LGA;t=SFO;'
month = int(str(datetime.date.today())[5:7]) + 1
year = int(str(datetime.date.today())[:4])
if month < 10:
    month = '0' + str(month)
    year = str(year)
elif month == 13:
    month = '01'
    year = str(year + 1)
else:
    month = str(month)
    year = str(year)
dates = [
        ['d=' + year + '-' + month + '-25;r=' + year + '-' + month + '-28', 'f1'],
        ['d=' + year + '-' + month + '-18;r=' + year + '-' + month + '-28', 'f2'],
        ['d=' + year + '-' + month + '-11;r=' + year + '-' + month + '-28', 'f3'],
        ['d=' + year + '-' + month + '-04;r=' + year + '-' + month + '-28', 'f4'],
        ['d=' + year + '-' + month + '-25;r=' + year + '-' + month + '-28', 'f5'],
        ['d=' + year + '-' + month + '-18;r=' + year + '-' + month + '-25', 'f6'],
        ['d=' + year + '-' + month + '-11;r=' + year + '-' + month + '-18', 'f7'],
        ['d=' + year + '-' + month + '-04;r=' + year + '-' + month + '-11', 'f8']
         ]

display = Display(visible=0, size=(1920, 1080)).start()
firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
firefox_capabilities['binary'] = '/usr/bin/firefox'


def init_driver():
    ### possible gecko paths ###
    # /usr/local/bin/geckodriver
    # /tmp/geckodriver-v0.18.0-linux64.tar.gz
    # /home/rodrigocoelho/geckodriver-v0.18.0-linux64.tar.gz
    # /home/rodrigocoelho/dotfiles/geckodriver.log

    gecko = '/usr/local/bin/geckodriver'
    binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
    # driver = webdriver.Firefox(capabilities=firefox_capabilities)
    driver = webdriver.Firefox(capabilities=firefox_capabilities, executable_path=gecko) # firefox_binary=binary,

    driver.wait = WebDriverWait(driver, 5)
    try:
        time.sleep(5)
        os.system('Xvfb :10 -ac &')
        time.sleep(5)
        os.system('export DISPLAY=:10')
    except:
        print('display failed')
    return driver


def lookup(driver):

    # loads page
    for date in dates:
        time.sleep(random.uniform(1, 6))
        driver.get(website+date[0])

        timeout = 35
        try:
            WebDriverWait(driver, timeout)
            driver.implicitly_wait(25)
            # get text within div class
            element = driver.find_element_by_class_name('LJV2HGB-d-Ab')
            price = (element.get_attribute('innerHTML'))
            # price = price[1:]
            payload[date[1] + '-' + str(int(time.time()))] = {
                'description': date[0],
                'flight_id': date[1],
                'price': price,
                'city': r,
                'unix': int(time.time())
            }
        except:
            payload['Error' + str(int(time.time()))] = 'Error Handler'


if __name__ == "__main__":
    # init driver
    driver = init_driver()
    payload = {}
    time.sleep(round(random.uniform(0, 3)*60 + round(random.uniform(0, 59))))  # sleeps for random amount of time
    lookup(driver)
    write_out_to_log(payload, region=r)
    # close driver
    driver.quit()

