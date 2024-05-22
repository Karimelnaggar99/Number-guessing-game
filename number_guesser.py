import random

guesses=0
top_of_range=input("Type a number(upper limit):")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("pls type a number larger than zero")
        quit()
else:
    print("pls enter a number")
    quit()
random_number=random.randint(0,top_of_range)
# print(random_number)

while True:
    user_guess=input("Make a guess:")
    guesses+=1
    if user_guess.isdigit():
        user_guess=int(user_guess)
        
    else:
        print("pls enter a number")
        continue
    if user_guess==random_number:
        print("You guessed it right!")
        break
    elif user_guess>random_number:
        print("Go Lower!")
    else:
        print("Go Higher!")

print("you got it in",guesses,"guesses")
