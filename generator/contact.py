from model.contact import Contact
import random
import string
import jsonpickle
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "..\\data\\contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
                    email3=rand_sting(maxlength=10, case="emails"),
                    group="group_name"
                    )]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
