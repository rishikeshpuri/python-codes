import random
num=random.randint(1,100)
print('WELCOME TO GUESS ME!!')
print("I'M THINKING OF A NUMBER BETWEEN 1 TO 100")
print("if your guess is more than 10 away from my number, I will tell you your'r Cold")
print("if your guess is within 10 of my number i will tell you'r warm")
print("if your guess is farther than your most recent guess I'll say you are getting colder,")
print("if your guess is closer than your most recent guess, I'll say you are getting warmer")
print("LET'S PLAY THE GAME!!")

guesses=[0]
while True:
    guess=int(input("I'am thinking a number between 1 and 100. \n What is your number"))
    if guess<1 or guess>100:
        print("OUT of BOUNDS! Please try again:")
        continue
    if guess==num:
        print("CONGRATULATION,YOU GUESSED IT IN ONLY{} GUESSES!!".format(len(guesses)))
    guesses.append(guess)


