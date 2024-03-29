import re
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
        self.open_contacts_page()
        self.init_contact_creation()
        self.fill_contact_data(wd, cont, "submit")
        self.app.return_to_homepage()
        self.contact_cache = None

    def edit_contact_by_index(self, cont, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements(By.XPATH, "//img[@title='Edit']")[index].click()
        self.fill_contact_data(wd, cont, "update")
        self.app.return_to_homepage()
        self.contact_cache = None

    def fill_contact_data(self, wd, cont, flag):
        self.fill_field_value("firstname", cont.firstname)
        self.fill_field_value("lastname", cont.lastname)
        self.fill_field_value("nickname", cont.nickname)
        self.fill_field_value("company", cont.company)
        self.fill_field_value("address", cont.address)
        self.fill_field_value("home", cont.home)
        self.fill_field_value("mobile", cont.mobile)
        self.fill_field_value("work", cont.work)
        self.fill_field_value("email", cont.email)
        self.fill_field_value("email2", cont.email2)
        self.fill_field_value("email3", cont.email3)
        self.select_selector_value("//select[@name='new_group']", cont.group)
        if flag == "submit":
            wd.find_element(By.NAME, "submit").click()
        if flag == "update":
            wd.find_element(By.NAME, "update").click()

    def fill_field_value(self, field_id, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element(By.NAME, field_id).click()
            wd.find_element(By.NAME, field_id).clear()
            wd.find_element(By.NAME, field_id).send_keys(value)

    def select_selector_value(self, selector_id, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element(By.XPATH, selector_id).send_keys(value)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements(By.NAME, "selected[]")[index].click()
        wd.find_element(By.XPATH, "// input[ @ value = 'Delete']").click()
        wd.switch_to.alert.accept()
        self.app.return_to_homepage()
        self.contact_cache = None

    def open_contacts_page(self):
        wd = self.app.wd
        if len(wd.find_elements(By.XPATH, "//img[@title='vCard']")) == 0:
            wd.find_element(By.XPATH, "//a[normalize-space()='home']").click()

    def contacts_count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for i in wd.find_elements(By.NAME, "entry"):
                contact_id = i.find_element(By.NAME, "selected[]").get_attribute("value")
                contact_firstname = i.find_element(By.XPATH, "./td[3]").text
                contact_lastname = i.find_element(By.XPATH, "./td[2]").text
                contact_address = i.find_element(By.XPATH, "./td[4]").text
                contact_allphones = i.find_element(By.XPATH, "./td[6]").text
                contact_allemails = i.find_element(By.XPATH, "./td[5]").text
                self.contact_cache.append(Contact(id=contact_id, firstname=contact_firstname, lastname=contact_lastname,
                                                  address=contact_address, all_phones=contact_allphones, all_emails=contact_allemails))
        return list(self.contact_cache)

    def get_contacts_list_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements(By.XPATH, "//img[@title='Edit']")[index].click()
        contact_id = wd.find_element(By.NAME, "id").get_attribute("value")
        contact_firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        contact_lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        contact_address = wd.find_element(By.NAME, "address").get_attribute("value")
        contact_home = wd.find_element(By.NAME, "home").get_attribute("value")
        contact_mobile = wd.find_element(By.NAME, "mobile").get_attribute("value")
        contact_work = wd.find_element(By.NAME, "work").get_attribute("value")
        contact_email = wd.find_element(By.NAME, "email").get_attribute("value")
        contact_email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        contact_email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        return Contact(id=contact_id, firstname=contact_firstname, lastname=contact_lastname,
                       address=contact_address, home=contact_home, mobile=contact_mobile, work=contact_work,
                       email=contact_email, email2=contact_email2, email3=contact_email3)