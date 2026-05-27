# This program is for number guessing game

import random

all_smart_user_data = []

while True:
    
    computer_answer = random.randint(1, 20)

    guess_count = 0
    
    print("Hey, Dude! Welcome to number guessing game!")
    print("It is very exicting game! Don't be a buzzkill!")
    print("I know you always wanted to play this game like an idiot five years old kid who wants candy...")
    print("Now let's begin!")
    print("For guideness numbers are BTW 1 and 20! Be careful!")
        
    user_name = input("What's your name, brave one?\n")
        
    user_guess = (input("Okay... My lover, what is your guess?\n"))
        
    guess_count +=1


    while user_guess != computer_answer:
            
        if user_guess.isalpha():
                        
            print("Yeah... Very well... Another Dumbass")
            print("Do you even have brain or are you blind?")
            print("Well... A FACT that average of IQ in 'DUMBLAND' is 5 but you have less that...")
            print("Well, good for you dummy... Guinness can register you as (THE DUMBEST PERSON IN THE WORLD)! Congrats, bro!")
            print("I can't stand you... GET OUT!")
            break
            
        elif user_guess.isdigit():
            
            if int(user_guess) < 1 or int(user_guess) > 20:
                print("Hey dummy! It's BTW 1 to 20! LOOK:(BETWEEN 1 TO 20)! IF you are BLIND!")
                print("DumbBrain... A SHEEP has more IQ than you...")
                user_guess = input("Guess again empty brain:\n")
                guess_count += 1
                continue
            elif int(user_guess) < computer_answer:
                print("Nice Try! But mine is BIGGER!")
                user_guess = input("Guess again: ")
                guess_count += 1
                continue
            elif int(user_guess) > computer_answer:
                print("Good Guess! But mine is SMALLER!")
                user_guess = input("Guess again: ")
                guess_count += 1
                continue
            elif int(user_guess) == computer_answer:
                print("WOW! You hit the nail on the head, baby!")
                exit_game = input("So, Good game! Wanna continue?\n")
                if exit_game.lower() ==  "yes":
                    print("Alright! Let's continue!")
                    continue
                elif exit_game.lower() == "no":
                    print("You don't deserve...")
                    user_data = {
                        "name" : user_name,
                        "guess_count" : guess_count
                    }
                    all_smart_user_data.append(user_data)
                    break
                else:
                    print("😒😒😒")
                    user_data = {
                        "name" : user_name,
                        "guess_count" : guess_count
                    }
                    all_smart_user_data.append(user_data)
                    break
        else:
            print("What the hell is wrong with?")
            print("Are you out your brain?")
            print("In your head instead of brain is SLIPPERS!")
            print("GET OUT!")
            break
        break        
    exit_game2 = input("No one else want to play?\n")
    if exit_game2.lower() == "yes":
        print("Awesome! Let's play again!")
        continue
    elif exit_game2.lower() == "no":
        print("Featureless! Come and do something good for these dumbs...")
        break
    else:
        print("Not important, Knobhead! Go away!")
        break
        
print(all_smart_user_data)       