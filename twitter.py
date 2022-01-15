from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

un = "cuellarandy12"
pw = "andres97"
driver = webdriver.Chrome()

# log in
driver.get("http://www.twitter.com/login")
unElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "session[username_or_email]")))
unElement.send_keys(un)
pwElement = driver.find_element_by_name("session[password]")
pwElement.send_keys(pw+"\n")

# open profile
profileButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@href="/'+un+'"]')))
profileButton.click()

followingButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@href="/'+un+'/following"]')))
followingButton.click()