import re


def test_add_contact(app):
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contacts_list_from_edit_page(0)
    assert contact_from_home_page.all_phones == merge_phones(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones(contact):
    return "\n".join(filter(lambda a: a != "", map(lambda b: clear(b), filter(lambda c: c is not None,
                                                                              [contact.home, contact.mobile, contact.work]))))
