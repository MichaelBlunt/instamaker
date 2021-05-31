from selenium import webdriver
import os
import random
import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

name = input('Enter the name of the user you would like to log in as without a space between first and last name: ')
directory = 'C:/Users/micha/Desktop/Programing/Selenium/Instagram_Accounts/'

data = json.load((open(((directory+name)+'.json'),))) #converts json to dict
step1 = str(data['instagram']) #converts cursed dict (instagrm, [everything else]) to just string of [everything else]
#print(step1) #uncomment me to see what the above confusing comment means
step2 = step1.replace("'", '')
step3 = step2.replace(' ', '')
step4 = step3[2:]
step5 = step4[:-2]
step6 = step5.replace(':', ',')
dataList = step6.split(',')

name = dataList[1]
username = dataList[3]
password = dataList[5]
year = dataList[7]
month = dataList[9]
day = dataList[11]

#initial stuff
browser = webdriver.Chrome("C:\Windows\chromedriver_win32\chromedriver.exe")
browser.maximize_window()
browser.delete_all_cookies()

browser.get("https://instagram.com")
time.sleep(5)

#find and fill out username field
username_field = browser.find_element_by_name('username')
username_field.send_keys(username)
time.sleep(0.5)

#find and fill out password field
password_field = browser.find_element_by_name('password')
password_field.send_keys(password)
time.sleep(0.5)

#click login
login_button = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
login_button.click()

