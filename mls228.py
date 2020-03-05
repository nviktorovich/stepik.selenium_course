from selenium import webdriver
import time
import os

URL = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(URL)
with open('test1.txt', 'w') as file:
	file.write('test1 for mls 228')


try:
	# 1. check text fields as name, surname, email
	for field in ['firstname', 'lastname', 'email']:
		check = browser.find_element_by_css_selector(f"[name = '{field}']")
		check.send_keys('test1')

	# 2. upload text file
	file_upload = browser.find_element_by_id("file")
	file_upload.send_keys(os.getcwd()+'/'+file.name)

	# 3. check submit button
	submit = browser.find_element_by_css_selector("button.btn")
	submit.click()
finally:
	time.sleep(10)
	browser.quit()

# save the one empty string to correct work