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
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_elements(By.NAME, "selected[]")[index].click()
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_group_by_index(self, group, index):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_elements(By.NAME, "selected[]")[index].click()
        wd.find_element(By.NAME, "edit").click()
        self.fill_group_data(wd, group, "update")
        self.group_cache = None

    def edit_group_by_id(self, group, id):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()
        wd.find_element(By.NAME, "edit").click()
        self.fill_group_data(wd, group, "update")
        self.group_cache = None

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

    def check_group_name(self, group_name_to_check):
        wd = self.app.wd
        self.open_groups_page()
        rows_count = len(wd.find_elements(By.CLASS_NAME, 'group'))
        if rows_count > 0:
            group_names = []
            for i in range(rows_count):
                row_index = str(i + 1)
                group = wd.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[4]/form[1]/span[" + row_index + "]").text
                group_names.append(group)
            if group_name_to_check in group_names:
                return True


    group_cache = None

    def get_groups_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for i in wd.find_elements(By.CSS_SELECTOR, "span.group"):
                group_name = i.text
                group_id = i.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(id=group_id, name=group_name))
        return list(self.group_cache)
