import random as rand

class GuessNumber:

    def generate(self, upperBound):
        return rand.randint(1,upperBound)
    
    def guess(self, upperBound):
        return int(input(f"Guess a number between 1 and {upperBound}: "))
        
    def checkGuess(self, upperBound):
        randNumber = self.generate(upperBound)
        guess = 0
        
        while (guess != randNumber):
            guess = self.guess(upperBound)
            if (guess > randNumber):
                print("Try lower")
            elif (guess < randNumber):
                print("Try higher")
        
        print("You got it!")
    
firstVersion = GuessNumber()
#firstVersion.randNumber = rand.randint(1,10)
firstVersion.checkGuess(10)

        