from model.contact import Contact
from model.group import Group
from random import randrange


def test_delete_contact(app):
    contact = Contact(firstname="Jack", lastname="Daniels", nickname="JD", company="Whiskey", address="Scotland",
                      home="999-999-99-99", work="777-777-77-77", email="jd@test.com", group="group_name")
    if app.contact.contacts_count() == 0:
        if not app.group.check_group_name("group_name"):
            app.group.create(Group(name="group_name", header="group_header", footer="group_footer"))
        app.contact.create_contact(contact)
    before_contacts_list = app.contact.get_contacts_list()
    index = randrange(app.contact.contacts_count())
    app.contact.delete_contact_by_index(index)
    after_contacts_list = app.contact.get_contacts_list()
    before_contacts_list[0:1] = []
    assert sorted(after_contacts_list, key=Contact.return_id_or_maxsize) == sorted(after_contacts_list, key=Contact.return_id_or_maxsize)
