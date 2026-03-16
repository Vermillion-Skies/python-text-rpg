import random #Imports the random library for use in stat calculations and rolls
import Scripts #Imports the custom script library
import os #Imports os for initial checks
def varinit(): #Initializes all variables to make sure they exist
    global chapter
    global part
    global name
    global health
    global maxhealth
    global money
    global strength
    global defense
    global wisdom
    global speed
    global varlist
    try:
        chapter, part, name, health, maxhealth, money, strength, defense, wisdom, speed = varlist
    except Exception as e:
        Scripts.errorhandle("C10")
    pass
def makesave(x): #Function to prep for saving, as well as advancing to the next chapter
    if x == 900: #Change this to whatever the final part in the chapter is
        part = str("1")
        chapter = str("3")
        pass
    else:
        part = str(x)
        chapter = str("2")
        pass
    print("")
    answer = str(input("Would you like to save the game? (y/n) ")) #Asks user to confirm the save
    if answer == str("y"):
        varlist =[str(chapter), str(part), str(name), str(health), str(maxhealth), str(money), str(strength), str(defense), str(wisdom), str(speed)] #Sets varlist to all variables needed for a save
        Scripts.savegame(varlist) #Calls savegame with the varlist as an argument
        pass
    else:
        pass
    if chapter == str("2"): #Add as many conditionals in here as needed (one per part)
        if part == str("1"):
            part1()
            pass
        else:
            Scripts.errorhandle("C11")
            pass
        pass
    elif chapter == str("3"):
        Scripts.loadchapter(str("3"))
    pass
def part1():
    global chapter #sets many variables to be global, rather than locked to this function
    global part
    global name 
    global health
    global maxhealth
    global money
    global strength
    global defense
    global wisdom
    global speed
    Scripts.screenclear()
    Scripts.sprint("Chapter Two is now in development.")
    Scripts.sprint("Check back later once it's actually complete and released!")
    answer = str(input("Please close the game"))
    pass
Scripts.screenclear() #the initial game logic that runs at the start
toload = Scripts.checkcache(0)
if toload ==str("y"):
    varlist = Scripts.loadgame() #Loads variables from a save file to a local varlist
    if varlist[0] == str("No"):
        part1()
    else:
        if varlist[1] == str("1"):
            varinit()
            part1()
            pass
        elif varlist[1] == str("2"):
            varinit() #Initializes all needed variables
            part2()
            pass
        elif varlist[1] == str("3"):
            varinit()
            part3()
            pass
        elif varlist[1] == str("4"):
            varinit()
            part4()
            pass
        elif varlist[1] == str("5"):
            varinit()
            part5()
            pass
elif toload == str("n"):
    part1()
