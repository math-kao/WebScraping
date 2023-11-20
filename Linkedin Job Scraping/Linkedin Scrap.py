from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

account="#########"
password="########"

chrome_options=webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach",value=True)

driver=webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3714608636&f_AL=true&f_E=1%2C3&f_PP=104746682&keywords=Python&refresh=true&sortBy=R")

# #ENTRAR
time.sleep(2)
data=driver.find_element(By.LINK_TEXT,value="Entrar")
data.click()
#
# #USER E PASSWORD
time.sleep(2)
user_enter=driver.find_element(By.ID,value="username")
user_enter.send_keys(account)
password_enter=driver.find_element(By.ID,value="password")
password_enter.send_keys(password)

password_enter.send_keys(Keys.ENTER)

#Verification notication
input("Press Enter to go")

#Apply
#tabindex=0
#data-control-id
#button class="
time.sleep(3)

#Minimize Chat
minimize=driver.find_element(By.CLASS_NAME,value="msg-overlay-bubble-header__details")
minimize.click()


jobs = driver.find_elements(By.CLASS_NAME,value="jobs-search-results__list-item")

for job in jobs:
    # print(job.text)
    job.click()
    time.sleep(4)
    save_button = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
    save_button.click()

#Using CSS Selector instead of CLAS NAME
# job_list=driver.find_elements(By.CSS_SELECTOR,value=".job-card-container--clickable")
# listing_no=len(job_list)
# for x in range(listing_no):
#     job=job_list[x]
#     job.click()
#     time.sleep(1)
#     save_button = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
#     save_button.click()


#FOLLOW BUTTON PAGE 
    # try:
    #     company=driver.find_element(By.CLASS_NAME,value="artdeco-entity-lockup")
    #     follow_button=driver.find_element(By.CLASS_NAME,value="follow")
    #     follow_button.click()
    #
    # except NoSuchElementException:
    #     print("No application button")
    #     continue









