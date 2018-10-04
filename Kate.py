import util
from random import randint

punct = "?!,.;()#$%^&*"
greeting = ["hello","hi","howdy","sup","salutations","hello?"]
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
                    util.delayPrint("nice to meet you " + name)
                    a = 1

    if all(e in list(map(lambda b: b.strip(punct), u.split())) for e in ["my","name"]):
        if name != None:
            util.delayPrint(name + ", was it?")
        else:
            a = 0
            while a == 0:
                util.delayPrint("you never told me.")
                util.pause(1)
                util.delayPrint("what IS your name?")
                name = input(": ")
                util.delayPrint(name + "?")
                yn = input(": ")
                if yn.lower() in yes:
                    util.delayPrint("nice to meet you " + name)
                    a = 1
