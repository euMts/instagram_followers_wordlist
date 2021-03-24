from selenium import webdriver
from pathlib import Path
from time import sleep
import random
import re
import os
import sys

# Matheus Eduardo
# github.com/eumts

# - DEFININDO VARIAVEIS -
login = input("Digite seu login do Instagram: ")
senha = input("Digite sua senha do Instagram: ")
numero = 0
conta = input("Digite o nome da conta para ver os seguidores: ")

# - ENTRANDO NO INSTAGRAM -
driver = webdriver.Firefox()
driver.get("https://www.instagram.com/")
sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(str(login))
sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(str(senha))
sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
sleep(5)
driver.get("https://www.instagram.com/" + str(conta))
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
        print("Scrollando a página...")
        print("Número de scrolls: " + str(numero + 1))
        numero += 1
        with open('arrobas.txt', 'r') as f:
            n_linhas = len(f.readlines())
            print("Foram armazenadas " + str(n_linhas) + " contas no arquivo 'arrobas.txt'.")
            f.close
        sleep(1)
    except Exception as e:
        print(e)
        sleep(1)
