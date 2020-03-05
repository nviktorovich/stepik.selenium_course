from selenium import webdriver
import time
from math import log, sin
URL = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(URL)

try:
	# 1. press button
	browser.find_element_by_css_selector("button.trollface").click()

	# 2. next window
	browser.switch_to_window(browser.window_handles[1])
	res = log(abs(12 * sin(int(browser.find_element_by_id("input_value").text))))

	# 3. input to answer form
	ans = browser.find_element_by_id("answer")
	ans.send_keys(str(res))

	# 4. press submit
	browser.find_element_by_css_selector("button.btn").click()
finally:
	time.sleep(10)
	browser.quit()

# save the one empty string to correct work