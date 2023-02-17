import pytest

from model.contact import Contact
from fixture.application import Application


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create_contact(Contact(firstname="Jack", lastname="Daniels", nickname="JD", company="Whiskey",
                                       address="Scotland", home="999-999-99-99", work="777-777-77-77",
                                       email="jd@test.com"))
    app.session.logout()
