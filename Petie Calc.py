import random
print ("Howdy, welcome to the Petie calculator, where the specialty is division!\n")
topNumber=input("First, insert a number to go into the numerator of your equation.\n")
btmNumber=input("Next, tell me the number you would like to put as the denominator.\n")
if btmNumber == "0": 
	value = random.randint(1,10)
	if value == "3":
		print("*Loud Calculator Screams*")
	if value == "2":
		print("Try dividing yopurself by zero and let's see what you get, go on, I'll wait...\n")
	if value == "1":
		print("Hey, I like your enthusiasm but as great as I am I cant do that, sorry. Dividing by zero is kind of a no-go here.\n")

	
if btmNumber != "0":
    answer = int(topNumber)/int(btmNumber)
    print("\n")
    print("Answer: \n" + str(answer))
