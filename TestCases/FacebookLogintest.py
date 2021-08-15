import pytest
from pageobjects.FacebookLoginPage import loginpage
from selenium import webdriver
from utilites.face import ReadConfig
from utilites.customlogger import LogGen
from utilites import Xlutilites
import time

class Test_Login_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = "C:\\Users\\Dell\\PycharmProjects\\Apptesting\\TestData\\LoginDataq.xlsx"

    logger = LogGen.loggen()  # this import from utilites package
    def test_login_ddt(self, setup):
        self.logger.info("************** Test_Login_002_DDT_Login ***********")
        self.logger.info("******** Test_login DDTest *********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = loginpage(self.driver)

        self.rows = Xlutilites.getRowCount(self.path,'Sheet1')
        print("Number of Rows i a Excel :", self.rows) # incase mistake raises

        lst_status = []  # empty list variable

        for r in range(2,self.rows+1):
            self.username = Xlutilites.readData(self.path, 'Sheet1', r, 1)
            self.password = Xlutilites.readData(self.path, 'Sheet1', r, 2)
            self.testing_result = Xlutilites.readData(self.path, 'Sheet1', r, 3)


            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)

            self.lp.clicklogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "(20+) Facebook"



            if act_title == exp_title:
                if self.testing_result == "pass":
                    self.logger.info("*** Test is passed ***")
                    self.lp.link_account_linktext();
                    self.lp.clicklogout();
                    lst_status.append("Pass")
                elif self.testing_result == "fail":
                    self.logger.info("*** Test is Failed ***")
                    self.lp.clicklogout();
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.testing_result == "pass":
                    self.logger.info("*** Failed ***")
                    lst_status.append("Fail")
                elif self.testing_result == "fail":
                    self.logger.info("*** Passed ***")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("**** Login Datadriven test Passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.info("******* Login Datadriven Test Failed ******")
            self.driver.close()
            assert False

        self.logger.info("**** END of Login DATA Driven Test *****")
        self.logger.info("**** Completed Test_Login_002_DDT_Login ****");


