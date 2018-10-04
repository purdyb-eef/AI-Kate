import util
from random import randint

punct = "?!,.;()#$%^&*"
greeting = ["hello","hi","howdy","sup"]
yes = ["yes","yeah","yea","sure","yup","mhm","ye","yuh"]
name = None

while True:
    u = input(": ")

    if u.lower() in greeting:
        util.delayPrint(["hello","hi"][randint(0,1)] + " there :')")
        print("")
        if name == None:
            util.pause(1.5)
            a = 0
            while a == 0:
                util.delayPrint("so")
                util.pause(0.08)
                util.delayPrint(".")
                util.pause(0.08)
                util.delayPrint(". ")
                util.pause(0.4)
                util.delayPrint("what's your name?")
                print("")
                name = input(": ")
                util.delayPrint(name)
                util.pause(0.08)
                util.delayPrint(".")
                util.pause(0.08)
                util.delayPrint(".")
                util.pause(0.08)
                util.delayPrint("?")
                print("")
                yn = input(": ")
                if yn.lower() in yes:
                    util.delayPrint("oh!")
                    util.pause(0.4)
                    util.delayPrint(" nice to meet you,")
                    util.pause(0.15)
                    util.delayPrint(" " + name)
                    print("")
                    a = 1

    if all(e in list(map(lambda b: b.strip(punct), u.split())) for e in ["my","name"]):
        if name != None:
            util.delayPrint(name + ", right?")
            print("")
        else:
            a = 0
            while a == 0:
                util.delayPrint("i, uh.. you never told me... ")
                util.pause(2)
                util.delayPrint("what's your name?")
                print("")
                name = input(": ")
                util.delayPrint(name + ".?")
                yn = input(": ")
                if yn.lower() in yes:
                    util.delayPrint("oh! nice to meet you, ")
                    util.pause(0.25)
                    util.delayPrint(name)
                    print("")
                    a = 1
