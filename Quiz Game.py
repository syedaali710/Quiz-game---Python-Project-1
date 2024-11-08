print("Welcome to the Quiz Game")

Name = input("Enter Your Name here: ")

playing = input("Do you want to play this game? ")
if playing.lower() == "yes":
   print("Welcome on board")
   score = 0

if playing.lower() == "no":
    quit()

answer = input("what does cpu stands for? ")
if answer.lower() == "central processing unit":
    print("Its correct")
    score +=1
else:
        print("Its wrong")

answer2 = input("what does gpu stands for? ")
if answer2.lower() == "graphics processing unit":
    print("Its correct")
    score += 1
else:
        print("Its wrong")

answer3 = input("what does PSU stands for? ")
if answer3.lower() == "power supply unit":
    print("Its correct")
    score += 1
else:
        print("Its wrong")

print("You got " + str(score) + " questions correct!!")
print("You got " + str((score / 4)*100) + "%.")