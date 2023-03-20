import pytest
import string
import random

from model.group import Group
from fixture.application import Application

def rand_sting(prefix, maxlength):
    symbols = string.ascii_letters + string.digits + (" " * 5)
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlength))])


testdata = [Group(name=rand_sting("name", 15),
                  header=rand_sting("header", 100),
                  footer=rand_sting("footer", 100))]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    before_groups_list = app.group.get_groups_list()
    app.group.create(group)
    assert len(before_groups_list) == app.group.groups_count() - 1
    after_groups_list = app.group.get_groups_list()
    before_groups_list.append(group)
    assert sorted(after_groups_list, key=Group.return_id_or_maxsize) == sorted(before_groups_list, key=Group.return_id_or_maxsize)
