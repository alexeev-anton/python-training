import pytest
import string
import random

from model.contact import Contact
from model.group import Group


def rand_sting(prefix=None, maxlength=None, case=None):
    symbols = string.ascii_letters + string.digits + (" ")
    digits = string.digits + ("-" * 3)
    letters = string.ascii_letters
    if case == "names":
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(3, maxlength))])
    if case == "phones":
        return "".join([random.choice(digits) for i in range(random.randrange(3, maxlength))])
    if case == "emails":
        random_email_part_before = "".join([random.choice(letters) for i in range(random.randrange(3, maxlength))])
        random_email_part_after = "".join([random.choice(letters) for i in range(random.randrange(3, maxlength))])
        domain = [".com", ".ru", ".info", ".biz"]
        return random_email_part_before + "@" + random_email_part_after + random.choice(domain)


testdata = [Contact(firstname=rand_sting("firstname", 50, "names"),
                    lastname=rand_sting("lastname", 50, "names"),
                    nickname=rand_sting("nickname", 50, "names"),
                    company=rand_sting("company", 50, "names"),
                    address=rand_sting("address", 50, "names"),
                    home=rand_sting(maxlength=30, case="phones"),
                    mobile=rand_sting(maxlength=30, case="phones"),
                    work=rand_sting(maxlength=30, case="phones"),
                    email=rand_sting(maxlength=10, case="emails"),
                    email2=rand_sting(maxlength=10, case="emails"),
                    email3=rand_sting(maxlength=10, case="emails")
                    )]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    if not app.group.check_group_name("group_name"):
        app.group.create(Group(name="group_name", header="group_header", footer="group_footer"))
    before_contacts_list = app.contact.get_contacts_list()
    app.contact.create_contact(contact)
    after_contacts_list = app.contact.get_contacts_list()
    before_contacts_list.append(contact)
    assert sorted(after_contacts_list, key=Contact.return_id_or_maxsize) == sorted(before_contacts_list, key=Contact.return_id_or_maxsize)
