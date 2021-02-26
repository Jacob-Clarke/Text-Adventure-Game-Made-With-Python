directions = ["left", "right", "forward", "backward"]
inventory = []
possible_inventory1 = ["A Pistol", "A Sword", "An Axe"]

print("What is your name young warrior?")
name = input()
print("Hello "  + name,", you begin your adventure in a dark cave...")
print("Do you want to leave the cave?")
Answer1 = input()
if Answer1 == "yes" or "Yes":
    print("You leave the cave and move to the next step of your game!")
else:
    print("You can't figure out how to leave the cave and slowly die of starvation. In your last dying breath you express how hungry you are.")
    quit()

response = ""
while response not in directions:
    print("To your left, you see a bear.")
    print("To your right, there is a forest.")
    print("There is a rock wall directly in front of you.")
    print("Behind you is the forest exit.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print("The bear eats you. Farewell, " + name + ".")
        quit()
    elif response == "right":
        print("You head into the forest.\n")
    elif response == "forward":
        print("You cannot scale the wall.\n")
        response = "" 
    elif response == "backward":
        print("You leave the forest. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")
response = ""
while response not in possible_inventory1:
    print("Just as you realise that you need a weapon, you notice an array of weapons on the floor (You can only pick one up). There is...\n A Pistol,\n A Sword,\n An Axe")
    print("What do you choose?")
    response = input()
    if response == "A Pistol":
        print("You picked up " + response)
        inventory.append(response)
    elif response == "A Sword":
        print("You picked up " + response)
        inventory.append(response)
    elif response == "An Axe":
        print("You picked up " + response)
        inventory.append(response)
    else:
        print("I didn't understand that.\n")
        
    
