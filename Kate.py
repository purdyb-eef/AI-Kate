import util
from random import randint

greeting = ["hello","hi","howdy","sup","salutations"]
yes = ["yes","yeah","yea","sure","yup","mhm"]
name = None

while True:
    u = input(": ")
    if u.lower() in greeting:
        util.delayPrint(greeting[randint(0,4)])
        print("")
        if name == None:
            a = 0
            while a == 0:
                util.delayPrint("what's your name?")
                name = input(": ")
                util.delayPrint(name + "?")
                yn = input(": ")
                if yn.lower() in yes:
                    util.delayPrint("nice to meet you, " name)
                    a = 1
    print("")
