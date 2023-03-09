from model.group import Group


def test_edit_group_name(app):
    group = Group(name="test", header="test", footer="test")
    if app.group.groups_count() == 0:
        app.group.create(group)
    before_groups_list = app.group.get_groups_list()
    app.group.edit_group(Group(name="group_name_updated"))
    assert len(before_groups_list) == app.group.groups_count()
    after_groups_list = app.group.get_groups_list()
    before_groups_list[0].name = after_groups_list[0].name
    assert sorted(after_groups_list, key=Group.return_id_or_maxsize) == sorted(before_groups_list, key=Group.return_id_or_maxsize)