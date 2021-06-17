import random
from random import randint
import sys
import time
import threading
import os
from playsound import playsound 
from colorama import init, Fore, Back, Style
from art import *
import winsound
import names
from random_word import RandomWords
r = RandomWords()
init(autoreset = True)

class Item:

    def __init__(self, name, description, amount, individual_value):
        self.name = name
        self.description = description
        self.amount = amount
        self.individual_value = individual_value

    @property
    def worth(self):
        return f'${self.amount * self.individual_value:.2f}'

    def sell(self):
        if self.amount >= 1:
            print('How many do you want to sell?')
            amt = int(input('amt > '))
            print(f'Are you sure you want to sell {self.amount} {self.name} for ${self.individual_value * amt:.2f}?')
            confirm = input('[y/n] > ')
            if confirm == 'y':
                self.amount -= amt
                print(f'{amt} {self.name} sold for ${amt * self.individual_value:.2f}!')

            else:
                pass

        pass

    def add_to_inventory(self, inventory):
        if len(inventory.items) < inventory.capacity:
            inventory.items.append(self)
            print(f'x{self.amount} {self.name} added to your Inventory')

        else:
            print('No room for more items...')

class Inventory:

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def show(self):
        index = 1
        for item in self.items:
            print(str(Fore.YELLOW + f'{index}. [x{item.amount}] {item.name} - {item.description}. Costs {item.individual_value:.2f} gold'))
            index += 1

    def drop_item(self):
        self.show()
        print("")
        i = int(input('Which item do you want to drop? ["0" to Quit]: '))
        if i == 0:
            print('\nClosing the Inventory...')
            mainmenu()

        item = self.items[i - 1]
        if item.amount == 1:
            amt = 1
            self.items.pop(i - 1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'\nItem {item.name}[x{amt}] Dropped!')

        else:
            print(f'You have {item.amount} of this, how many do you want to drop?')
            amt = int(input('amt > '))
            if item.amount <= 0:
                amt = 0
                self.items.pop(item)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'Item {item.name}[x{amt}] Dropped!')
            item.amount -= amt
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Item {item.name}[x{amt}] Dropped!')
        inventoryMenu()

    @property
    def total_worth(self):
        return f'\nThe inventory Total Worth is: ${sum([i.individual_value * i.amount for i in self.items]):.2f}'

# Declaring the Inventory
inventory = Inventory(6)

sword = Item('Sword', 'A rusty sword with inscriptions in an unfamiliar language...', 1, 125.24)
sword.add_to_inventory(inventory)

#Info
Name = ""
Gold = 0
Health = 0
Hunger = 0

#Skills
Crafting = 0
Athletics = 0
Read = 0
Artistic = 0
Charisma = 0
Dodge = 0
Medical = 0
Intellectual = 0
Social = 0
Clubs = 0
Archery = 0
Polearms  = 0
Blades = 0
Stealth = 0
Burglary = 0

#Bio
age = random.randint(14,30)
birthplace = "Birthplace: " + ["Barn, shed, or similar.","Small house.","Prison.","Home"][randint(0,3)]
childhood = f"Childhood: " + ["Everyone knew who you were, and you had friends everywhere you went.","You had a few close friends and lived an ordinary childhood."][randint(0,1)]
father = "Father: " + names.get_full_name(gender='male') + ", works as a  " + ["Butcher","Baker","Stonemason","Weaver","Winemaker","Mason","Farmer","Watchman","Shoemaker","Wheelwright","Locksmith","Grocer ","Armourer"][randint(0,11)] + ". Your relationship was " + ["friendly","indifferent"][randint(0,1)] + ". He is " + ["dead","alive"][randint(0,1)] + "."
family = "Family: " + ["You were raised by paternal or maternal grandparents.","You were raised by your mother.","You were raised by your father.","You were raised by your mother and father.","You were raised by adoptive family."][randint(0,4)]
mother = "Mother: " + names.get_full_name(gender='female') + ", works as a " + ["Butcher","Baker","Stonemason","Weaver","Winemaker","Mason","Farmer","Watchman","Shoemaker","Wheelwright","Locksmith","Grocer","Armourer"][randint(0,11)] + ". Your relationship was " + ["friendly","indifferent"][randint(0,1)] + ". She is " + ["dead","alive"][randint(0,1)] + "."

Slow_type_speed = 300 #Type speed

def info():
    print(Fore.WHITE + "||=Character info=||")
    print(Fore.GREEN + f"   Name: {Name}")
    print(Fore.YELLOW + f"   Gold: {Gold}")
    print(Fore.RED + f"   Health: {Health}/100")
    print(Fore.MAGENTA + f"   Hunger: {Hunger}/100")
    print(Fore.WHITE + "||================||")

def bio():
    print(Fore.WHITE + "||======Bio======||")
    print(Fore.YELLOW + f"   Name: {Name}")
    print(Fore.YELLOW + f"   Age: {age}")
    print(Fore.YELLOW + f"   {birthplace}")
    print(Fore.YELLOW + f"   {childhood}")
    print(Fore.YELLOW + f"   {father}")
    print(Fore.YELLOW + f"   {mother}")
    print(Fore.YELLOW + f"   {family}")
    print(Fore.WHITE + "||===============||")

def inventoryMenu():
    print("")
    inventory.show()
    print("")
    print(Fore.YELLOW + "0. Exit")
    print(Fore.YELLOW + "1. Drop item")
    print(Fore.WHITE + "Choose option: ", end=" ")
    menu = input()
    if menu == "0":
        os.system('cls' if os.name == 'nt' else 'clear')
        mainmenu()
    elif menu == "1":
        if not inventory.items:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.RED + "Inventory is empty")
            mainmenu()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            inventory.drop_item()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Back.RED + "Type 1-2")
        inventoryMenu()

