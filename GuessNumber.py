import random


num = random.randint(0, 101)
guess = 0


print("Welcome to the guessing game!")
print("Im a guessing a number between 1 and 100.")

if input("Choose a difficulty. Type 'easy' or 'hard': ") == "easy":
    guess = 10
elif input("Choose a difficulty. Type 'easy' or 'hard': ") == "hard":
    guess = 5

win = False
while guess != 0:
    ans = int(input("Make a guess:"))

    if ans < num:
        guess -= 1
        print("Too low:")
    elif ans > num:
        guess -= 1
        print("Too high")
    elif ans == num:
        print("You win!")
        break
    elif guess == 0:
        print("No more guess!")
        break
    
