from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait

try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(12) #Даёт 12 секунд на прогрузку страницы, с попыткой взаимодействия каждые 0.5 секунд

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, "book")
    button.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value.nowrap")
    x = x_element.text

    y = calc(x)

    enter = browser.find_element(By.CSS_SELECTOR, "#answer.form-control")
    enter.send_keys(y)


    submit = browser.find_element(By.ID, "solve")
    submit.click()

    time.sleep(5)
finally:
    browser.quit()