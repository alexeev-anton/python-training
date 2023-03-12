from random import randrange

from model.group import Group


def test_edit_group_name(app):
    group = Group(name="test", header="test", footer="test")
    if app.group.groups_count() == 0:
        app.group.create(group)
    before_groups_list = app.group.get_groups_list()
    group_updated = Group(name="group_name_updated")
    index = randrange(app.group.groups_count())
    app.group.edit_group_by_index(group_updated, index)
    assert len(before_groups_list) == app.group.groups_count()
    after_groups_list = app.group.get_groups_list()
    before_groups_list[index].name = group_updated.name
    assert sorted(after_groups_list, key=Group.return_id_or_maxsize) == sorted(before_groups_list, key=Group.return_id_or_maxsize)