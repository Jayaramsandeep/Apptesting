import pytest
from pageobjects.LoginPage import loginpage
from selenium import webdriver
from utilites.readproperties import ReadConfig
from utilites.customlogger import LogGen

class Test_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    logger = LogGen.loggen()  # this import from utilites package

    def test_homepageTitle(self, setup):

        self.logger.info("******************** Test_OO1_Login ***************")
        self.logger.info("****************** Verifying Home Page Title **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True

            self.logger.info("****************** Home Page Title passed **********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_homepageTitle.png")
            self.driver.close()
            self.logger.error("*********** test title is failed *********")
            assert False

    def test_login(self, setup):

        self.logger.info("******** Test_login *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title


        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("*************** test login title is passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_login.png")
            self.driver.close()
            self.logger.error("************ test login title is failed ***********")
            assert False
