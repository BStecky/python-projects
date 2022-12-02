import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("please type a number larger than 0 you donut")
        quit()
else:
    print("Please type a number next time")

random_number = random.randint(0, top_of_range)
guesses = 0 

while True:
    user_guess = input("Please make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        guesses += 1
    else:
        print("Please type a number next time. ")
        continue
    
    if user_guess == random_number :
        print("You are a winner! The number was: ", random_number)
        break
    
    elif user_guess < random_number:
        print("Your guess is too small, try again! ")
        continue
    else:
        print("Your guess is too big, try again! ")
        continue

print("Congratulations, you have won the game, it took you ", guesses, " guesse(s) to break out of the loop!")

        