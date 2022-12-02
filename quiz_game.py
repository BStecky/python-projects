print("Welcome to 'the' quiz.")

playing = input("Do you want to play a game? ")

if playing.lower() != "yes":
    quit()

print("Okay lets play the game. ")
score = 0
answer = input("When did runescape release? ")
if answer == "2001":
    print("Correct")
    score += 1
else :
    print("Incorrect")

answer = input("What level do rune items require? ")
if answer == "40":
    print("Correct")
    score += 1
else :
    print("Incorrect")

answer = input("What quest do you slay the dragon named 'Elvarg'? ")
if answer.lower() == "dragon slayer":
    print("Correct")
    score +=1
else :
    print("Incorrect")

print("Your final score is: ", score)
print("Your percentage correct is: ", score/3 * 100)