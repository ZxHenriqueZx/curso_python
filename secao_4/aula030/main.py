# Selenium - Automatizando tarefas no navegador
# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_BIN = ROOT_FOLDER / 'drivers'/'chromedriver-linux64'/'chromedriver'

def make_chrome_driver(*options):
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')

    if options is not None:
        for op in options:
            chrome_options.add_argument(op)

    chrome_service = Service(executable_path=CHROMEDRIVER_BIN)
    chrome_browser = webdriver.Chrome(
        service = chrome_service,
        options = chrome_options
        )

    return chrome_browser

options = ()
chrome = make_chrome_driver(*options)

chrome.get('https://www.google.com.br/')

search_input = WebDriverWait(chrome, 5).until(
    EC.presence_of_element_located((By.ID, 'APjFqb'))
    )

search_input.send_keys('Hello World!!')
search_input.send_keys(Keys.ENTER)

results = chrome.find_element(By.ID, 'search')
links = results.find_elements(By.TAG_NAME, 'a')
print(links[0].click())

time.sleep(5)
