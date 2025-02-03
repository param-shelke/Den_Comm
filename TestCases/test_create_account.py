import time
import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
from Utilities.ReadProperties import Readconfig
from Utilities.CustomLogger import LogGen
from Utilities import XLUtils
from PageObjects.Create_An_Account_Page import Create_Account  # Importing Page Object class


class Test_Registration_DDT:
    baseURL = Readconfig.getApplicationURL()
    path = r"C:\Users\Prem\Python\PycharmProjects\Den_Comm\TestData\test_data.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_registration_ddt(self, setup):
        self.logger.info("********* Test_Registration_DDT *******************")
        self.logger.info("********* Verifying Registration with Multiple Data Inputs *******************")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.reg = Create_Account(self.driver)
        self.lp = Login(self.driver)

        rows = XLUtils.getRowCount(self.path, "Sheet2")
        lst_status = []

        for r in range(2, rows + 1):  # Skipping header row
            first_name = XLUtils.readData(self.path, "Sheet2", r, 1)
            last_name = XLUtils.readData(self.path, "Sheet2", r, 2)
            email = XLUtils.readData(self.path, "Sheet2", r, 3)
            password = XLUtils.readData(self.path, "Sheet2", r, 4)
            confirm_password = XLUtils.readData(self.path, "Sheet2", r, 5)
            expected_result = XLUtils.readData(self.path, "Sheet2", r, 6)

            self.logger.info(f"***** Executing Test for {email} *****")

            try:
                self.reg.click_on_create_acccount_link()
                self.reg.Enter_username(first_name)
                self.reg.Enter_lastname(last_name)
                self.reg.Enter_email(email)
                self.reg.Enter_password(password)
                self.reg.Enter_password_confirm(confirm_password)
                self.reg.click_on_create_button()

                time.sleep(3)
                actual_message = self.reg.get_success_msg()
                expected_message = 'Thank you for registering with Main Website Store.'

                if actual_message == expected_message:
                    lst_status.append("Pass")
                    self.logger.info(f"***** Test Passed for {email} *****")
                else:
                    lst_status.append("Fail")
                    self.logger.error(f"***** Test Failed for {email} *****")

            except Exception as e:
                self.logger.error(f"***** Exception occurred: {str(e)} *****")
                screenshot_path = f"C:\\Users\\Prem\\Python\\PycharmProjects\\Den_Comm\\Screenshots\\{email}.png"
                self.driver.get_screenshot_as_file(screenshot_path)
                lst_status.append("Fail")

            finally:
                self.driver.get(self.baseURL)  # Reset page for next test
                self.lp.signout_drop()
                self.lp.move_to_element()
                time.sleep(2)

        if "Fail" not in lst_status:
            assert True
        else:
            assert False

        self.driver.quit()
