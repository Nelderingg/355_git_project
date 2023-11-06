print("Welcome to my computer quiz")

playing = input("Would you like to play a game? (y/n) ")

if playing.lower() != "y":
    quit()
print("live or die, the choice is yours")
score = 0

answer = input("what does CPU stand for? ")
if answer == "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("what does GPU stand for? ")
if answer == "graphics processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("what does RAM stand for? ")
if answer == "random access memory":
    print("correct")
    score += 1
else:
    print("incorrect")

answer = input("what does PSU stand for? ")
if answer == "power supply":
    print("correct")
    score += 1
else:
    print("incorrect")

print("you got " + str(score) + " questions correct")
print("you got " + (str(score / 4) * 100) + " questions correct")
