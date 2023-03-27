from model.group import Group
import random
import string
import jsonpickle
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "..\\data\\groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def rand_sting(prefix, maxlength):
    symbols = string.ascii_letters + string.digits + (" ")
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlength))])


testdata = [Group(name=rand_sting("name", 15),
                  header=rand_sting("header", 100),
                  footer=rand_sting("footer", 100))]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
