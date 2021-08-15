from selenium import webdriver
from utilites.readproperties import ReadConfig
from utilites.customlogger import LogGen
from pageobjects.LoginPage import loginpage
from pageobjects.Addcustomer import Addcustomer
from pageobjects.SearchCustomer import SearchCustomer
import time
class Test_addCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    logger = LogGen.loggen()  # this import from utilites package

    def test_addcustomer(self, setup):

        self.logger.info("******************** Test_O1_Addcustomer ***************")
        self.logger.info("****************** Verifying Home Page Title **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()

        self.logger.info("****************** login succesful **********")
        self.logger.info("*********** Strating Add customer test *********")

        self.addcut = Addcustomer(self.driver)
        self.addcut.clickOncustomerMenu()
        self.addcut.clickOncustomerMenuitem()

        self.logger.info("***** searching customer by email id *****")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.ClickSearch()
        time.sleep(3)
        status = searchcust.searchCustomerByemail("victoria_victoria@nopCommerce.com")
        assert True==status
        self.logger.info("**** Test Finished *****")
        self.driver.close()