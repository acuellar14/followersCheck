import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# https://chromedriver.chromium.org/downloads

# TODO: add username and password
un = ""
pw = ""
scrollWait = 0.5;

driver = webdriver.Chrome()
driver.get("http://www.instagram.com")

# login page
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "username")))
unElement = driver.find_element_by_name("username")
unElement.send_keys(un)
pwElement = driver.find_element_by_name("password")
pwElement.send_keys(pw+"\n")

# save login info
notNowButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Not Now')]")))
notNowButton.click()

# turn on notification
notNowButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Not Now')]")))
notNowButton.click()

# open profile
driver.get("http://www.instagram.com/"+un)

# open followers and get count
followersButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "followers")))
followersCount = int(followersButton.text.replace(" followers", ""))
followersButton.click()

#scroll to bottom of followers
followersElements = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "wo9IH")))
while len(followersElements) < followersCount:
    followersDialog = driver.find_element_by_xpath('//div[@class="isgrP"]//a')
    followersElements = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "wo9IH")))
    followersDialog.send_keys(Keys.END)
    time.sleep(scrollWait)

# put follower usernames in a list
followersList = []
for x in range(len(followersElements)):
    followersList.append(followersElements[x].text[:followersElements[x].text.index("\n")])

# open profile
driver.get("http://www.instagram.com/"+un)

# open following and get count
followingButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "following")))
followingCount = int(followingButton.text.replace(" following", ""))
followingButton.click()

#scroll to bottom of following
followingElements = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "wo9IH")))
while len(followingElements) < followingCount:
    followingDialog = driver.find_element_by_xpath('//div[@class="isgrP"]//a')
    followingElements = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "wo9IH")))
    followingDialog.send_keys(Keys.END)
    time.sleep(scrollWait)

# put following usernames in a list
followingList = []
for x in range(len(followingElements)):
    followingList.append(followingElements[x].text[:followingElements[x].text.index("\n")])

# print users not following back
print("Not following me back:")
for curFollowing in followingList:
    if curFollowing not in followersList:
        print(curFollowing)

# print users I'm not following back
print("I'm not following back:")
for curFollower in followersList:
    if curFollower not in followingList:
        print(curFollower)
