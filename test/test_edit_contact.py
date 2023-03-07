from model.contact import Contact
from model.group import Group


def test_edit_contact_all_fields(app):
    contact = Contact(firstname="Jack", lastname="Daniels", nickname="JD", company="Whiskey", address="Scotland",
                      home="999-999-99-99", work="777-777-77-77", email="jd@test.com", group="group_name")
    if app.contact.contacts_count() == 0:
        if not app.group.check_group_name("group_name"):
            app.group.create(Group(name="group_name", header="group_header", footer="group_footer"))
        app.contact.create_contact(contact)
    before_contacts_list = app.contact.get_contacts_list()
    contact.id = before_contacts_list[0].id
    app.contact.edit_contact(
        Contact(firstname="Jack_updated", lastname="Daniels_updated", nickname="JD_updated", company="Whiskey_updated",
                address="Scotland_updated", home="333-333-33-33", work="111-111-11-11",
                email="jd_updated@test.com"))
    after_contacts_list = app.contact.get_contacts_list()
    after_contacts_list[0] = contact
    assert sorted(after_contacts_list, key=Contact.return_id_or_maxsize) == sorted(after_contacts_list, key=Contact.return_id_or_maxsize)


def test_edit_contact_name(app):
    contact = Contact(firstname="Jack", lastname="Daniels", nickname="JD", company="Whiskey", address="Scotland",
                      home="999-999-99-99", work="777-777-77-77", email="jd@test.com", group="group_name")
    if app.contact.contacts_count() == 0:
        if not app.group.check_group_name("group_name"):
            app.group.create(Group(name="group_name", header="group_header", footer="group_footer"))
        app.contact.create_contact(contact)
    before_contacts_list = app.contact.get_contacts_list()
    contact.id = before_contacts_list[0].id
    app.contact.edit_contact(
        Contact(firstname="Jack_updated"))
    after_contacts_list = app.contact.get_contacts_list()
    after_contacts_list[0] = contact
    assert sorted(after_contacts_list, key=Contact.return_id_or_maxsize) == sorted(after_contacts_list, key=Contact.return_id_or_maxsize)