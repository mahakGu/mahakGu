import random
while True:
    choices=["rock","paper","scissor"]
    computer =random.choice(choices)
    player = None
    while player not in choices:
         player =input("rock,paper, or scissor:").lower()
    if player==computer:
        print("Compuer:",computer)
        print("player:",player)
        print("Tie!")
    elif player=="rock":

      if computer=="paper":
            print("Computer:",computer)
            print("player:",player)
            print("you lose !!")
      if computer=="scissor":
           print("Computer:",computer)
           print("player:",player)
           print("you win !!")
    elif player=="scissor":

      if computer=="rock":
         print("Computer:",computer)
         print("player:",player)
         print("you lose !!")
      if computer=="paper":
        print("Computer:",computer)
        print("player:",player)
        print("you win !!")
    elif player=="paper":

      if computer=="scissor":
        print("Computer:",computer)
        print("player:",player)
        print("you lose !!")
      if computer=="rock":
        print("Computer:",computer)
        print("player:",player)
        print("you win !!")

    play_again=input("play again? (yes/no):").lower()
    if play_again!="yes":
      break
print("bye! ")
