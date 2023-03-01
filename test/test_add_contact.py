from model.contact import Contact
from model.group import Group


def test_add_contact(app):
    if not app.group.check_group_name("group_name"):
        app.group.create(Group(name="group_name", header="group_header", footer="group_footer"))
    app.contact.create_contact(Contact(firstname="Jack", lastname="Daniels", nickname="JD", company="Whiskey",
                                       address="Scotland", home="999-999-99-99", work="777-777-77-77",
                                       email="jd@test.com", group="group_name"))
