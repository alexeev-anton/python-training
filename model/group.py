from sys import maxsize


class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.id = id
        self.name = name
        self.header = header
        self.footer = footer

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and self.name == other.name)

    def return_id_or_maxsize(group):
        if group.id:
            return int(group.id)
        else:
            return maxsize
