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
        self.fill_field_value("firstname", cont.firstname)
        self.fill_field_value("lastname", cont.lastname)
        self.fill_field_value("nickname", cont.nickname)
        self.fill_field_value("company", cont.company)
        self.fill_field_value("address", cont.address)
        self.fill_field_value("home", cont.home)
        self.fill_field_value("work", cont.work)
        self.fill_field_value("email", cont.email)
        if flag == "submit":
            wd.find_element(By.NAME, "submit").click()
        if flag == "update":
            wd.find_element(By.NAME, "update").click()

    def fill_field_value(self, field, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element(By.NAME, field).click()
            wd.find_element(By.NAME, field).clear()
            wd.find_element(By.NAME, field).send_keys(value)

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.XPATH, "// input[ @ value = 'Delete']").click()
        wd.switch_to.alert.accept()
        self.app.return_to_homepage()
