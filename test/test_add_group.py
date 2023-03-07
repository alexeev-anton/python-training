import pytest

from model.group import Group
from fixture.application import Application


def test_add_group(app):
    group = Group(name="test", header="test", footer="test")
    before_groups_list = app.group.get_groups_list()
    app.group.create(group)
    after_groups_list = app.group.get_groups_list()
    assert len(before_groups_list) == len(after_groups_list) - 1
    before_groups_list.append(group)
    assert sorted(after_groups_list, key=Group.return_id_or_maxsize) == sorted(before_groups_list, key=Group.return_id_or_maxsize)
