from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Browser setup
driver = webdriver.Chrome()

try:
    # Website open kara
    driver.get("https://hello-testly.lovable.app/")
    driver.maximize_window()
    time.sleep(2) 

    # Email field shodhne ani data takne
    email_field = driver.find_element(By.TAG_NAME, "input") 
    email_field.send_keys("test_user@gmail.com")
    print("Email successfully takla aahe!")

    # Waitlist button click karne
    # Website pramane button shodhne
    submit_btn = driver.find_element(By.XPATH, "//button")
    submit_btn.click()
    print("Button click jhale!")

    time.sleep(5) 

finally:
    driver.quit()