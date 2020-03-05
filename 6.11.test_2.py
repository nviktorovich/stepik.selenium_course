from selenium import webdriver
import time

try:
	link = "http://suninjuly.github.io/registration2.html"
	browser = webdriver.Chrome()
	browser.get(link)

	name = browser.find_element_by_css_selector(".first_block  .form-group.first_class input")
	name.send_keys("sdasdasd")
	last = browser.find_element_by_css_selector(".first_block  .form-group.second_class input")
	last.send_keys("sdasdasd")
	email = browser.find_element_by_css_selector(".first_block  .form-group.third_class input")
	email.send_keys("sdasdasd")

	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	time.sleep(1)
	welcome_text_elt = browser.find_element_by_tag_name("h1")
	welcome_text = welcome_text_elt.text
	assert "Congratulations! You have successfully registered!" == welcome_text

finally:
	time.sleep(10)
	browser.quit()
