from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PyQt5.QtCore import Qt, QRunnable, QObject, pyqtSlot, pyqtSignal, QThreadPool
import requests
from PyQt5.QtCore import QObject, pyqtSignal
import time
from proxy_chrome_driver import get_chromedriver
from auto_action import auto_like, auto_haha, auto_play_video, auto_comment_on_livetream, auto_follow_on_livestream
import traceback
import shutil

from traodoisub import Traodoisub



class FBSelenium():

    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
    
    def login(self):
        try:

            # Navigate to the Facebook login page
            self.driver.get("https://www.facebook.com")

            time.sleep(5)

            # Find the username and password input fields and the login button using their respective attributes
            username_input = self.driver.find_element(By.ID, "email")
            password_input = self.driver.find_element(By.ID, "pass")
            login_button = self.driver.find_element(By.NAME, "login")

            # Enter your Facebook credentials
            username_input.send_keys("huyhanh12498@gmail.com")
            password_input.send_keys("Huythinh@68")


            # Click the login button
            login_button.click()

            if "https://www.facebook.com/" == self.driver.current_url:
                self.get_cookie_and_write_it_into_file(file_name="fb_cookie.txt")

            time.sleep(100)

        except Exception as error:
            print(error)

        

        self.driver.quit()


        # if "https://www.facebook.com/" == self.driver.current_url:
        #     self.signals.result.emit(f'Lưu profile thành công!')
        #     self.signals.profile_status.emit(1)
        #     self.driver.quit()
        #     # Add additional checks if needed
        # else:
        #     self.signals.result.emit(f'Lưu profile thất bại!')
        #     self.signals.profile_status.emit(0)
        #     self.driver.quit()
        #     self.remove_chrome_profile(user_data_directory=f'./user-profiles/{self.facebook_login_credential["uid"]}')

    def open_new_tab(self, url="/"):
        self.driver.execute_script(f"window.open('{url}');")

    def quit_driver(self):
        self.driver.quit()

    def get_cookie_and_write_it_into_file(self, file_name:str):
        cookies = self.driver.get_cookies()

        fb_cookie_str = ""

        for cookie in cookies:
            fb_cookie_str += cookie['name'] + '=' + cookie['value'] + ';'
        if file_name:
            with open(file_name, 'w') as file:
                # Write fb_cookie_str to the file
                file.write(fb_cookie_str)

            print('Wrote facebook cookie successfully!')

fb_woker = FBSelenium()
fb_woker.login()