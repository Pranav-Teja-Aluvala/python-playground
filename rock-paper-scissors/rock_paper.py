def rock_paper_scissor(user):
    import random
    robot = random.choice(['rock','paper','scissor'])
    if user == robot:
        print("IT'S A TIE!\n>We both choose ",user)
        new()
    elif (user == 'rock' and robot == 'scissor') or (user == 'paper' and robot == 'rock') or (user == 'scissor' and robot == 'paper'):
        print(f"U WON!\n>By choosing {user} and i choose {robot}")
        return True   
    else:
        print(f"I WON!! \n>I choose {robot}.")
        new()

def new():
    print("**----------*----------***----------*----------**")
    another = input("No problem! Lets play Again!\n>Choose Rock/Paper/Scissor : ")
    rock_paper_scissor(another)

def greet():
    print("**----------*----------***----------*----------**")
    print("HI! Lets play Rock Paper Scissor! ")
    print()  

greet()
user = input("Choose Rock/Paper/scissor: ").lower()
won = rock_paper_scissor(user)
