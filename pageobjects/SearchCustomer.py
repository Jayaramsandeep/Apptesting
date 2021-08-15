class SearchCustomer:

    email_xpath = "//*[@id='SearchEmail']"
    fname_xpath = "//*[@id='SearchFirstName']"
    lname_xpath = "//*[@id='SearchLastName']"
    btnSearch_id = "//*[@id='search-customers']"
    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//*[@id='customers-grid']"
    tableRows_xpath = "//*[@id='customers-grid']/tbody/tr"
    tableColumns_xpath = "//*[@id='customers-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver =  driver

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.email_xpath).clear()
        self.driver.find_element_by_xpath(self.email_xpath).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.fname_xpath).clear()
        self.driver.find_element_by_xpath(self.fname_xpath).send_keys(fname)

    def setLastname(self, lname):
        self.driver.find_element_by_xpath(self.fname_xpath).clear()
        self.driver.find_element_by_xpath(self.lname_xpath).send_keys(lname)

    def ClickSearch(self):
        self.driver.find_element_by_xpath(self.btnSearch_id).click()

    def getNoofRows(self):
        return len(self.driver.find_element_by_xpath(self.tableRows_xpath))

    def getNoofColumn(self):
        return len(self.driver.find_element_by_xpath(self.tableColumns_xpath))

    def searchCustomerByemail(self, email):
        flag = False
        for r in range(1,self.getNoofRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailid = table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
            return flag
    def searchCustomerByname(self, name):
        flag = False
        for r in range(1,self.getNoofRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            Name = table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if Name == name:
                flag = True
                break
            return flag










