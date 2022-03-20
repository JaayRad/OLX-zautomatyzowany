from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

user = input('podaj email:  ')
password = input('podaj hasło:  ')


if user and password != None:
    driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")
    driver.get("https://www.olx.pl/")
    driver.maximize_window()
    driver.implicitly_wait(2)
    cookies = driver.find_element_by_id("onetrust-accept-btn-handler")
    cookies.send_keys(Keys.RETURN)
    login_menu = driver.find_element_by_id("topLoginLink")
    login_menu.send_keys(Keys.RETURN)
    email = driver.find_element_by_id("userEmail")
    email.send_keys(str(user))
    time.sleep(2)
    password = driver.find_element_by_id("userPass")
    password.send_keys(str(password))
    time.sleep(1)
    captcha = driver.find_element_by_id("se_userLogin")
    captcha.click()
    time.sleep(1)
    creating_listning_button = driver.find_element_by_id("postNewAdLink")
    creating_listning_button.click()
    title = driver.find_element_by_class_name("css-v49bm8")
    title.send_keys("Zbiory zadań z matematyki")
    time.sleep(1)
    category= driver.find_element_by_class_name("css-pyu9k9")
    category.click()
    time.sleep(1)
    category2 = driver.find_element_by_class_name("css-mufufg")
    category2.click()
    time.sleep(1)
    category3 = driver.find_element_by_class_name("css-1jek2ew-Text eu5v0x0")
    category3.click()
    adding_photo = driver.find_elements_by_partial_link_text("Dodaj zdjęcie").click()
else:
    pass

