import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
human = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")  # human choose
random = random.randint(0, 2)  # computer choose
way = [rock, paper, scissors]
humanchoose = way[int(human)]
computerchoose = way[random]
print(f"you choose {humanchoose}.")
print(f"computer choose {computerchoose}.")
# comparison
if (int(human) == 0 and random == 2):
    print("you win")
elif (int(human) == 1 and random == 0):
    print("you win")
elif (int(human) == 2 and random == 1):
    print("you win")
elif (int(human) == random):
    print("Its an draw")
else:
    print("you lose")








