from selenium import webdriver
import time
import math


def calc(x):
	return str(math.log(abs(12 * math.sin(int(x)))))


URL = 'http://suninjuly.github.io/get_attribute.html'

try:
	browser = webdriver.Chrome()
	browser.get(URL)

	# 1. reading x value
	x = browser.find_element_by_id("treasure")

	# 2. insert the result into answer-field
	answer_field = browser.find_element_by_id("answer")
	answer_field.send_keys(calc(int(x.get_attribute('valuex'))))

	# 3. check the check-box "Im the robot"
	ch_b = browser.find_element_by_id("robotCheckbox")
	ch_b.click()

	# 4. check the radio-button "robots rule"
	r_b = browser.find_element_by_id("robotsRule")
	r_b.click()

	# 5. press submit-button
	sub_b = browser.find_element_by_css_selector("button.btn")
	sub_b.click()

finally:
	time.sleep(10)
	browser.quit()

# save the one empty string to correct work
