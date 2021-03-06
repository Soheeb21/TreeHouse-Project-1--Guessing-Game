import random

def start_game():
    list_of_guesses = []
    correct_solution = False
    attempted_guesses = 0
    user_name = input("Hello, what is your name?    ")
    print("Hello, {} thank you for playing the Guessing Game, let's get started!".format(user_name))
    solution = random.randrange(1,10)
    while correct_solution == False:
        try:
            user_guess = input("Hello {}, please make a guess that is greater or equal to 1 but less than or equal to 10.   ".format(user_name))
            user_guess = int(user_guess)
            list_of_guesses.append(user_guess)
        except: 
            print("That is not a valid integer value, please try again")
        else:
            attempted_guesses += 1
            if user_guess > solution:
                print("It's lower")
            elif user_guess < solution:
                print("It's higher")
            elif user_guess == solution:
                print("Got it")
                correct_solution = True
                counter = 1
                if attempted_guesses != 1:
                    print("You took {} guesses to correctly guess the solution!".format(attempted_guesses))
                else:
                    print("You took {} guess to correctly guess the solution!".format(attempted_guesses))
                for guesses in list_of_guesses:
                    print("Guess #{} = {}".format(counter,guesses))
                    counter += 1
    print("Thank you for playing the Guessing Game, {}.".format(user_name))
start_game()