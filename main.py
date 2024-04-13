from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configure driver path
driver_path = r'C:\Users\User\Desktop\discordbot\chromedriver.exe' # webdriver folder path

# Configure Selenium driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) # Allows the browser not to close automatically

# Configure the driver service
service = webdriver.chrome.service.Service(driver_path)

# Configure the driver using the service
driver = webdriver.Chrome(service=service, options=options)

# Initialize the browser
  # Example using Chrome, but you can use another browser

try:
    # Navigate to Discord login page
    driver.get('https://discord.com/login')

    # Wait until the login page is completely loaded
    driver.implicitly_wait(10)

    #CHANGE EMAIL AND PASSWORD!!!
    #CHANGE EMAIL AND PASSWORD!!!
    #CHANGE EMAIL AND PASSWORD!!!
    #CHANGE EMAIL AND PASSWORD!!!

    # Find the email field and enter the email
    email_field = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    email_field.send_keys('myemail@email.com')

    # Find the password field and enter the password
    password_field = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
    password_field.send_keys('Mypassword123')

    # Find the login button and submit the form
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    login_button.click()

    # Wait for the login to complete
    driver.implicitly_wait(10)


    # Keep the browser open longer for ******educational purposes*****
    input('Press any key to close the browser...')
finally:
    # Close the browser only when you are ready to exit
    driver.quit()