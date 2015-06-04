import random
'''Guess a random number between 1 to 100 in 10 guesses'''
the_number = random.randint(1,100)
total_guesses = list()
allowed_guesses = 10

#since I increased the range, I may as well increase the chances


print("Hello, I would like to play a guessing game with you ")
print("Pick a number between 1 to 100 and I will tell you if you are correct. ")

while len(total_guesses) < allowed_guesses:
    answer = input("What is your number? ")

    try:
        player_answer = int(answer)
    except:
        print("That is not a whole number. ")
        break
    if not player_answer > 0 or not player_answer < 101:
        print("That number is not between 1 and 100. ")
            #I accidently put in 354 and it did not give me the error message?
        #I changed indents. Maybe that will fix it
        #Okay it did fix it, yay!
        break
    total_guesses.append(player_answer)

    if player_answer == the_number:
        print("You win! My number was {}! ".format(the_number))
        print("It took you {} tries. Good job! ".format(len(total_guesses)))
        break
    else:
        if player_answer > the_number:
            print("No, my number is lower than {}. Guess again! ".format(player_answer))
        else:
            print("No, my number is higher than {}. Guess again!".format(player_answer))
        continue
    
    
#It breaks the loop when I reach ten guesses. OK, I should have more faith in my instructors
    
            
