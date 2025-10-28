from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- Initialize Chrome WebDriver ---
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# --- Step 1: Open the movie page ---
driver.get("http://127.0.0.1:8000/movies/")

# --- Step 2: Wait for the search box to appear ---
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search movies...']"))
)

# --- Step 3: Type "Squid Game" into the search box ---
search_box.clear()
search_box.send_keys("Squid Game")

# --- Step 4: Find and click the Search button ---
# (Assuming there is a button next to the search box or with text 'Search')
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Search')]"))
)
search_button.click()

# --- Step 5: Wait for the next page (results) to load ---
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Squid Game')]"))
)

print("Successfully searched for 'Squid Game' and navigated to results page.")

# --- Optional pause to visually confirm ---
time.sleep(10)

# --- Close browser ---
driver.quit()
