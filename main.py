from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from sheetReader import sheetReader

i = 0
arrayXlsx = sheetReader()

def challenge_bot() -> None:
    driver = webdriver.Chrome()
    driver.get("https://rpachallenge.com/")

    startButton = driver.find_element(By.TAG_NAME, "button")
    startButton.click()

    inputPrinter(arrayXlsx, driver)

    input("Enter")
    driver.quit()

def inputPrinter(arrayXlsx: List, driver: webdriver) -> None:
    Inputs = ["FirstName", "LastName", "CompanyName", "Role", "Address", "Email",  "Phone"]
    a = 0
    b = 0
    i = 0
    while i < 10:
        for x in Inputs:
            inputLabel = driver.find_element(By.CSS_SELECTOR, f'[ng-reflect-name="label{x}"]')
            inputLabel.send_keys(arrayXlsx[a][b])
            b += 1
            
        submitButton = driver.find_element(By.CSS_SELECTOR, 'input[value="Submit"]')
        submitButton.click()
        b = 0
        a += 1
        i += 1

if __name__ == "__main__":
    challenge_bot()