from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Launching the browser
browser = webdriver.Chrome()  # Assuming Chrome browser is being used
browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # Replace "URL" with the actual URL of Orange HRM 3.0 site
browser.maximize_window()
sleep(2)

# Logging in as Admin (Replace 'username' and 'password' with actual credentials)
username = "Admin"
password = "admin123"

# Locating and filling the username and password fields
username_field = browser.find_element(By.XPATH, '//input[@name="username"]')
username_field.send_keys(username)

password_field = browser.find_element(By.XPATH, '//input[@type="password"]')
password_field.send_keys(password)
sleep(2)

# Clicking on the login button
login_button = browser.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]')
login_button.click()
sleep(2)

# Clicking on the admin 
admin_label = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span')
admin_label.click()
# print("ADMIN_clicked")
sleep(3)

# Wait for the page to load after login
WebDriverWait(browser, 10).until(EC.title_contains("OrangeHRM"))
sleep(2)

# Step 1: Validate title of the page as "OrangeHRM"
page_title = browser.title
assert page_title == "OrangeHRM", "Title validation failed!"
print("valid Title")

# Step 2: Validate options on Admin page
option_element = browser.find_element(By.XPATH, '//div[@class="oxd-topbar-body"]').text
print(option_element)
print("the user should be able to see the above mentioned Admin page Header on Admin Page.")

# Close the browser
browser.quit()
