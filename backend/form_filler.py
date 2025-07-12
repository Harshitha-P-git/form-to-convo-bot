import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

def fill_form(url, responses):
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # ✅ Path to chromedriver.exe in parent directory of backend/
    driver_path = os.path.join(os.path.dirname(os.getcwd()), "chromedriver.exe")
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        print("🌐 Opening form...")
        driver.get(url)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "form")))
        print("🧭 Navigating through wizard pages...")

        # Step 1
        page1 = driver.find_element(By.CSS_SELECTOR, ".page.active")
        fname_input = page1.find_element(By.NAME, "fname")
        fname_input.clear()
        fname_input.send_keys(responses["fname"])
        print(f"✅ Filled 'fname' with '{responses['fname']}'")

        lname_input = page1.find_element(By.NAME, "lname")
        lname_input.clear()
        lname_input.send_keys(responses["lname"])
        print(f"✅ Filled 'lname' with '{responses['lname']}'")

        page1.find_element(By.XPATH, ".//button[text()='Next']").click()
        time.sleep(1.2)

        # Step 2
        page2 = driver.find_element(By.CSS_SELECTOR, ".page.active")
        email_input = page2.find_element(By.NAME, "user_email")
        email_input.clear()
        email_input.send_keys(responses["user_email"])
        print(f"✅ Filled 'user_email' with '{responses['user_email']}'")

        aadhaar_input = page2.find_element(By.NAME, "aadhaar_number")
        aadhaar_input.clear()
        aadhaar_input.send_keys(responses["aadhaar_number"])
        print(f"✅ Filled 'aadhaar_number' with '{responses['aadhaar_number']}'")

        page2.find_element(By.XPATH, ".//button[text()='Next']").click()
        time.sleep(1.2)

        # Step 3
        page3 = driver.find_element(By.CSS_SELECTOR, ".page.active")
        try:
            gender_select = Select(page3.find_element(By.NAME, "gender"))
            gender_select.select_by_visible_text(responses["gender"])
            print(f"✅ Selected gender: {responses['gender']}")
        except Exception as e:
            print(f"❌ Error selecting gender: {e}")

        lang_input = page3.find_element(By.NAME, "lang_pref")
        lang_input.clear()
        lang_input.send_keys(responses["lang_pref"])
        print(f"✅ Filled 'lang_pref' with '{responses['lang_pref']}'")

        submit_btn = page3.find_element(By.CSS_SELECTOR, "button[type='submit']")
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        time.sleep(0.5)
        submit_btn.click()
        print("🚀 Form submitted.")

    except Exception as e:
        print(f"❌ Error during form filling: {e}")

    finally:
        time.sleep(5)
        driver.quit()
