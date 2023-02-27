from selenium.webdriver.common.by import *
from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new")) > 0):
            wd.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element(By.NAME, "new").click()
        self.fill_group_data(wd, group, "submit")

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()

    def edit_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.NAME, "edit").click()
        self.fill_group_data(wd, group, "update")

    def fill_group_data(self, wd, group, flag):
        self.fill_field_value("group_name", group.name)
        self.fill_field_value("group_header", group.header)
        self.fill_field_value("group_footer", group.footer)
        if flag == "submit":
            wd.find_element(By.NAME, "submit").click()
        if flag == "update":
            wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()

    def fill_field_value(self, field_id, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element(By.NAME, field_id).click()
            wd.find_element(By.NAME, field_id).clear()
            wd.find_element(By.NAME, field_id).send_keys(value)

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def groups_count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements(By.NAME, "selected[]"))
