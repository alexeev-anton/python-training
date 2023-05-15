from model.group import Group


def test_group_list(app, db):
    ui_list = app.group.get_groups_list()
    print(ui_list)

    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.return_id_or_maxsize) == sorted(db_list, key=Group.return_id_or_maxsize)
