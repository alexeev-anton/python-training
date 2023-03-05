import pytest

from model.group import Group
from fixture.application import Application


def test_add_group(app):
    before_groups_list = app.group.get_groups_list()
    app.group.create(Group(name="test", header="test", footer="test"))
    after_groups_list = app.group.get_groups_list()
    assert len(before_groups_list) == len(after_groups_list) - 1
