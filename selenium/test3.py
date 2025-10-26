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
    # Open login page
    driver.get("http://127.0.0.1:8000/users/login/")

    # Wait until the username and password fields appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id_username"))
    )
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id_password"))
    )

    # Fill in the login form
    driver.find_element(By.ID, "id_username").send_keys("Shaima")
    driver.find_element(By.ID, "id_password").send_keys("123qweas")

    # Click the login button (you can also use name="login" or another selector if needed)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Wait for redirect after successful login (adjust URL to your actual homepage)
    WebDriverWait(driver, 10).until(
        EC.url_changes("http://127.0.0.1:8000/users/login/")
    )

    # Verify if redirected to home/dashboard page
    current_url = driver.current_url
    if "home" in current_url or current_url == "http://127.0.0.1:8000/":
        print("Login successful! Redirected to:", current_url)
    else:
        print("Login did not redirect as expected. Current URL:", current_url)

    # Pause for visual confirmation
    time.sleep(10)

finally:
    # Close browser
    driver.quit()