def skills():
    print(Fore.WHITE + "||=====Skills=====||")
    if Crafting > 0:
        print(Fore.YELLOW + f"   Crafting: {Crafting}")
    if Athletics > 0:
        print(Fore.YELLOW + f"   Athletics: {Athletics}")
    if Read > 0:
        print(Fore.YELLOW + f"   Read: {Read}")
    if Artistic > 0:
        print(Fore.YELLOW + f"   Artistic: {Artistic}")
    if Charisma > 0:
        print(Fore.YELLOW + f"   Charisma: {Charisma}")
    if Dodge > 0:
        print(Fore.YELLOW + f"   Dodge: {Dodge}")
    if Medical > 0:
        print(Fore.YELLOW + f"   Medical: {Medical}")
    if Intellectual > 0:
        print(Fore.YELLOW + f"   Intellectual: {Intellectual}")
    if Clubs > 0:
        print(Fore.YELLOW + f"   Clubs: {Clubs}")
    if Archery > 0:
        print(Fore.YELLOW + f"   Archery: {Archery}")
    if Polearms > 0:
        print(Fore.YELLOW + f"   Polearms: {Polearms}")
    if Blades > 0:
        print(Fore.YELLOW + f"   Blades: {Blades}")
    if Stealth > 0:
        print(Fore.YELLOW + f"   Stealth: {Stealth}")
    if Burglary > 0:
        print(Fore.YELLOW + f"   Burglary: {Burglary}")
    print(Fore.BLACK + Back.WHITE + "(?) The learned skills will appear here.")
    print(Fore.WHITE + "||================||")

def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/Slow_type_speed)
    print('')


print('                                              [][][] /""\ [][][] ')
print('                                               |::| /____\ |::|  ')
print('                                               |[]|_|::::|_|[]|  ')
print('                                               |::::::__::::::|  ')
print('                                               |:::::/||\:::::|  ')
print('                                               |:#:::||||::#::|  ')
print('                                              #%*###&*##&*&#*&## ')
print('                                             ##%%*####*%%%###*%*#')
print('                            |===------------------------------------------------===|')
print("")
tprint('                                 408 RPG')
print('                            |===------------------------------------------------===|')
print('')
print(Fore.YELLOW + 'Hello traveler. Welcome to my game. It is a simple text based RPG. Ignore the mistakes in the text, the whole text is translated and cannot be completely corrected.')
print('')
sounds = "0"
while True:
    print(Fore.GREEN + "1. Yes")
    print(Fore.YELLOW + "2. No")
    print(Fore.CYAN + "3. Only sounds")
    print(Fore.WHITE + "Enable no copyright music and sounds?: ",end="")
    sounds = input()
    if sounds == "1":
        break
    elif sounds == "2":
        break
    else:
        print(Back.RED + "Type 1 or 2")
if sounds == "1":
    playsound("Sounds/1.mp3", False)
dif = ""
while True:
    print('')
    print(Fore.GREEN + "1. Really Easy")
    print(Fore.YELLOW + "2. Medium (RECOMMENDED)")
    print(Fore.RED + "3. Hard" + Fore.WHITE)
    print(Fore.BLACK + Back.WHITE + "(?) Your story, the beginning, the outcome of the battle and other parameters depend on it.")
    print(Fore.WHITE + "Choose your difficulty (1-3): ",end="")
    dif = input()
    if dif == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        slow_type("You wake up in the middle of the street. This is where your journey begins ...")
        break
    elif dif == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        slow_type("You wake up in the middle of the street. This is where your journey begins ...")
        break
    elif dif == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        slow_type("You wake up in the middle of the street. This is where your journey begins ...")
        break
    else:
        print(Back.RED + "Type 1,2 or 3")
print("")
slow_type("You don't remember your name")
print('')
print("What is the" + Fore.YELLOW + " name " + Fore.WHITE + "of your character:", end=' ')
Name = input()
print('')
if dif == "1":
    Gold = random.randint(600,1000)
    Crafting = 1
    Read = 3
    Charisma = 3
    Blades = 1
    Health = 100
    Hunger = 100
elif dif == "2":
    Gold = random.randint(200,450)
    Clubs = 1
    Crafting = 3
    Read = 1
    Health = 100
    Hunger = 100
elif dif == "3":
    Gold = random.randint(5,9)
    Hunger = 78
    Health = 62

def mainmenu():
    print("")
    print(Fore.YELLOW + "1. Character info")
    print(Fore.YELLOW + "2. Skills")
    print(Fore.YELLOW + "3. Backpack")
    print(Fore.YELLOW + "4. Go to ")
    print(Fore.YELLOW + "5. Travel (Map)")
    print(Fore.YELLOW + "6. Quests")
    print(Fore.YELLOW + "7. Biography")
    print(Fore.WHITE + "Choose option: ", end=" ")
    menu = input()
    if menu == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        info()
        mainmenu()
    elif menu == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        skills()
        mainmenu()
    elif menu == "3":
        if not inventory.items:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.RED + "Inventory is empty")
            mainmenu()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            inventoryMenu()
    elif menu == "7":
        os.system('cls' if os.name == 'nt' else 'clear')
        bio()
        mainmenu()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Back.RED + "Type 1-7")
        mainmenu()

info()
mainmenu()
        

def main():
    pass

if __name__ == "__main__":
    main()