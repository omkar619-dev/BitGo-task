from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    
    driver = webdriver.Chrome()
    return driver

def get_transaction_hashes(driver):
    
    driver.get("https://blockstream.info/block/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732")

    
    wait = WebDriverWait(driver, 10)
    transactions = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "transaction-box")))

    for transaction in transactions:
        try:
            
            tx_hash = transaction.find_element(By.XPATH, ".//div[@class='txn font-p2']/a").text
            
            
            inputs = transaction.find_elements(By.XPATH, ".//div[@class='vins']/div[@class='vin']")
            outputs = transaction.find_elements(By.XPATH, ".//div[@class='vouts']/div[@class='vout']")

            
            if len(inputs) == 1 and len(outputs) == 2:
                print(f"Transaction Hash: {tx_hash}")

        except Exception as e:
            print(f"Error processing transaction: {e}")

def main():
    driver = setup_driver()
    try:
        get_transaction_hashes(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
