from model.contact import Contact


def test_edit_contact_all_fields(app):
    app.contact.edit_contact_create_if_missing(
        Contact(firstname="Jack_updated", lastname="Daniels_updated", nickname="JD_updated", company="Whiskey_updated",
                address="Scotland_updated", home="333-333-33-33", work="111-111-11-11",
                email="jd_updated@test.com"))


def test_edit_contact_name(app):
    app.contact.edit_contact_create_if_missing(
        Contact(firstname="Jack_updated"))