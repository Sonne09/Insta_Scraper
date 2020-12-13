from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget
import time


# open browser and navigate to instagram landing page.
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.instagram.com")

# targeting the username and password field
username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# clearing the username and password field
username.clear()
password.clear()

# passing username and password
username.send_keys("your username")
password.send_keys("your password")

# clicking login button
log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

# clicking not now buttons
not_now1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

# searching for items
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()
keyword = "#sagarmatha"
time.sleep(5)
searchbox.send_keys(keyword)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)

# scrolling the page
driver.execute_script("window.scrollTo(0,5000);")
images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]
images = images[:-2]
print('Number of scraped images: ', len(images))

# making the folder to save images
path = os.getcwd()
path = os.path.join(path, keyword[1:]+"_Pics")
os.mkdir(path)
print(path)

# downloading images
counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter))
    wget.download(image, save_as)
    counter += 1