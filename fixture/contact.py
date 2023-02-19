from selenium.webdriver.common.by import *

from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def init_contact_creation(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def create_contact(self, cont):
        wd = self.app.wd
        self.init_contact_creation()
        self.fill_contact_data(wd, cont, "submit")
        self.app.return_to_homepage()

    def edit_contact_create_if_missing(self, cont):
        wd = self.app.wd
        contacts_count = len(wd.find_elements(By.NAME, "selected[]"))
        if contacts_count == 0:
            self.create_contact(Contact(firstname="Jack", lastname="Daniels", nickname="JD", company="Whiskey",
                                        address="Scotland", home="999-999-99-99", work="777-777-77-77",
                                        email="jd@test.com"))

        wd.find_element(By.XPATH, "//img[@title='Edit']").click()
        self.fill_contact_data(wd, cont, "update")
        self.app.return_to_homepage()

    def fill_contact_data(self, wd, cont, flag):
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(cont.firstname)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(cont.lastname)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(cont.nickname)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(cont.company)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(cont.address)
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(cont.home)
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys(cont.work)
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(cont.email)
        if flag == "submit":
            wd.find_element(By.NAME, "submit").click()
        if flag == "update":
            wd.find_element(By.NAME, "update").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.XPATH, "// input[ @ value = 'Delete']").click()
        wd.switch_to.alert.accept()
        self.app.return_to_homepage()
