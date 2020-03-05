from selenium import webdriver
import time
from math import log, sin

URL = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(URL)

try:
	# 1. press button
	btn = browser.find_element_by_css_selector("button.btn")
	btn.click()

	# 2. confirm alert message
	alert = browser.switch_to.alert
	alert.accept()

	# 3. solve math
	res = log(abs(12 * sin(int(browser.find_element_by_id("input_value").text))))

	# 4. input res to answer field
	field = browser.find_element_by_id("answer")
	field.send_keys(str(res))

	# 5. press submit
	browser.find_element_by_css_selector("button.btn").click()
finally:
	time.sleep(10)
	browser.quit()

# save the one empty string to correct work