import pytest

from model.contact import Contact
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login("admin", "secret")
    app.create_contact(Contact(firstname="Jack", lastname="Daniels", nickname="JD", company="Whiskey",
                               address="Scotland", home="999-999-99-99", work="777-777-77-77",
                               email="jd@test.com"))
    app.logout()
