import random

items = []
menu = ['~~Menu~~', 'add - to add items to your list', 'list - to view list', 'randomize - to get a random item', 'menu - show this menu', 'quit - to quit']

def printMenu():
    for option in menu:
        print(option)
        
random.seed()
random.randint(1, 100)
random.randint(1, 100)
random.randint(1, 100)

running = True

print('RANDOMIZER!')
print('Change up the routine')
printMenu()
while(running):
    userInput = ''
    userInput = input('>> Make your selection now: ')
    if userInput == 'randomize':
        num = len(items)
        if (num > 1):
            num  = random.randint(1, num)
            print(items[num-1])
        else:
            print('Not enough items!')
    elif userInput == 'add':
        items.append(input('>> Item to add: '))
    elif userInput == 'list':
        for item in items:
            print(item)
    elif userInput == 'menu':
        printMenu()
    elif userInput == 'quit':
        running = False
    else:
        print('Command not recognized')
print('Program Exiting\nThank You')
