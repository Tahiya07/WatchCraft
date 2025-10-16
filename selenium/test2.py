from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open login page
driver.get("http://127.0.0.1:8000/users/login/")

# Wait until the username field appears
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "id_username"))
)

# Type username
driver.find_element(By.ID, "id_username").send_keys("Shazia")

# Optional: type password if needed
# driver.find_element(By.ID, "id_password").send_keys("yourpassword")

# Pause to see it work
import time
time.sleep(5)

# Close
driver.quit()
