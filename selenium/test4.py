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
    # --- STEP 1: LOGIN ---
    driver.get("http://127.0.0.1:8000/users/login/")

    # Wait for login fields
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id_username")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id_password")))

    # Fill in login form
    driver.find_element(By.ID, "id_username").send_keys("Shaima")
    driver.find_element(By.ID, "id_password").send_keys("123qweas")

    # Click the login button
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("🔐 Logged in... waiting for homepage")

    # Wait for home redirect
    WebDriverWait(driver, 10).until(EC.url_contains("/"))
    print("✅ Logged in successfully!")

    # --- STEP 2: CLICK 'SEE MORE' BUTTON ---
    # Wait until the See More button is visible
    see_more_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'See More')]"))
    )
    see_more_btn.click()
    print("➡️ Clicked 'See More' button")

    # Pause for visual confirmation
    time.sleep(5)

finally:
    # Close browser
    driver.quit()
