# start the quiz off with a score of 0 in order to calculate the final score later

score = 0

# introduce the quiz
# ask the first question and introduce the options

print("""
Here is a quiz about aquatic life!

Question #1
What is the largest animal in the ocean?
A. Colossal Squid
B. Blue Whale
C. Whale Shark""")

# ask for the user's answer

answer1 = input("Choose an option! ")

# tell them if they're correct or incorrect
# if they were correct, add to their score
# if they're wrong, don't add anything to their score
if answer1 == "b" or answer1 == "B":
    print("Correct!")
    score = score + 1
else:
    print("Wrong, the answer is B.")

# repeat 4 more times with different questions

print("\nQuestion #2\nHow many hearts do octopus have?\nA. 3 hearts\nB. 6 hearts\nC. 9 hearts")
answer2 = input("Choose an option! ")
if answer2 == "a" or answer2 == "A":
    print("Correct!")
    score = score + 1
else:
    print("Wrong, the answer is A")

print("\nQuestion #3\nHow many brains do octopus have?\nA. 3 brains\nB. 6 brains\nC. 9 brains")
answer3 = input("Choose an option! ")
if answer3 == "c" or answer3 == "C":
    print("Correct!")
    score = score + 1
else:
    print("Wrong, the answer is C")

print("\nQuestion #4\nWhat is the largest FISH in the sea?\nA. Whale Shark\nB. Blue Whales\nC. Giant Manta Ray")
answer4 = input("Choose an option! ")
if answer4 == "a" or answer4 == "A":
    print("Correct!")
    score = score + 1
else:
    print("Wrong, the answer is A")

print("\nQuestion #5\nWhat percent of the ocean has been explored??\nA. 5%\nB. 10%\nC. 20%")
answer5 = input("Choose an option! ")
if answer5 == "a" or answer5 == "A":
    print("Correct!")
    score = score + 1
else:
    print("Wrong, the answer is A")

# ask them if they want their answer as a joke. Give it to them anyways if they say no
# don't add to the score because this question doesnt count
print("""
Final Question
Do you want to know your results?
A. Yes
B. No""")
answer6 = input("Choose an option! ")
if answer6 == "a" or answer6 == "A":
    print("Ok!")
else:
    print("Too bad! You get to know anyways!")

print(" ")
# divide their score by 5 (what the quiz is out of)
# multiply that by 100 in order to give them a percentage
score_percent = score
score_percent /= 5
score_percent *= 100

# print their score. if their score is higher than 50, they passed
# if its anything else, they failed
if score_percent > 50:
    print(f"You passed! Your score is {score_percent}% or {score}/5! Good job!")
else:
    print(f"Uh oh! Better luck next time. Your score is {score_percent}% or {score}/5")







