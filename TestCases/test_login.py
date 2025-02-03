from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities.CustomLogger import LogGen
from PageObjects.LoginPage import Login
from Utilities.ReadProperties import Readconfig
import pytest
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Login_001:
    baseURL = Readconfig.getApplicationURL()
    useremail = Readconfig.getUserEmail()
    password = Readconfig.getPassword()

    logger = LogGen.loggen()
    logger.debug('******basic****')

    def test_homePageTitle(self, setup):
        self.logger.info("*********TC_001_Login*******************")
        self.logger.info("********* verifying home page title *******************")

        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        self.driver.close()
        if act_title == "Home Page":
            assert True
            self.logger.info("*********Home page title is passed *******************")

        else:
            self.logger.error("*********Home page title is failed *******************")
            assert False

    @pytest.mark.smoke
    def test_login(self, setup):
        self.logger.info("*********verifying login testcase *******************")

        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)
        self.lp.click_On_link()
        self.lp.set_username(self.useremail)
        self.lp.set_password(self.password)
        self.lp.click_on_btn()

        try:
            # Use explicit wait instead of sleep
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "search"))
            )

            act_title = self.driver.title
            expected_title = "Home Page"

            assert act_title == expected_title, f"Expected title '{expected_title}', but got '{act_title}'"
            self.logger.info("********* login test is passed *******************")

        except Exception as e:
            screenshot_path = os.path.join(os.getcwd(), "Screenshots", "new.png")
            self.driver.get_screenshot_as_file(screenshot_path)
            assert False, f"Test failed due to {e}"

        finally:
            self.driver.close()
