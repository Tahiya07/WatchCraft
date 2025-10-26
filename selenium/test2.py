from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open signup page
driver.get("http://127.0.0.1:8000/users/signup/")

# Wait until all required fields appear
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "id_username"))
)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "id_email"))
)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "id_password1"))
)

# Fill in the form fields
driver.find_element(By.ID, "id_username").send_keys("Shazia")
driver.find_element(By.ID, "id_email").send_keys("rabeashazia53@gmail.com")
driver.find_element(By.ID, "id_password1").send_keys("12qwe123q#")

# Pause to visually confirm
time.sleep(10)

# Close browser
driver.quit()
