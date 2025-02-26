import json

from .objects import Scraper
from selenium.webdriver.common.by import By
import time


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
        try:
            with open("emails.txt", "r") as file:
                emails_data = [
                    email.strip() for email in file.read().split("\n") if email.strip()
                ]
        except FileNotFoundError:
            print("Please create `emails.txt` file.")
            exit()

        for email in emails_data:
            time.sleep(self.config.get("sleep_1", 5))
            self.send_email(
                email=email,
                subject=self.config.get("subject"),
            )

    def send_email(self, email, subject):
        self.driver.get(
            self.config.get("custom_link")
            .replace("{profile}", "0")
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
