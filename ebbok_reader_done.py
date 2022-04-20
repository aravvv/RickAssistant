from tkinter import*
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
keyboard = Controller()
PATH = "/Users/mac/Desktop/sr1final auto/chromedriver"
#nameEntered = str(input("Enter the genre of the book you want to read:  "))
#if nameEntered == "fiction":
    #time.sleep(1)
    #options= webdriver.ChromeOptions()
    #options.add_experimental_option("detach", False)
    #options.add_experimental_option('excludeSwitches', ['enable-logging'])
question = str(input("Enter the name of the book :  "))

driver = webdriver.Chrome(PATH)
driver.get("https://www.pdfdrive.com/")

inputbox= driver.find_element(By.ID, 'q').send_keys(question)
'''btns= driver.find_element(By.CLASS_NAME, 'fa fa-search search-button')
btns.click()'''
time.sleep(1)
keyboard.press(Key.enter)
time.sleep(3)

btns= driver.find_element(By.CLASS_NAME, 'ai-search')
btns.click()

btn2= driver.find_element(By.ID, 'download-button-link')
btn2.click()
time.sleep(15)
btn3= driver.find_element(By.CLASS_NAME, 'text-center')
btn3.click()
