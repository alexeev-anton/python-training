from model.group import Group


def test_edit_group_name(app):
    if app.group.groups_count() == 0:
        app.group.create(Group(name="group_name", header="group_header", footer="group_footer"))
    before_groups_list = app.group.get_groups_list()
    app.group.edit_group(Group(name="group_name_updated"))
    after_groups_list = app.group.get_groups_list()
    assert len(before_groups_list) == len(after_groups_list)


def test_edit_group_header(app):
    if app.group.groups_count() == 0:
        app.group.create(Group(name="group_name", header="group_header", footer="group_footer"))
    app.group.edit_group(Group(header="group_header_updated"))
    before_groups_list = app.group.get_groups_list()
    after_groups_list = app.group.get_groups_list()
    assert len(before_groups_list) == len(after_groups_list)
