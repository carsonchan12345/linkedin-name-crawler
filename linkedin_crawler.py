from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import sys

# initialize selenium driver with chrome
driver = webdriver.Chrome()

# a function allow selenium go to linkedin login page and login
def login():
    driver.get("https://www.linkedin.com/uas/login")
    time.sleep(10)

# selenium go to linkedin company page, /people/ is the url of linkedin company employee page, scroll down to bottom repeatingly untill there is no more employee being loaded. 

def scroll_down(company_name): # add a parameter to pass in the company name
    driver.get("https://www.linkedin.com/company/" + company_name + "/people/")
    last_height = driver.execute_script("return document.body.scrollHeight")
    i=0
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        i+=1
        last_height = new_height
    return driver.find_elements(By.CLASS_NAME, "org-people-profile-card__profile-title")
# on the selenium page, return all element in div class="org-people-profile-card__profile-title"

# end selenium driver
def end():
    driver.close()

# main function
if __name__ == "__main__":

    login()
    test=scroll_down(sys.argv[1])
    fileout=open(sys.argv[1]+"_employee.csv","w")
    for res in test:
        #check if res.get_attribute("textContent") is not empty
        if res.get_attribute("textContent") != "" and res.get_attribute("textContent").strip() != "LinkedIn Member":
            try:
            # strip string res of space and then split by space write all to employee.csv
                fileout.write(",".join(res.get_attribute("textContent").strip().split(" ")))
                fileout.write("\n")
            except:
                pass
    time.sleep(2)
    end()





