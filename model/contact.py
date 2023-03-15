from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, nickname=None, company=None, address=None, home=None, mobile = None,
                 work=None, email=None, group=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.email = email
        self.group = group
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def return_id_or_maxsize(cont):
        if cont.id:
            return int(cont.id)
        else:
            return maxsize