
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
import pause
import datetime
import random

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
service = Service(r'C:\Drivers\geckodriver.exe')
driver = webdriver.Firefox(service=service, options=options)
driver.get("https://reserve.pokemon-cafe.jp/")

# 席の予約 HTML 1 - Make a reservation
#driver.find_element(By.XPATH, "//*[@class='button arrow-down']").click()

# 席の予約 HTML 1 - Agree T&C
driver.find_element(By.XPATH, "//*[@class='agreeChecked']").click()
driver.find_element(By.XPATH, "//*[@class='button']").click()

# 席の予約 HTML 2 - Make a reservation
driver.implicitly_wait(3)
driver.find_element(By.XPATH, "//*[@class='button arrow-down']").click()

# 席の予約 HTML 3 - Select number of guest
select = Select(driver.find_element(By.NAME, 'guest'))
#Number of guests
select.select_by_index(7)

# 席の予約 HTML 4 - Select from calendar
driver.find_element(By.XPATH, "//*[contains(text(), '次の月を見る')]").click()
#Use this for the 1am round
driver.find_element(By.XPATH, "//*[contains(text(), '未開放')]").click()
#Use this afer 1am, change 12 to be however many full days are on the calendar
#driver.find_elements(By.XPATH, "//*[contains(text(), '満席')]")[12].click()

#Year, month, day, hour, minute, second
dt = datetime.datetime(2024, 1, 9, 1, 20, 1)
pause.until(dt)
driver.find_element(By.XPATH, "//*[@class='button']").click()
#Use the code below if you want it to try and pick a timeslot
#driver.implicitly_wait(2)
#elts = driver.find_elements(By.XPATH, "//*[contains(text(), '空席')]")
#rand = random.randrange(0, len(elts))
#elts[rand].click()
