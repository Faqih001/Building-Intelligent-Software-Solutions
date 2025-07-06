# Task 2: Automated Testing with AI (Selenium Example)
# Note: Requires selenium and a webdriver (e.g., ChromeDriver) installed.
# This script uses a public demo login page for demonstration purposes.
# Do NOT use real credentials for security reasons.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    try:
        # Wait for the username field to be interactable
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "username"))
        )
        driver.find_element(By.ID, "username").send_keys("invalid_user")
        driver.find_element(By.ID, "password").send_keys("invalid_pass")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Wait for an error message or failed login indication
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )
        error_text = driver.find_element(By.ID, "flash").text.lower()
        failure = ("invalid" in error_text or "your username is invalid" in error_text)
    except Exception as e:
        print("Test failed due to exception:", e)
        print("Page source for debugging:\n", driver.page_source[:1000])
        failure = False
    finally:
        driver.quit()

    print("Invalid login failure detected:", failure)

    summary = '''\
AI-powered testing tools like Selenium IDE with AI plugins or Testim.io enhance test coverage by automatically generating and maintaining test cases, adapting to UI changes, and identifying edge cases that manual testers might overlook. They can analyze application behavior, suggest new tests, and reduce maintenance overhead by self-healing scripts. This leads to higher reliability and faster feedback compared to manual testing, which is limited by human effort and prone to oversight. AI-driven automation ensures broader coverage and more consistent results, improving software quality and reducing time to release.
'''
    print(summary)

if __name__ == "__main__":
    test_login()
