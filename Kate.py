import util
from random import randint

greeting = ["hello","hi","howdy","sup","salutations"]

while True:
    u = input(": ")
    if u.lower() in greeting:
        util.delayPrint(greeting[randint(0,4)])
    print("")
