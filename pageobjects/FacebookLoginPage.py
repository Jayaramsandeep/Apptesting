from selenium import webdriver
class loginpage:

    textbox_username_id = "email"
    textbox_password_id = "pass"
    button_login_xpath = "login"
    link_logout_linktext = "//*[@id='mount_0_0_84']/div/div[1]/div/div[2]/div[4]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div[3]/div/div[4]/div/div[1]/div[2]/div/div/div/div/span"
    link_account_linktext = "//*[@id='mount_0_0_fD']/div/div[1]/div/div[2]/div[4]/div[1]/span/div/div[1]/i"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)


    def clicklogin(self):
        self.driver.find_element_by_name(self.button_login_xpath).click()

    def clickaccount(self):
        self.driver.find_element_by_xpath(self.link_account_linktext).click()


    def clicklogout(self):
        self.driver.find_element_by_xpath(self.link_logout_linktext).click()