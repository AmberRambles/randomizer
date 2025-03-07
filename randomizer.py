import random

items = []
menu = ['~~Menu~~', 'autoDelete - toggles autoDelete (default on)', 'add - to add items to your list', 'add multiple - to add several items, separated by commas', 'delete - to remove items from your list', 'list - to view list', 'randomize - to get a random item', 'menu - show this menu', 'quit - to quit']

def printMenu():
    for option in menu:
        print(option)
        
random.seed()
random.randint(1, 100)
random.randint(1, 100)
random.randint(1, 100)

running = True
autoDelete = True
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
            if autoDelete:
                items.pop(num-1)
        else:
            print('Not enough items!')
    elif userInput == 'add':
        items.append(input('>> Item to add: '))
    elif userInput == 'add multiple':
        items.extend(input('>> Items to add (separate with commas): ').split(','))
    elif userInput == 'autoDelete':
        autoDelete = not autoDelete
        print(f'autoDelete is now {autoDelete}')
    elif userInput == 'list':
        for itemNum, item in enumerate(items):
            print(f'{itemNum}: {item}')
    elif userInput == 'delete':
        itemNum = int(input('>> Item number to delete: '))
        if itemNum < len(items):
            items.pop(itemNum)
        else:
            print('Invalid item number')
    elif userInput == 'menu':
        printMenu()
    elif userInput == 'quit':
        running = False
    else:
        print('Command not recognized')
print('Program Exiting\nThank You')
