from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.common.by import By


class TestHome(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.close()

    def signup(self):
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

    def signin(self):
        self.signup()

        username = self.browser.find_element(By.ID, "your_name")
        username.send_keys("rgonnage")
        password = self.browser.find_element(By.ID, "your_pass")
        password.send_keys("ranga12345")
        signin = self.browser.find_element(By.ID, "signin")
        signin.click()

    def check_if_element_exists_by_id(self, element):
        try:
            self.browser.find_element(By.ID, "element")
        except NoSuchElementException:
            return False
        return True

    def test_home_with_logged_user(self):
        self.signin()

        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("home")
        )
        self.assertNotEqual(self.browser.page_source.find("LOGOUT"), -1)

    def test_home_with_not_logged_user(self):
        self.browser.get(self.live_server_url + reverse("home"))
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("home")
        )
        self.assertNotEqual(self.browser.page_source.find("LOGIN"), -1)
        