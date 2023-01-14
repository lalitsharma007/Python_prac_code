import random
def game_win(comp,you):
    if comp==you:
        return  None
    elif comp=='r':
        if you=="s":
            return False
        elif you=='p':
            return True
    elif comp=='p':
        if you=="r":
            return False
        elif you=='s':
            return True
    elif comp=='s':
        if you=="p":
            return False
        elif you=='r':
            return True
    

print("Comp Turn: rock(r) paper(p) scissors(s)")
random_no=random.randint(1,3)
if random_no==1:
    comp='r'
elif random_no==2:
    comp='p'
elif random_no==3:
    comp='s'
you=input("Your turn:rock(r) paper(p) scissors(s)")
a=game_win(comp,you)

print(f"Computer chose: {comp}")
print(f"You chose: {you}")

if a==None:
    print("The game is tie!!!!")
elif a:
    print("You win!!!")
else:
    print("You loose the game!!!!!")



