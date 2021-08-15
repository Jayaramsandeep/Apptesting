import pytest
from pageobjects.LoginPage import loginpage
from pageobjects.Addcustomer import Addcustomer
from selenium import webdriver
from utilites.readproperties import ReadConfig
from utilites.customlogger import LogGen
import random
import string
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

        self.addcut.clickAddon()
        self.logger.info("******* Providing customer *******")
        self.email = random_generator() + ' @gmail.com '
        self.addcut.setEmail(self.email)
        self.addcut.setPassword("Test123")
        self.addcut.setfirstName("JaYaRam")
        self.addcut.setLastName("Sandeep")
        self.addcut.setGender("Male")
        self.addcut.setDateOfBirth("12/07/1995")
        self.addcut.setCompanyname("JSWS")
        self.addcut.setTax()
        self.addcut.setNewletter("Test store 2")
        self.addcut.setCustomerRoles("Guests")
        self.addcut.setManagerOfvendor("Vendor 2")
        self.addcut.setActive()
        self.addcut.setAdminContent("This is happy diwali force . misson launche by jayaramsandeep")
        self.addcut.clickOnSave()

        self.logger.info("******* Saving customer info")

        self.logger.info("******* Succeful ADD a new Customer")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("*************** Add Customer test is passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_login.png")
            self.logger.error("************ Add customer test is failed ***********")
            assert True == False

        self.driver.close()
        self.logger.info("****** Ending Home Page Title Test *******")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))