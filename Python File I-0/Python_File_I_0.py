import random

myfile = open("TextFile1.txt", "r")#open the file in read mode
print("Current scores in the file:")
lines = myfile.readlines() #read all lines from the file
myfile.close()

#Dr. Mo just wanted to say if you could explain this more in class since I didn't understand this as much as i should of
#and i felt like i was falling behind because of it. Hence all of the comments to see what everything does. Also if you could give us more of these
#to practice that would be great

#converts each line to a tuple of (score, name) and store them in a list
#strip = removes any leading, and trailing whitespaces. Leading means at the beginning of the string, trailing means at the end.
scores =[(int(line.split()[0]), line.split()[1].strip()) for line in lines]

#print the stuff in the list
for score, name in scores:
    print(score, " - ", name)

#insert game logic
score = 0

num = random.randrange(1, 201)
gameover = False

while gameover == False:

    player = int(input("Guess a number between 0 and 200: "))

    if player > num:
        print("Your answer is too high")
        score += 1

    elif player < num:
        print("Your answer is too low")
        score +=1

    else:
        print("Your answer is exactly right")
        score +=1
        gameover = True




#gets a new score from user the score is already gotten from the inputs of the user

name = input("Enter your name: ")

scores.append((score, name))
scores.sort(reverse=True)

while len(scores) > 10:
    scores.pop()

myfile = open("TextFile1.txt", "w") #write mode for text file
for score, name in scores:
    myfile.write(f"{score} {name}\n")
myfile.close() #closes file after writing