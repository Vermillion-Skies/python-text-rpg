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
    part = str(x)
    print("")
    answer = str(input("Would you like to save the game? (y/n) ")) #Asks user to confirm the save
    if answer == str("y"):
        varlist =[str(chapter), str(part), str(name), str(health), str(maxhealth), str(money), str(strength), str(defense), str(wisdom), str(speed)] #Sets varlist to all variables needed for a save
        Scripts.savegame(varlist) #Calls savegame with the varlist as an argument
        pass
    else:
        pass
    if part ==str("1"):
        part1()
        pass
    elif part == str("2"):
        part2()
        pass
    elif part == str("3"):
        part3()
    else:
        Scripts.errorhandle("C11")
    pass
def part1(): #Function for the beginning character creation part of the game
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
    print("You are a wayward soul.")
    print("One without path, without purpose")
    print("A blank slate, both in past and in future")
    print("However, even a blank slate can be written upon, sculpted anew")
    print("And such a process begins with knowing Yourself")
    try:
        name = str(input("How shall the world know you? (enter your name) "))
    except Exception as e:
        Scripts.errorhandle("C12")
    print(name + "...")
    print("A name most uncommon in this world, and yet not an unwelcome one")
    print("Although, I could swear I've heard it before...")
    print("Ah, an unimportant detail")
    print("We shall now see how the world wishes to build you...")
    answer = str(input("(Press enter to roll your stats. It will only be done once.)"))
    try:
        strength = random.randint(1,20)
        defense = random.randint(1,20)
        wisdom = random.randint(1,20)
        speed = random.randint(1,20)
        maxhealth = random.randint(50,145)
        money = random.randint(0,300)
        health = maxhealth
    except Exception as e:
        Scripts.errorhandle("C13")
    print("")
    print("---===STATS ROLLED===---")
    print("HP:", maxhealth)
    print("STARTING CASH:", money)
    print("STR:", strength)
    print("DEF:", defense)
    print("WIS:", wisdom)
    print("SPD:", speed)
    print("----------------------------")
    print("")
    answer = str(input("(Press enter to continue)"))
    print("")
    print("Interesting... Most interesting...")
    print("It seems the stars above have a very specific path planned for you.")
    print("Until you reach the end of the path, try not to die")
    print("")
    print("*as the voice says this, you feel a light shining in front of you")
    answer = str(input("(Press enter to step towards this light)"))
    print("")
    print("*The light grows brighter as you step toward it. Every inch enveloping your body further in radiance.")
    print("*As you take one final step, you feel your vision go dark as you protect yourself from the beams of light")
    print("")
    answer = str(input("(Press enter to continue)"))
    part = 2
    chapter = 1
    makesave()
    part2()
    pass
