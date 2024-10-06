from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    
    driver.get("https://blockstream.info/block/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732")
    wait = WebDriverWait(driver, 10)
    heading = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[normalize-space()='25 of 2875 Transactions']")))

    assert heading.text == "25 of 2875 Transactions", "Heading does not match expected text!"
    print("Test Case 1 Passed: Heading is correct.")
except Exception as e:
    print(f"Error encountered: {e}")