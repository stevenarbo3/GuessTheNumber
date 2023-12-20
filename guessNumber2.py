#inverse addition, computer guessing our number
import random as rand

class GuessNumber:

    def generate(self, lowerBound, upperBound):
        return rand.randint(lowerBound,upperBound)
    
    def pickNum(self, upperBound):
        return int(input(f"Pick a number between 1 and {upperBound}: "))
        
    def checkGuess(self,upperBound):
        number = self.pickNum(upperBound)
        guess = 0
        
        while (guess != number):
            if guess < number:
                lowerBound = guess + 1
            if guess > number:
                upperBound = guess - 1
                
            guess = self.generate(lowerBound,upperBound)
            
            difference = abs(guess - number)
            if difference != 0:
                print(f"Computer guessed {guess} and the number was {number}. The computer was {difference} off.")
        
        print("Computer got it!")
    
firstVersion = GuessNumber()
firstVersion.checkGuess(10)

        