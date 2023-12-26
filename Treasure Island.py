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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''' )
print("Welcome To Treasure Island.")
print("Your mission is to find the treasure.")

left_or_right = input(
    "You'r at the cross road. Where do you want to go? Type"
    + ' "left"'
    + " or"
    + ' "right"\n'
)

if left_or_right.lower() == "left":
    swim_or_wait = input(
        "You come to a lake. There is an island in the middle of the lake. Type"
        + ' "wait"'
        + " to wait for a boat. Type"
        + ' "swim"'
        + " to swim across.\n"
    )
    if swim_or_wait.lower() == "wait":
        door = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n"
        )
        if door.lower() == "yellow":
            print("You Win!")
        elif door.lower() == "red":
            print("Burned by fire. Game Over.")
        elif door.lower() == "blue":
            print("Eaten by beasts. Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")

print("Thank you for playing.")
