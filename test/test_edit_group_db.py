from random import randrange
from model.group import Group


def test_edit_group_name_db(app, db, check_ui):
    group = Group(name="test", header="test", footer="test")
    if len(db.get_group_list()) == 0:
        app.group.create(group)
    before_groups_list = db.get_group_list()
    index = randrange(app.group.groups_count())
    group_updated = Group(name="group_name_updated")
    group.id = before_groups_list[index].id
    app.group.edit_group_by_id(group_updated, group.id)
    after_groups_list = db.get_group_list()
    assert len(before_groups_list) == len(after_groups_list)
    assert sorted(before_groups_list, key=Group.return_id_or_maxsize) == sorted(after_groups_list, key=Group.return_id_or_maxsize)
    if check_ui:
        assert sorted(after_groups_list, key=Group.return_id_or_maxsize) == sorted(app.group.get_groups_list(), key=Group.return_id_or_maxsize)