# Puts time inbetween messages for readabilty
import time
import climage

# i is for the while loop at the end
i = 0
# These are what set the # of fails when the user starts the program. It is always 0.
unique_fails = 0
total_fails = 0


# this function is what is supposed to count how many fails you get in total, and to count the fails you've never seen. has some bugs :/
def fail_increase():
    global unique_fails
    global total_fails

    if bank_enter() < 6:
        unique_fails = unique_fails + 1
        total_fails = total_fails + 1
    else:
        if unique_fails == "5":
            unique_fails = unique_fails + 0
            total_fails = total_fails + 1
        else:
            print("oh no theres an error")



# This massive function is the main code of the game, and is called in a while loop at the end.


images = [
    "sovell.jpg", "tmnt.jpg", "lazer.jpg", "teleplorter.jpg", "wrecker ball.jpg", "baggy.jpg"
]


def bank_enter():
    itemlist = [
        "(1.) Shovel  (2.) TNT  (3.) Laser  (4.) Teleporter  (5.) Wrecking Ball  (6.) Disguise"
    ]

    print(itemlist)

    bank_enter_choice = input()

    if bank_enter_choice == "1" or bank_enter_choice == "shovel":
        print(climage.convert(images[0]))
        print()
        print(
            "You dig directly down with the goal of digging a tunnel from where you started to the vault, but you hit a metal thing in the ground.\n"
        )
        time.sleep(1)
        print(
            "You take a small lighter to see what it was you hit and see the words 'GAS MAIN' written on it. Shortly, you and the hole you dug swiftly explodes.\n"
        )
        time.sleep(1)
        print("FAIL")
        print("Never dig down.\n")

        fail_increase()

        print("Unique fails: " + str(unique_fails))
        print("Total fails: " + str(total_fails))
        print()

    elif bank_enter_choice == "2" or bank_enter_choice == "tnt":
        print(climage.convert(images[1]))
        print()
        print(
            "You hook up ton of dynamite and TNT to the left side wall, and hide behind a nearby boulder. You push down on the plunger (yes thats what the push thing is called), but no explosion follows.\n"
        )
        time.sleep(1)
        print(
            "You go to get a closer look at the explosives, until they explode riiight next to you, presumably blowing up the entire area.\n"
        )
        time.sleep(1)
        print("FAIL")
        print("Handle with care.\n")

        fail_increase()

        print("Unique fails: " + str(unique_fails))
        print("Total fails: " + str(total_fails))
        print()

    elif bank_enter_choice == "3" or bank_enter_choice == "laser":
        print(climage.convert(images[2]))
        print()
        print("You use a huge laser cutter to cut a hole in the wall. Nice!\n")
        time.sleep(1)
        print("But then said cut out portion falls you, smushing you instantly.\n")
        time.sleep(1)
        print("FAIL")
        print("Open Sesame.\n")

        fail_increase()

        print("Unique fails: " + str(unique_fails))
        print("Total fails: " + str(total_fails))
        print()

    elif bank_enter_choice == "4" or bank_enter_choice == "teleporter":
        print(climage.convert(images[3]))
        print()
        print(
            "You pull out a mysterious device and press a few buttons on it, and teleport...\n"
        )
        time.sleep(1)
        print("Into the wall. You are now stuck in a bank wall.\n")
        time.sleep(1)
        print("FAIL")
        print("It's emergent technology, i'm sure it will get better!\n")

        fail_increase()

        print("Unique fails: " + str(unique_fails))
        print("Total fails: " + str(total_fails))
        print()

    elif bank_enter_choice == "5" or bank_enter_choice == "wrecking ball":
        print(climage.convert(images[4]))
        print()
        print(
            "You drive an large wrecking ball to the side of the bank, but you hear a whistle from one of the guards, who points to the back of you.\n"
        )
        time.sleep(1)
        print("You back up, away from the bank.\n")
        time.sleep(1)
        print("FAIL")
        print("There's no construction planned for today.\n")

        fail_increase()

        print("Unique fails: " + str(unique_fails))
        print("Total fails: " + str(total_fails))
        print()

    elif bank_enter_choice == "6" or bank_enter_choice == "diguise":
        print(climage.convert(images[5]))
        print()
        print(
            "You find a bag that looks *just* like a other bags of money they have at the vault, and get in. You also manage to tie the knot from the outside... somehow.\n"
        )
        time.sleep(2)
        print(
            "You hear a truck come by, and then shortly stop. You hear footsteps, then voices.\n"
        )
        time.sleep(2)
        print(
            "'How did we lose one?' 'I think we should put it in the car, just to be safe?'\n"
        )
        time.sleep(2)
        print(
            "You are then lugged into a truck full of money bags. You hear driving for a solid amount of time before your once again thrown somwhere.\n"
        )
        time.sleep(2)
        print(
            "You open the bag from the inside *somehow* and lift your fist up in vitory, only to trigger a security laser, and are caught by the guards nearly immediately."
        )
        time.sleep(2)
        print("erm... game over(?)")

        quit()

    else:
        print(
            "You couldn't figure out how to break in and got caught by a nearby guard.")
        quit()


# ----------------------SEPERATION OF FUNCTION TO MAIN CODE-----------------------------#

# print(
#  "Thank you for playing this python recreation of Breaking the Bank! The original version is by PuffballsUnited and InnerSloth, do play the original version for the more authentic *and visual* experience!).\n"
# )
# time.sleep(3)
# print(
#  "Huge shoutout to the Henry Stickmin series for wanting me to get into video game development in the first place <3\n"
# )
# time.sleep(2)

print(
 "The scene starts with a view of a bank, out in the middle of a desert, with some guards in the front. The camera then pans over to you on the left side the bank.\n"
)
time.sleep(2)
print("How will you Break the Bank?\n")

# here is the while loop where the main code runs.
while i <= 5:
    bank_enter()
    i = i + 1
    fail_increase()
    if i <=5:
        fail_increase()
        print("You fail. Sad. :(")
    else:
        print("oh no there be an error")