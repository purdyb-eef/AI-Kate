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
                util.pause(0.1)
                util.delayPrint(".")
                util.pause(0.1)
                util.delayPrint(". ")
                util.pause(0.4)
                util.delayPrint("what's your name?")
                print("")
                name = input(": ")
                util.delayPrint(name)
                util.pause(0.1)
                util.delayPrint(".")
                util.pause(0.1)
                util.delayPrint(".")
                util.pause(0.1)
                util.delayPrint("?")
                print("")
                yn = input(": ")
                if yn.lower() in yes:
                    util.delayPrint("oh!")
                    util.pause(0.4)
                    util.delayPrint(" nice to meet you,")
                    util.pause(0.1)
                    util.delayPrint(" " + name)
                    print("")
                    a = 1

    if all(e in list(map(lambda b: b.strip(punct), u.split())) for e in ["my","name"]):
        if name != None:
            if randint(0,4) == 0:
                util.delayPrint("i forgot")
                util.pause(0.1)
                util.delayPrint(".")
                util.pause(0.1)
                util.delayPrint(".")
                util.pause(0.75)
                util.delayPrint(" what was the first letter again?")
                print("")

                z = 1
                while z == 1 or z == 5:
                    if z == 5:
                        util.pause(1)
                        util.delayPrint("what was the first letter?")
                        print("")
                    fLetter = input(": ")
                    if fLetter == name[0]:
                        util.delayPrint("oh")
                        util.pause(0.5)
                        util.delayPrint(".")
                        util.pause(0.5)
                        util.delayPrint(".")
                        util.pause(1)
                        util.delayPrint(" OH YEA!")
                        util.pause(0.25)
                        util.delayPrint(" the second letter is \"" + name[1] + "\,")
                        util.pause(0.15)
                        util.delayPrint(" right???")
                        print("")

                        d = 1
                        while d == 1 or d == 5:
                            if d == 5:
                                util.pause(1)
                                util.delayPrint("is the second letter \"" + name[1] + "\"?")
                                print("")
                            yn = input(": ")
                            if yn in yes:
                                util.delayPrint(name + "!")
                                util.pause(0.5)
                                util.delayPrint(" your name is " + name + "! ^^")
                                print("")
                                z = 2
                                d = 2
                            else:
                                util.delayPrint("who you gassing,")
                                util.pause(0.15)
                                util.delayPrint(" that's not how computers work")
                                print("")
                                d = 5
                    else:
                        util.delayPrint("nice try,")
                        util.pause(1)
                        print(" bub.")
                        z = 5
            else:
                util.delayPrint(name + "!")
                util.pause(1)
                util.delayPrint(" well at least that's what you told me > . >")
                print("")
        else:
            a = 0
            while a == 0:
                util.delayPrint("i,")
                util.pause(0.15)
                util.delayPrint(" uh")
                util.pause(0.1)
                util.delayPrint(".")
                util.pause(0.1)
                util.delayPrint(".")
                util.pause(0.4)
                util.delayPrint(" you never told me.")
                util.pause(1.2)
                util.delayPrint(" what's your name?")
                print("")
                name = input(": ")
                util.delayPrint(name)
                util.pause(0.1)
                util.delayPrint(".")
                util.pause(0.1)
                util.delayPrint(".")
                util.pause(0.1)
                util.delayPrint("?")
                print("")
                yn = input(": ")
                if yn.lower() in yes:
                    util.delayPrint("oh!")
                    util.pause(0.4)
                    util.delayPrint(" nice to meet you,")
                    util.pause(0.1)
                    util.delayPrint(" " + name)
                    print("")
                    a = 1
