import random

print ("Howdy, Welcome to the passive aggresive Petie calculator, where our specialty is division!\n")

topNumber=input("First, insert a number to go into the numerator of your equation.\n")

btmNumber=input("Next, tell me the number you would like to put as the denominator.\n")

rndNum = random.randint(1,10)

print("\n")

if btmNumber == "0":
    value = random.randint(1,7)

if btmNumber == "0" and value == 7:
    print("Your answer is the same as " + str(int(topNumber)+int(rndNum)) +" divided by zero, Undefined." )
    
if btmNumber == "0" and value == 6:
    print("Wait, thats illegal!")
    
if btmNumber == "0" and value == 5:
    print("Wow, thats low, you think I like being reminded of what I can't do?\n")
    
if btmNumber == "0" and value == 4:
    print("Ok, that isnt funny!\n")
    
if btmNumber == "0" and value == 3:
    print("*Loud Calculator Screams*\n")
    
if btmNumber == "0" and value == 2:
    print("Try dividing yourself by zero and let's see what you get, go on, I'll wait...\n")
    
if btmNumber == "0" and value == 1:
    print("Hey, I like your enthusiasm but as great as I am I cant do that, sorry. Dividing by zero is kind of a no-go here.\n")


if btmNumber != "0":
    answer = int(topNumber)/int(btmNumber)
    print("\n")
    print("Answer: \n" + str(answer))
    
