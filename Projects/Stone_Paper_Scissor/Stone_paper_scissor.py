import random 

def game_Win(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='p':
            return True
        elif you=='c':
            return False
    elif comp=='p':
        if you=='c':
            return True
        elif you=='s':
            return False
    elif comp=='c':
        if you=='s':
            return True
        elif you=='p':
            return False


print("Computer turn : Stone(s) Paper(p) Scissor(c)")
randomNo=random.randint(1,3)
print(randomNo)

if randomNo == 1:
    comp = 's'
elif randomNo == 2:
    comp = 'p'
elif randomNo == 3:
    comp = 'c'


you=input("Your turn : Stone(s) Paper(p) Scissor(c) \n")

a=game_Win(comp,you)
print("Computer Choose :",comp,"")
print("You choose :",you,"\n")

if a==None:
    print("Game is Tie\n")
elif a:
    print("Congratulations! **You Win**\n")
else:
    print("Don't loose Heart!!! You lose***\n")

