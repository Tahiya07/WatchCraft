from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- Initialize Chrome WebDriver ---
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# --- Step 1: Open the movie search results page ---
driver.get("http://127.0.0.1:8000/movies/?q=squid+game")

# --- Step 2: Wait for movie cards to load ---
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME, "movie-card"))
)

# --- Step 3: Find and click the 'View Details' or 'See Details' link/button ---
try:
    view_details_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(),'View Details') or contains(text(),'See Details')] | //button[contains(text(),'View Details') or contains(text(),'See Details')]")
        )
    )
    view_details_button.click()
    print("Clicked the 'View Details' button successfully!")

except Exception as e:
    print("Could not find the 'View Details' button:", e)

# --- Step 4: Wait for details page to load ---
WebDriverWait(driver, 15).until(
    EC.url_contains("/movies/")
)

print("Navigated to the movie details page!")

# --- Optional pause to visually confirm ---
time.sleep(10)

# --- Close browser ---
driver.quit()
