from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from result import res # module with research


URL = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(URL)
#browser.implicitly_wait(13) #- waiting by 13 seconds
try:
	# 1. press book-btn at moment when price = $100
	WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
	browser.find_element_by_id("book").click()

	# 2. scroll the page to answer field
	field = browser.find_element_by_id("answer")
	browser.execute_script("return arguments[0].scrollIntoView(true);", field)
	field.send_keys(res(browser.find_element_by_id("input_value").text))

	# 3. press submit-button
	button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "solve")))
	button.click()
	#browser.find_element_by_id("solve").click()
	alert = browser.switch_to.alert
	print(alert.text)

finally:
	browser.quit()

# save the one empty string to correct work
