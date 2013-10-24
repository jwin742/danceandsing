## Joshua Winchester
## jwinchester6@gatech.edu
## I worked on this assignment alone and used course materials as wellas the following sites for music
## http://www.musicnotes.com/sheetmusic/mtdFPE.asp?ppn=MN0103571&ref=google
## http://www.phy.mtu.edu/~suits/notefreqs.html
## http://www.sandyn.com/play/OdetoJoyRec1.pdf

from Myro import *
init("sim")

def danceSing():
    waltz()
    odeToJoy()


def ode(z,c):
    odeList = [494,494,523,587,587,523,494,440,392,392,440,494]
    for note in odeList:
        beep(.5,note)
        #wait(.05)
    beep(.75,z)
    beep(.25,c)
    beep(1,c)

def odeToJoy():
    ode(494,440)
    ode(440,392)
    aList = [440,440,494,392,440,  494,392,440,   494,440,392,440,294,494]
    x = 0
    for note in aList:
        beep(.5,note)
        x = x +1
        #wait(.05)
        if x == 5 or x == 8:
            beep(.25,494)
            beep(.25,523)
    ode(440,392)

def waltz():
    r=0
    while r < 2:
        move(1,.5)
        wait(3.3)
        move(-1,.5)
        wait(3.3)
        stop()
        rotate(1,1.65)
        for time in timer(10):
            if time < 3 or time > 7:
                move(1,.25)
            else:
                move(1,-.3)
        stop()
        rotate(1,.75)
        r = r +1
        stop()


def bootyShake():
        #move 1
    n = 0
    while n <2:
        for time in timer(5):
            backward(1)
            move(0,.5)
            wait(.1)
            move(0,-.5)
            wait(.1)
        stop()
        #move 2
        move(1,.5)
        wait(1.25)
        backward(1,.5)
        move(1,.5)
        wait(1.25)
        move(-1,.5)
        wait(.8)
        stop()
        n = n+1

# move 3
    beep(.5, 800)
    r = 0
    while r <2:
        move(1,.5)
        wait(.75)
        move(-1,-.5)
        wait(.75)
        move(1,-.5)
        wait(.75)
        move(-1,.5)
        wait(.75)
        stop()
        r =r +1

def impMarch():
    time = [1,1,1,.75,.25,1,.75,.25,2,1,1,1,.75,.25,1,.75,.25,2]
    x= 0
    marchList = [392,392,392,311,466,392,311,466,392,   587,587,587,622,466,370,311,466,392]
    for note in marchList:
        length = time[x]
        beep(length,note)
        #wait(.05)
        x= x+1
    time2 = [1,.75,.25,1,.75,.25,.25,.25,.5,.5,.5,1,.75,.25,  .25,.25,.5,.5,.5,1,.75,.25,1,.75,.25,2]
    n = 0
    marchList2 = [784,392,392,784,740,698,659,622,659,000,415,554,523,493,   466,440,466,000,311,470,311,392,466,392,466,392]
    for note2 in marchList2:        
        length2 = time2[n]
        beep(length2,note2)
        #wait(.05)
        n = n+1

def menu():
    choices = ["Waltz", "Booty Shake", "Ode To Joy", "Imperial March"]
    num = 0
    while num <4:
        print( str(num + 1) + ". " + choices[num])
        num = num +1
    print("0. Exit")
    user = int(input("What song/dance do you want?"))
    if user == 1:
        waltz()
        menu()
    elif user == 2:
        bootyShake()
        menu()
    elif user == 3:
        odeToJoy()
        menu()
    elif user == 4:
        impMarch()
        menu()
    elif user == 0:
        print("Bye!!")
    else:
        print("Sorry I don't know that one")
        menu()