def part2(): # Function for all logic of the first part of the first chapter of the game
    global name #sets many variables to be global, rather than locked to this function
    global maxhealth
    global health
    global money
    global strength
    global defense
    global wisdom
    global speed
    Scripts.screenclear()
    print("*When you finally come to, you slowly open your eyes")
    print("*You did not have eyes before, you don't believe you ever have")
    print("*Your eyes slowly adjust to the light, and you become aware of your surroundings")
    print("*You seem to be under a tree, leaning against it as your legs are crossed, and gently placed on top of the ground beneath you")
    print("*You aren't quite used to your body yet, and you find getting up to be a challenge for the moment. However, you managed to understand speech within this vessel quite fast")
    print("*You open your mouth to speak, and a voice escapes that you haven't heard before.")
    print("*It's not unpleasant, although there isn't anyone else around to confirm this.")
    print("*You speak softly to yourself, growing more used to this voice")
    print(name + ": ...suppose I could look around")
    print("")
    activeinput = 1
    inputcond1 = 0
    while activeinput == 1:
        print("1) Look left")
        print("2) Look right")
        print("3) Look to the sky")
        print("4) Stop looking and stand up")
        answer = str(input("Enter selection: "))
        if answer == str("1"):
            print("")
            print("----------")
            print("*As you look to your left, you see a large pond of sorts.")
            print("*Many animals are drinking from the pond, and wild flora seem to be growing plentifully around it's crystal blue waters.")
            print("*You can't quite explain it, but somehow this puts your mind at ease.")
            print("----------")
            print("")
            print("*You turn your head back to the ground beneath you, contemplating your next choice.")
            pass
        elif answer == str("2"):
            print("")
            print("----------")
            print("*To your right, you notice a sprawling forest of emerald green trees and bushes")
            print("*You can't quite see into it, but based on the outside it must be full of life")
            print("*As you admire it, you notice birds flying off from the trees, moving in a triangular formation")
            print("*And yet... something about it makes you shudder. But why?")
            print("----------")
            print("")
            print("*You turn your head back to the ground beneath you, contemplating your next choice.")
            pass
        elif answer == str("3"):
            if inputcond1 == 0:
                print("")
                print("----------")
                print("*You turn your head up to the sky, squinting your eyes as the sun shines upon you")
                print("*As the clouds slowly move to envelop the sun's light, your vision becomes clearer")
                print("*This moment of quiet contemplation clears your mind, you feel more wise!")
                wisdom = wisdom + int(1)
                inputcond1 = 1
                print("(Wisdom increased to", wisdom, "!)")
                print("----------")
                print("")
                print("*You turn your head back to the ground beneath you, contemplating your next choice.")
                pass
            elif inputcond1 == 1:
                print("")
                print("----------")
                print("*You stare into the clouds oncemore, but it seems rather unproductive")
                print("----------")
                print("")
                pass
            else:
                Scripts.errorhandle("C14")
            pass
        elif answer == str("4"):
            activeinput = 0
            pass
        else:
            print("Invalid input, please try again")
            pass
        pass
    print("")
    print("*As you stand up, you notice something ahead of you, something you're shocked you didn't notice before")
    print("*A small town, seemingly unpopulated and abandoned")
    print("*Just looking at it sends a chill down your spine as you wonder what could've happened there to leave it entirely void of life")
    print("*Just staring at it makes your skin feel cold and uncomfortable")
    print("*Just as the discomfort begins to subside, you suddenly feel something")
    print("")
    print("*A hand on your shoulder.")
    answer = str(input("(Press enter to continue)"))
    makesave(x) 
def part3():
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
    print("*As you register the hand that grabbed you, you can feel your heart racing uncontrollably")
    print("*However, you need to swallow your fear to face whatever creature awaits you...")
    activeinput = 1
    while activeinput == 1:
        print("1) Slowly turn your head")
        print("2) Ask the creature what it is without turning")
        print("3) (WIS) Analyze the hand")
        print("(required WIS: 6. Your WIS: ", wisdom, ")")
        answer = str(input("Make your choice"))
        if answer == str("1"):
            print("")
            print("----------")
            print("*Despite it all, your resolve remains firm")
            print("*Despite the fear in your heart, you turn your head to face whatever awaits you.")
            print("----------")
            print("")
            activeinput == 0
            pass
        elif answer == str("2"):
            print("")
            print("----------")
            print("*You slowly open your mouth, you can feel your lips quivering as you speak")
            print(name + ": Who or what are you?")
            print("*The creature stays silent for a moment, before you slowly hear their lips part")
            print("???: Bit of an odd question, don't you think?")
            print("???: I'm human, as I suspect you are, no?")
            print("*You aren't quite sure if you are human, or what you are. But the fact the individual claims some similarities to you puts you at ease")
            print("*As your guard lowers, you slowly turn your head to face them")
            print("----------")
            print("")
            activeinput == 0
            pass
        elif answer == str("3"):
            result = Scripts.statcheck(6, wisdom)
            if result == "Pass":
                print("")
                print("----------")
                print("*You take a close look at the hand")
                print("*While unfamiliar with this world, you can piece together that the hand looks slightly similar to your own")
                print("*Perhaps this individual is the same species as you, and such potentially friendly")
                print("*You decide you're likely safe to face them, and so you turn to do so")
                print("----------")
                print("")
                activeinput == 0
                pass
            elif result == "Fail":
                print("")
                print("----------")
                print("*You try to look at the hand, but you can't quite make out what it is")
                print("*Looking any further seems pointless.")
                print("----------")
                print("")
                pass
    print("")
    pass



Scripts.screenclear() #the initial game logic that runs at the start
varlist = Scripts.loadgame() #Loads variables from a save file to a local varlist
if varlist[0] == str("No"):
    part1()
else:
    if varlist[1] == str("2"):
        varinit() #Initializes all needed variables
        part2()