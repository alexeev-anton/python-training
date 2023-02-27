from model.group import Group


def test_delete_first_group(app):
    if app.group.groups_count() == 0:
        app.group.create(Group(name="group_name", header="group_header", footer="group_footer"))
    app.group.delete_first_group()
