import random

def choice(user,computer):
    if user == computer:
        print("Tie")
    elif user == "s" and computer == "w":
        print("Congrats You Won!")
    elif user == "s" and computer == "g":
        print("you loss!")
    elif user == "w" and computer == "s":
        print("you loss!")
    elif user == "w" and computer == "g":
        print("Congrats You Won!")
    elif user == "g" and computer == "w":
        print("you loss!")
    elif user == "g" and computer == "s":
        print("Congrats You Won!")



if __name__ == "__main__":


    while True:
        options = ["s","w","g"]
        user = input("Choose your options w for water s for snake and g for gun: ")
        computer = random.choice(options)

        choice(user,computer)

        choose = input("If you want to play again then type yes otherwise no: ")
        if choose == "no":
            break
