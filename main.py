#Importing time
import time

#introducing the quizz

print ("Welcome to the quiz for year 9's! ")
time.sleep (0.5)
name = input ("what is your name? ")
time.sleep (0.5)
print ("hello" ,name, "!")
#create 2 list of questions and answers
questions = [
  "what is the appropriate color of shoes you should wear?",
  "What day is the shortest school day?",
  "what color is rutherford?",
  "How many houses are in Rangiora High School?",
  "Where do you usally do ako?",
  "how many blocks in this school are 2 stories?",
  "what classes are usally in s2?",
  "How many terms are there in a school year?",
  "What subject is usally in C-Block?",
  "what classes are mainly in G-Block",

]
answers = [
  "Black",
  "Wednesday",
  "Blue",
  "6",
  "Rakahuri",
  "3",
  "Health",
  "4",
  "Maths",
  "English",
]
#set score to 0

score = 0


# Loop through each question
for i in range(len(questions)):
    # Ask the current question
    print("\nQuestion", i + 1)
    time.sleep(0.5)
    answer = input(questions[i] + ": ")
    
    # Check the answer
    if answer.lower() == answers[i].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect.") 
    time.sleep(0.5)
#print finale message
print("\nYour score is:",score, "out of",len(questions))
