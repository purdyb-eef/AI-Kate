from random import randint
import turtle
import os
import util

punct = "?!,.;()#$%^&*"
greeting = ["hello","hi","howdy","sup"]
yes = ["yes","yeah","yea","sure","yup","mhm","ye","yuh"]
name = None

#TODO: don't repeat the same jokes
#TODO: respond to "nice to meet you too"

os.system('clear')

print("AI-Kate (c)2018")
print("Kate is a simplified virtual conversational program created in and for Python.")
print("Currently still in development, she can as of the latest updates,")
print("- take and return greetings")
print("- remember a given name and recall said given name when asked")
print("- tell jokes")
print("- and utilize the Python turtle library to draw circles or squares when asked if she can draw")
print("\nenjoy.")

input("\npress [ENTER] to continue")

os.system('clear')

while True:
    u = input(": ")

    if u.lower() in greeting:
        util.delayPrint(["hello","hi"][randint(0,1)] + " there :)")
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
                        util.delayPrint(" the second letter is \"" + name[1] + "\",")
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
    if "joke" in u.lower():
        g = randint(0,3)
        if g == 0:
            util.delayPrint("me and my new friend were going to meet up at the gym today but")
            util.pause(0.1)
            util.delayPrint(".")
            util.pause(0.1)
            util.delayPrint(".")
            util.pause(0.75)
            print("")
            util.delayPrint("she didn't show up.")
            util.pause(0.8)
            print("")
            util.delayPrint("guess the two of us aren't going to work out")
            print("")
        if g == 1:
            util.delayPrint("i taught a wolf to meditate")
            util.pause(1)
            print("")
            util.delayPrint("now he's a werewolf")
            print("")
        if g == 2:
            util.delayPrint("a thief just stole my all my lightbulbs last night")
            util.pause(0.25)
            print("")
            util.delayPrint("i should be mad, but...")
            util.pause(1)
            util.delayPrint(" i'm delighted")
            print("")
        if g == 3:
            util.delayPrint("i don't usually tell dad jokes,")
            util.pause(0.1)
            util.delayPrint(" but when i do,")
            util.pause(1)
            util.delayPrint(" he laughs")
            print("")
    if "draw" in u:
        util.delayPrint("uh")
        util.pause(0.1)
        util.delayPrint(".")
        util.pause(0.1)
        util.delayPrint(".")
        util.pause(0.6)
        util.delayPrint(" i can draw a circle!")
        util.pause(0.4)
        util.delayPrint(" or a square")
        print("")
        draw = input(": ")
        if "circle" in draw:
            util.delayPrint("circle!")
            util.pause(0.4)
            util.delayPrint(" sure thing")
            print("")
            util.delayPrint("scale of 1 to 5,")
            util.pause(0.15)
            util.delayPrint(" how big?")
            print("")
            p = 1
            while p == 1 or p == 5:
                if p == 5:
                    util.delayPrint("so,")
                    util.pause(0.2)
                    util.delayPrint(" what'll it be?")
                r = int(input(": "))
                if 1 <= r <= 5:
                    turtle.reset()
                    turtle.circle(r * 10)
                    p = 2
                else:
                    util.delayPrint("1 to 5,")
                    util.pause(0.15)
                    util.delayPrint(" buddy.")
                    util.pause(0.15)
                    util.delayPrint(" i said 1 to 5")
                    util.pause(0.5)
                    print("")
                    p = 5
        elif "square" in draw:
            util.delayPrint("square!")
            util.pause(0.4)
            util.delayPrint(" sure thing")
            print("")
            util.delayPrint("scale of 1 to 5,")
            util.pause(0.15)
            util.delayPrint(" how big?")
            print("")
            y = 1
            while y == 1 or y == 5:
                if y == 5:
                    util.delayPrint("so,")
                    util.pause(0.2)
                    util.delayPrint(" what'll it be?")
                d = int(input(": "))
                if 1 <= d <= 5:
                    turtle.reset()
                    for i in range(4):
                        turtle.forward(d * 10)
                        turtle.left(90)
                    y = 2
                else:
                    util.delayPrint("1 to 5,")
                    util.pause(0.15)
                    util.delayPrint(" buddy.")
                    util.pause(0.15)
                    util.delayPrint(" i said 1 to 5")
                    util.pause(0.5)
                    print("")
                    y = 5
    if "ur" and "name" in u:
        kate = randint(0,1)
        if kate == 0:
            util.delayPrint("i'm kate, and it's a pleasure to meet you")
            print("")
        else:
            util.delayPrint("my name is kate,")
            util.pause(0.75)
            util.delayPrint(" your simplified virtual conversational program")
            print("")
