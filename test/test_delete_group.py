from model.group import Group


def test_delete_first_group(app):
    group = Group(name="test", header="test", footer="test")
    if app.group.groups_count() == 0:
        app.group.create(group)
    before_groups_list = app.group.get_groups_list()
    app.group.delete_first_group()
    after_groups_list = app.group.get_groups_list()
    assert len(before_groups_list) - 1 == len(after_groups_list)
    before_groups_list[0:1] = []
    assert sorted(after_groups_list, key=Group.return_id_or_maxsize) == sorted(before_groups_list, key=Group.return_id_or_maxsize)
