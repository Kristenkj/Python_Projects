# This is a sample Python script.
import time

import pytest
from selenium.webdriver.common.by import By


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class TestPositiveScenarios:

    @pytest.mark.positive
    @pytest.mark.login
    def test_positive_login(self, driver):
        # Open browser
        #driver = webdriver.Chrome()
        #time.sleep(3)

        # Navigate to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # Type username into username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class = 'btn' ]")
        submit_button_locator.click()
        time.sleep(2)

        # verify new page URL contains practicetestautomation.com/logged-in-successfully/
        # new_page_URL_locator = driver.find_element()
        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        text_locator1 = driver.find_element(By.TAG_NAME, "h1")
        actual_text = text_locator1.text
        assert actual_text == "Logged In Successfully"
        # text_locator2 = driver.find_element(By.NAME, "Congratulations student. You successfully logged in!")

        # Verify button Log out is displayed on the new page
        logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
        assert logout_button_locator.is_displayed()
