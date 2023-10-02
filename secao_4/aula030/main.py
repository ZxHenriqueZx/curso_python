from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_BIN = ROOT_FOLDER / 'drivers'/'chromedriver-linux64'/'chromedriver'

chrome_options = webdriver.ChromeOptions()
chrome_service = Service()
chrome_browser = webdriver.Chrome()
