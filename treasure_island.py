print('''
*******************************************************************************
          |                   |                  |                     |
_________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
_________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
_________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input("You walk to a corridor and hear faint moaning coming down one of the halls\nWhich way would you like to go? Left or Right?\n")

if direction == "Left":
    print("You chose to go left and begin walking down the hallway,\n however you begin to hear a chreaking coming from beneath your feet.")
    swim = input("The floor colapses and you fall into the underground tunnel\n You have a choice of swimming across or waiting to be rescued.\n Swim or Wait?\n")
    
    if swim == "Wait":
        wait = input("A mysterious phantom arrives and guides you toward a secret room\n In this room there are 3 doors\n Red.\n Yellow.\n Blue.\n Choose which door you'd like to go through.\n")
        if wait == "Red":
            print("Burned by fire Game Over")
        elif wait == "Blue":
            print("Eaten by beasts. Game Over")
        elif wait == "Yellow":
            print('''
        _,-=._              /|_/|
        `-.}   `=._,.-=-._.,  @ @._,
            `._ _,-.   )      _,.-'
                `    G.m-"^m`m''')
        print("You have found room 621. YOU WIN!!")
    elif swim == "Swim":
        print("You suck at swimming and drowned. Game Over")
elif direction == "Right":
    print("You have stumbled upon Rainfurrest and were taken captive. Game Over.")