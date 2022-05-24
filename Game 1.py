import random

def gamewin(Computer,you):
    if Computer == you:
        return None
    elif Computer =='s':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif Computer =='w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif Computer =='g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Computer Turn:Snake(s) Water(w) or Gun(g)? ")
randno = random.randint(1,3)
if randno == 1:
    Computer ='s'
elif randno == 2:
    Computer ='w'
elif randno == 3:
    Computer ='g'

you =  input("Your Turn:Snake(s) Water(w) or Gun(g)? ")
a = gamewin(Computer,you)

print(f'Computer Chosse {Computer}')
print(f'You chose {you}')
if a == None:
    print("The game is tie")
elif a:
    print("you Game Win")
else:
    print("you lose")