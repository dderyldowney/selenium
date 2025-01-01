from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
options.driver_executable_path = "/usr/local/bin/chromedriver"
options.accept_insecure_certs = True
options.ignore_ssl_errors = True

chrome_browser = webdriver.Chrome(options=options)
chrome_browser.get("https://www.google.com")
assert "Google" in chrome_browser.title

