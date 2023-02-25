import pytest

from model.group import Group
from fixture.application import Application


def test_add_group(app):
    app.group.create(Group(name="test", header="test", footer="test"))
