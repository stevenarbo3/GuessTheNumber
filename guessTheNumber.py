import random as rand

def guess(x):
    rand_number = rand.randint(1,x)
    guess = 0
    while guess != rand_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        print(guess)
        if guess < rand_number:
            print("Try something greater than that")
        elif guess > rand_number:
            print("Try something less than that")
    
    print(f"Nice Job! You got it! {rand_number}")
        
guess(10)
        