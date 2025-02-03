import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities.CustomLogger import LogGen
from PageObjects.LoginPage import Login
from Utilities.ReadProperties import Readconfig
import pytest
import os
from Utilities import XLUtils


class Test_Login_002_DDT:
    baseURL = Readconfig.getApplicationURL()
    path = r"C:\Users\Prem\Python\PycharmProjects\Den_Comm\TestData\Test_data.xlsx"
    logger = LogGen.loggen()
    logger.debug('******basic****')

    @pytest.mark.smoke
    def test_login_ddt(self, setup):
        self.logger.info("*********Test_login_002_DDT *******************")
        self.logger.info("*********verifying login testcase *******************")

        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)
        self.lp.click_On_link()

        self.rows = XLUtils.getColumnCount(self.path, "Sheet1")

        lst_status = []
        for r in range(1, self.rows + 1):
            self.lp.click_On_link()
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.set_username(self.user)
            self.lp.set_password(self.password)
            self.lp.click_on_btn()

            act_title = self.driver.title
            exp_title = "Home Page"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("**** Passed ****")
                    self.lp.signout_drop()
                    self.lp.move_to_element()
                    lst_status.append("Pass")

                elif self.exp == "Fail":
                    self.lp.signout_drop()
                    self.lp.move_to_element()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*******failed*********")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("******passed******")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("*****Login_ddt_002_passed******")
            self.driver.close()
            assert True
        else:
            self.logger.info("*******Login_ddt_002_Failed********")
            self.driver.close()
            assert False
        self.logger.info("*****end of login DDT ********")
        self.logger.info("********Completed TC Login Tc 002***********")
