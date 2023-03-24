from sys import maxsize


class Contact:
    def __init__(self, id=None, firstname=None, lastname=None, nickname=None, company=None, address=None, home=None, mobile = None,
                 work=None, email=None, email2=None, email3=None, group=None, all_phones=None, all_emails=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.group = group
        self.all_phones = all_phones
        self.all_emails = all_emails

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.nickname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def return_id_or_maxsize(cont):
        if cont.id:
            return int(cont.id)
        else:
            return maxsize