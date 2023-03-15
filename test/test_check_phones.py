import re


def test_add_contact(app):
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contacts_list_from_edit_page(0)
    assert contact_from_home_page.id == contact_from_edit_page.id
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.home == clear(contact_from_edit_page.home)
    assert contact_from_home_page.mobile == clear(contact_from_edit_page.mobile)
    assert contact_from_home_page.work == clear(contact_from_edit_page.work)


def clear(s):
    return re.sub("[() -]", "", s)
