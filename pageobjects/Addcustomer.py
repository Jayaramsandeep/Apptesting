from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

class Addcustomer:

    #add customer page

    link_Customer_tag_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    link_TwoCustomer_tag_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    link_Add_Customer_xpath=  "/html/body/div[3]/div[1]/form[1]/div/div/a"

    link_Email_xpath = "//*[@id='Email']"
    link_Password_id = "Password"
    link_FirstName_id = "FirstName"
    link_LastName_id = "LastName"
    rdlink_gender_Male_id = "Gender_Male"
    rdlink_gender_Female_id = "Gender_Female"
    link_DateOfBirth_id = "DateOfBirth"
    link_Company_id = "Company"
    link_customerRole = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    list_Customer_rol_xpathadmi = "//*[@id='SelectedCustomerRoleIds']/option[1]"
    list_Customer_rol_xpathforum = "//*[@id='SelectedCustomerRoleIds']/option[2]"
    list_Customer_rol_xpathguest = "//*[@id='SelectedCustomerRoleIds']/option[3]"
    list_Customer_rol_xpathvend = "//*[@id='SelectedCustomerRoleIds']/option[4]"
    list_Customer_rol_xpathReg = "//*[@id='SelectedCustomerRoleIds']/option[4]"

    list_link_Vendor_xpath= "//*[@id='VendorId']"
    drpmg_link_vendor_xpath= " //*[@id='VendorId']/option[2]"
    content = "//*[@id='AdminComment']"
    tax = "//*[@id='IsTaxExempt']"
    link_newsletter = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"
    rdpnewsletter = "SelectedNewsletterSubscriptionStoreIds_taglist"
    rdpnews2 = "SelectedNewsletterSubscriptionStoreIds_taglist"
    link_Save = "/html/body/div[3]/div[1]/form/div[1]/div/button[1]"


    active = "//*[@id='Active']"


    def __init__(self, driver):
        self.driver = driver

    def clickOncustomerMenu(self):
        self.driver.find_element_by_xpath(self.link_Customer_tag_xpath).click()

    def clickOncustomerMenuitem(self):
        self.driver.find_element_by_xpath(self.link_TwoCustomer_tag_xpath).click()

    def clickAddon(self):
        self.driver.find_element_by_xpath(self.link_Add_Customer_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.link_Email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.link_Password_id).send_keys(password)

    def setNewletter(self, news):
        self.driver.find_element_by_xpath(self.link_newsletter).click()
        time.sleep(3)

        if news == 'Test store 2':
            self.list = self.driver.find_element_by_id(self.rdpnewsletter)
        elif news == 'Your store name':
            self.list = self.driver.find_element_by_id(self.rdpnews2)
        else:
            self.list = self.driver.find_element_by_id(self.rdpnewsletter)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.list)


    def setCustomerRoles(self, role):
        self.driver.find_element_by_id(self.link_customerRole).click()
        time.sleep(3)

        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.list_Customer_rol_xpathReg)

        elif role == 'Administration':
            self.listitem = self.driver.find_element_by_xpath(self.list_Customer_rol_xpathadmi)

        elif role == 'Guests':
            #here use the one option in both guests or registered
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.list_Customer_rol_xpathguest)

        elif role == 'Vendors':
            self.driver.find_element_by_xpath(self.list_Customer_rol_xpathvend)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.list_Customer_rol_xpathguest)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setTax(self):
        self.driver.find_element_by_xpath(self.tax).click()

    def setActive(self):
        self.driver.find_element_by_xpath(self.active).click()

    def setManagerOfvendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.list_link_Vendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rdlink_gender_Male_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.rdlink_gender_Female_id).click()
        else:
            self.driver.find_element_by_id(self.rdlink_gender_Male_id).click()

    def setfirstName(self, fname):
        self.driver.find_element_by_id(self.link_FirstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_id(self.link_LastName_id).send_keys(lname)

    def setDateOfBirth(self, dob):
        self.driver.find_element_by_id(self.link_DateOfBirth_id).send_keys(dob)

    def setCompanyname(self, comname):
        self.driver.find_element_by_id(self.link_Company_id).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element_by_id(self.content).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.link_Save).click()