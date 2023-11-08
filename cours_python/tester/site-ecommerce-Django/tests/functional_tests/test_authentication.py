from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.common.by import By


class TestAuthentification(StaticLiveServerTestCase):
    def test_signup(self):
        # Ouvrir le navigateur avec le webdriver
        self.browser = webdriver.Chrome()
        self.browser.get(self.live_server_url + reverse("signup"))

        fname = self.browser.find_element(By.ID, "fname")
        fname.send_keys("Ranga")

        lname = self.browser.find_element(By.ID, "lname")
        lname.send_keys("Gonnage")

        username = self.browser.find_element(By.ID, "username")
        username.send_keys("rgonnage")

        email = self.browser.find_element(By.ID, "email")
        email.send_keys("test@test.com")

        password1 = self.browser.find_element(By.ID, "pass")
        password1.send_keys("ranga12345")

        password2 = self.browser.find_element(By.ID, "re_pass")
        password2.send_keys("ranga12345")

        agree_term = self.browser.find_element(By.ID, "agree-term")
        agree_term.click()

        signup = self.browser.find_element(By.ID, "signup")
        signup.click()

        self.assertEqual(self.browser.find_element(By.TAG_NAME, 'h2').text, "Log In")
        self.assertEqual(self.browser.current_url, self.live_server_url + reverse("login"))

        # Fermer le navigateur
        self.browser.close()
