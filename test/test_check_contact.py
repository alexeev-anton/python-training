import re
from random import randrange


def test_check_contact(app):
    index = randrange(app.contact.contacts_count())
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contacts_list_from_edit_page(index)
    assert contact_from_home_page.id == contact_from_edit_page.id
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname

    assert contact_from_home_page.all_phones == merge_phones(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones(contact):
    return "\n".join(filter(lambda a: a != "", map(lambda b: clear(b), filter(lambda c: c is not None,
                                                                              [contact.home, contact.mobile, contact.work]))))
