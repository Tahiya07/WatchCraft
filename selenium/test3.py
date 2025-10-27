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

    # Fill in login details
    driver.find_element(By.ID, "id_username").send_keys("Shaima")
    driver.find_element(By.ID, "id_password").send_keys("123qweas")

    # Click the login button
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("Login button clicked... waiting for redirect")

    # Wait until redirected to home page
    WebDriverWait(driver, 10).until(EC.url_contains("/"))
    print("Logged in successfully and redirected to homepage")

    # --- STEP 2: RATING SECTION ---
    # Wait until rating stars are visible on the homepage
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "star")))

    # Click on a 5-star rating
    star_to_click = driver.find_element(By.XPATH, "//span[@class='star' and @data-value='5']")
    star_to_click.click()
    print("Clicked 5-star rating")

    # Wait for comment box
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "comment")))

    # Enter a review comment
    comment_box = driver.find_element(By.NAME, "comment")
    comment_box.clear()
    comment_box.send_keys("Fantastic service! Really satisfied with the experience.")

    # Click the Submit button
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    print("Clicked the Submit button")

    # --- STEP 3: VERIFY SUCCESS ---
    time.sleep(5)
    page_source = driver.page_source

    if "Thank you" in page_source or "successfully" in page_source:
        print("Rating submitted successfully and confirmation message found!")
    else:
        print("Rating submitted, but confirmation message not detected.")

    # Pause to visually confirm
    time.sleep(5)

finally:
    # Close browser
    driver.quit()
