from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Open signup page
    driver.get("http://127.0.0.1:8000/users/signup/")

    # Wait until all required fields appear
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id_username")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id_email")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id_password1")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id_password2")))

    # Fill in the signup form
    driver.find_element(By.ID, "id_username").send_keys("Whaida")
    driver.find_element(By.ID, "id_email").send_keys("ayshawahida1995@gmail.com")
    driver.find_element(By.ID, "id_password1").send_keys("12qye124q#")
    driver.find_element(By.ID, "id_password2").send_keys("12qye124q#")

    # Click the signup button (update selector if your button differs)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Wait for redirection to the login page
    WebDriverWait(driver, 10).until(
        EC.url_contains("/users/login/")
    )

    # Verify redirect
    current_url = driver.current_url
    if "login" in current_url:
        print("Signup successful! Redirected to the login page:", current_url)
    else:
        print("Signup button clicked, but redirection not confirmed. Current URL:", current_url)

    # Pause to visually confirm
    time.sleep(10)

finally:
    # Close browser
    driver.quit()
