import pytest

from model.group import Group
from fixture.application import Application


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group_create_if_missing(Group(name="test_updated", header="test_updated", footer="test_updated"))
    app.session.logout()
