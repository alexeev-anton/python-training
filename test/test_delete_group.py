from model.group import Group


def test_delete_first_group(app):
    if app.group.groups_count() == 0:
        app.group.create(Group(name="group_name", header="group_header", footer="group_footer"))
    before_groups_list = app.group.get_groups_list()
    app.group.delete_first_group()
    after_groups_list = app.group.get_groups_list()
    assert len(before_groups_list) - 1 == len(after_groups_list)
