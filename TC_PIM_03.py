from selenium import webdriver
from selenium.webdriver.common.by import By
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

# Step 1: Validate the below MENU options (on side pane) displaying on Admin page:
menu_option_element = browser.find_element(By.XPATH, '//ul[@class="oxd-main-menu"]').text
print(menu_option_element)
print("the user should be able to see the above-mentioned Admin page Menu Items on Admin Page.")

# Close the browser
browser.quit()
