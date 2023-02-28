import pytest

from model.contact import Contact
from fixture.application import Application


def test_add_contact(app):
    if app.group.groups_count() > 0 and app.group.check_group_name("group_name"):
        pass
    else:
        app.group.create(Group(name="group_name", header="group_header", footer="group_footer"))
    app.contact.create_contact(Contact(firstname="Jack", lastname="Daniels", nickname="JD", company="Whiskey",
                                       address="Scotland", home="999-999-99-99", work="777-777-77-77",
                                       email="jd@test.com", group="group_name"))
