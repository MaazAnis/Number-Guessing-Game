import random

print("Number Guessing Game")
print("Guess a number between 1-9")

s = random.randint(1,9)

chances = 0
while chances < 5:
    guess = int(input("Guess a number"))
    chances += 1
    if guess < s:
        print("Your Guess is too low")

    if guess > s:
        print("Your guess is too high")    
    
    if guess == s:
        break

if guess == s:
    print("You Guessed the correct number") 

else:
  print("You have guessed the wrong number")        

        