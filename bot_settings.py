from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
import decouple

INSTAGRAM_URL = "https://www.instagram.com/"

INSTAGRAM_USERNAME = decouple.config('BOT_INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = decouple.config('BOT_INSTAGRAM_PASSWORD')

CHROME_DRIVER_PATH = r"C:\Users\chepe\Desktop\Development\chromedriver.exe"

class InstagramFollowerBot:
    def __init__(self, profile_to_visit):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def log_in_bot(self):
        """This function log into your account"""
        self.driver.get(url=INSTAGRAM_URL)
        time.sleep(1)

        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys(INSTAGRAM_USERNAME)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(INSTAGRAM_PASSWORD, Keys.ENTER)

        time.sleep(8)

    def find_following_users(self, profile_to_visit):
        """This function looks for followers """
        self.driver.get(url=f'{profile_to_visit}following/')
        time.sleep(2)

        # this code scrolls inside a popup
        modal = self.driver.find_element(By.CLASS_NAME, "_aano")
        for i in range(100):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(1)


        ## this code scroll inside a popup
        all_span_names = self.driver.find_elements(By.CSS_SELECTOR, "span._aacl._aaco._aacw._aacx._aad7._aade")

        # https://www.instagram.com/josechay_20/

        following_users = [span.text for span in all_span_names]

        time.sleep(3)

        return following_users



    def find_follower_users(self, profile_to_visit):
        """This function looks for followers """
        self.driver.get(url=f'{profile_to_visit}followers/')
        time.sleep(2)

        # this code scrolls inside a popup
        modal = self.driver.find_element(By.CLASS_NAME, "_aano")
        for i in range(100):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(1)

        ## this code scroll inside a popup
        all_span_names = self.driver.find_elements(By.CSS_SELECTOR, "span._aacl._aaco._aacw._aacx._aad7._aade")

        # https://www.instagram.com/josechay_20/

        followers_users = [span.text for span in all_span_names]

        time.sleep(3)

        return followers_users






