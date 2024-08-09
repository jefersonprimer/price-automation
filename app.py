from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui

driver = webdriver.Chrome()
driver.get('https://precos-de-produtos.netlify.app/')
sleep(5)

driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

button_more = driver.find_element(By.XPATH, "button[@id='loadMoreButton']")
sleep(2)
button_more.click()
sleep(2)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
sleep(1)

driver.execute_script('window.scrollTo(0, 0);')
sleep(2)

button_charge_excell = driver.find_element(By.XPATH, "button[@class='btn btn-primary btn-custom']")
sleep(2)

button_charge_excell.click()
sleep(5)

pyautogui.write(r'C:\Users\jdsjh\Downloads\precos-produtos-atualizados.xlsx')
sleep(2)
pyautogui.press('enter')
input('Click enter to terminal to closed program')