from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
URL = 'http://suninjuly.github.io/selects2.html'

try:
	browser = webdriver.Chrome()
	browser.get(URL)

	# 1. find summ
	summ = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)

	# 2. select summ in drop-list
	select = Select(browser.find_element_by_id("dropdown"))
	select.select_by_visible_text(str(summ))

	# 3. press the submit button
	btn = browser.find_element_by_css_selector("button.btn")
	btn.click()

finally:
	time.sleep(10)
	browser.quit()

# save the one empty string to correct work
