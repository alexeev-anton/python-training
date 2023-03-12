from random import randrange

from model.group import Group


def test_delete_first_group(app):
    group = Group(name="test", header="test", footer="test")
    if app.group.groups_count() == 0:
        app.group.create(group)
    before_groups_list = app.group.get_groups_list()
    index = randrange(app.group.groups_count())
    app.group.delete_group_by_index(index)
    assert len(before_groups_list) - 1 == app.group.groups_count()
    after_groups_list = app.group.get_groups_list()
    before_groups_list[index:index + 1] = []
    assert sorted(after_groups_list, key=Group.return_id_or_maxsize) == sorted(before_groups_list, key=Group.return_id_or_maxsize)
