def game():
    f=int(input("Enter the number :"))
    return f

score=game()
with open("high_score.txt") as f:
    high_score = int(f.read())

if high_score<score:
    with open("high_score.txt","w") as f:
        f.write(str(score))
        


