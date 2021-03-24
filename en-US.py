from selenium import webdriver
from pathlib import Path
from time import sleep
import random
import re
import os
import sys

# Matheus Eduardo
# github.com/eumts

# - VARIABLES -
login = input("Enter your Instagram login: ")
password = input("Enter your Instagram password: ")
number = 0
account = input("Write the user who you want to save the Followers: ")

# - LOGGIN IN -
driver = webdriver.Firefox()
driver.get("https://www.instagram.com/")
sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(str(login))
sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(str(password))
sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
sleep(5)
driver.get("https://www.instagram.com/" + str(account))
sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').click()
sleep(5)

# - LOOP -
while True:
    try:
        os.system("cls")
        div = driver.find_element_by_class_name("PZuss").get_attribute('innerHTML')
        matches = re.findall(
        r'<a[\s\w=?"]+title="[\w]+" href="/([\w\d]+)/"', div)
        with open("arrobas.txt", "w") as file:
            for i in matches:
                file.write('@' + i + '\n') 
            file.close
        driver.find_element_by_class_name('isgrP').send_keys(u'\ue00f') #page_down
        print("Scrolling the page...")
        print("Scrolls count: " + str(number + 1))
        number += 1
        with open('arrobas.txt', 'r') as f:
            n_lines = len(f.readlines())
            print("There is " + str(n_lines) + " accounts on the archive 'arrobas.txt'.")
            f.close
        sleep(1)
    except Exception as e:
        print(e)
        sleep(1)
