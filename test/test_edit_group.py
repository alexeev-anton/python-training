from model.group import Group


def test_edit_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group_create_if_missing(Group(name="group_name_updated"))
    app.session.logout()


def test_edit_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group_create_if_missing(Group(header="group_header_updated"))
    app.session.logout()
