from model.group import Group


def test_edit_group_name(app):
    app.group.edit_group_create_if_missing(Group(name="group_name_updated"))


def test_edit_group_header(app):
    app.group.edit_group_create_if_missing(Group(header="group_header_updated"))
