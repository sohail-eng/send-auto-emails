import json

from .objects import Scraper
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException
import time
from .utils import get_valid_email, remove_valid_email, write_used_email


class AutomateEmails(Scraper):
    def __init__(self, driver=None, proxy=None):
        self.driver = driver
        try:
            with open("config.json", "r") as file:
                self.config = json.loads(file.read())
        except FileNotFoundError:
            print("Please create `config.json` file.")
            exit()
        if not self.driver:
            self.driver = self.initialize_remotely(proxy=proxy)
            self.create_window()

    def create_window(self):
        self.driver.execute_script("window.open('');")
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def start_processing(self):
        for profile_data in self.config.get("profiles", {}):
            subject = profile_data.get("subject", "")
            profile = profile_data.get("profile", 0)
            for counter in range(self.config.get("loop", 10)):
                email = get_valid_email(profile=0)
                if not email:
                    continue

                time.sleep(self.config.get("sleep_1", 5))
                self.send_email(
                    profile=profile,
                    email=email,
                    subject=subject,
                )
                print(
                    f"email sent, profile {profile}, loop {counter}, email {email}, subject {subject}"
                )
                write_used_email(profile=profile, email=email)
                remove_valid_email(profile=profile, email=email)

    def send_email(self, profile, email, subject):
        while True:
            try:
                self.driver.get(
                    self.config.get("custom_link")
                    .replace("{profile}", f"{profile}")
                    .replace("{email}", email)
                    .replace("{subject}", subject)
                )
                time.sleep(self.config.get("sleep_2", 5))
                self.click_button(
                    element=self.get_elements_by_time(
                        by=By.XPATH,
                        value='//div[@id=":ot"]',
                    )
                )
                break
            except NoSuchWindowException:
                self.driver.execute_script("window.open('');")
                time.sleep(2)
                self.driver.switch_to.window(self.driver.window_handles[-1])
                time.sleep(1)
                continue
