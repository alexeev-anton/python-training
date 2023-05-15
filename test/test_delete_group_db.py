from model.group import Group
import random


def test_delete_first_group_db(app, db, check_ui):
    group = Group(name="test", header="test", footer="test")
    if len(db.get_group_list()) == 0:
        app.group.create(group)
    before_groups_list = db.get_group_list()
    group = random.choice(before_groups_list)
    app.group.delete_group_by_id(group.id)
    after_groups_list = db.get_group_list()
    assert len(before_groups_list) - 1 == len(after_groups_list)
    before_groups_list.remove(group)
    assert before_groups_list == after_groups_list
    if check_ui:
        assert sorted(after_groups_list, key=Group.return_id_or_maxsize) == sorted(app.group.get_groups_list(), key=Group.return_id_or_maxsize)