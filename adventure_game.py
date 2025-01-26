import random
import time


def print_pause(message):
    print(message)
    time.sleep(2)


def intro(monster):
    time.sleep(2)
    print_pause("You find yourself standing in an open"
                " field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a "
                + monster + " is somewhere around here,")
    print_pause("and has been terrifying the nearby village.")
    print_pause("In front of you is a HOUSE.")
    print_pause("To your right is a dark CAVE.")
    print_pause("In your hand you hold your trusty"
                " (but not very effective) dagger.\n")


def field(items, monster):
    print_pause("What would you like to do?")
    print_pause("Enter 1 to knock on the door of the HOUSE.")
    print_pause("Enter 2 to peer into the CAVE.")
    response_field = input("(Please enter 1 or 2).\n")
    if response_field == "1":
        house(items, monster)
    elif response_field == "2":
        cave(items, monster)
    else:
        print_pause("Please, enter a VALID INPUT.")
        field(items, monster)


def house(items, monster):
    print_pause("You approach the door of the HOUSE.")
    print_pause("You are about to knock when the door opens"
                " and out steps a " + monster + "!")
    print_pause("Eep! This is the " + monster + "'S HOUSE!")
    print_pause("The " + monster + " ATTACKS YOU!")
    if "sword" not in items:
        print_pause("You feel a bit under-prepared for this,"
                    " what with only having a tiny dagger.")
    actions(items, monster)


def actions(items, monster):
    response_fight_or_run = input("Would you like to (1)Fight "
                                  "or (2)Run away?\n")
    if response_fight_or_run == "1":
        fight(items, monster)
    elif response_fight_or_run == "2":
        run_away(items, monster)
    else:
        print_pause("Please, enter a VALID INPUT")
        actions(items, monster)


def cave(items, monster):
    print_pause("You peer cautiously into the CAVE.")
    print_pause("It turns out to be only a very small cave.")
    if "sword" in items:
        print_pause("You've been here before, and gotten all"
                    " the good stuff. It's just an empty cave now.")
    else:
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical SWORD OF OGOROTH!")
        print_pause("You discard your silly old dagger and take "
                    "the sword with you.")
        items.append("sword")

    print_pause("You walk back out to the FIELD.\n")
    field(items, monster)


def fight(items, monster):
    if "sword" in items:
        print_pause("As the " + monster + " moves to attack,"
                    " you unsheath your new sword.")
        print_pause("The SWORD OF OGOROTH shines brightly in your hand"
                    " as you brace yourself for the attack.")
        print_pause("But the " + monster + " takes one look at your shiny"
                    " new toy and runs away!")
        print_pause("You have rid the town of the " + monster + ".")
        print_pause("YOU ARE VICTORIUS! :D ")
    else:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the " + monster + ".")
        print_pause("You have been defeated! :( ")

    print_pause("\nGAME OVER\n")
    play_again()


def run_away(items, monster):
    print_pause("You run back into the FIELD. Luckily, "
                "you don't seem to have been followed.\n")
    field(items, monster)


def play_again():
    response_play_again = input("Would you like to play again?"
                                " (y/n)\n").lower()
    if response_play_again == "y":
        print_pause("\nExcellent! \nRESTARTING THE GAME ...\n")
        start_game()
    elif response_play_again == "n":
        print_pause("Thanks for playing! ;) \nSee you next time.")
    else:
        print_pause("Please, enter a VALID INPUT.")
        play_again()


def start_game():
    characters = ["GOLUM", "TROLL", "DRAGON", "PIRATE", "VAMPIRE", "DEMON"]
    monster = random.choice(characters)
    items = []
    intro(monster)
    field(items, monster)


start_game()
