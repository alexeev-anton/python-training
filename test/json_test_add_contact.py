from model.contact import Contact
from model.group import Group


def test_add_contact(app, json_contacts):
    contact = json_contacts
    if not app.group.check_group_name("group_name"):
        app.group.create(Group(name="group_name", header="group_header", footer="group_footer"))
    before_contacts_list = app.contact.get_contacts_list()
    app.contact.create_contact(contact)
    after_contacts_list = app.contact.get_contacts_list()
    before_contacts_list.append(contact)
    assert sorted(after_contacts_list, key=Contact.return_id_or_maxsize) == sorted(before_contacts_list, key=Contact.return_id_or_maxsize)