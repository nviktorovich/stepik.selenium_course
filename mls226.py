from selenium import webdriver
import time
from math import log, sin

browser = webdriver.Chrome()
URL = 'http://SunInJuly.github.io/execute_script.html'
browser.get(URL)
try:
	# 1. find the x-value
	x = int(browser.find_element_by_id("input_value").text)

	# 2. use the function
	res = log(abs(12 * sin(x)))

	# 3. input the res to answer-field
	answer_field = browser.find_element_by_id("answer")
	browser.execute_script("return arguments[0].scrollIntoView(true);", answer_field)
	answer_field.send_keys(str(res))

	# 4, 5 check: robotCheckbox, robotsRule
	nec_id = ["robotCheckbox", "robotsRule"]
	for cur_id in nec_id:
		field = browser.find_element_by_id(cur_id)
		browser.execute_script("return arguments[0].scrollIntoView(true);", field)
		field.click()

	# 6. scroll page bottom and check submit
	submit = browser.find_element_by_css_selector("button.btn")
	browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
	submit.click()
finally:
	time.sleep(10)
	browser.quit()

# save the one empty string to correct work
