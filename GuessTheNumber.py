

import random

# class Guess:
#     def __init__(self, x):
#         # Generate the secret number to guess
#         self.secret = random.randint(1, x)
    
#     def play(self):
#         guess = None
#         while guess != self.secret:
#             try:
#                 guess = int(input(f"Guess a number between 1 and {x}: "))
#             except ValueError:
#                 print("Please enter a valid integer.")
#                 continue

#             if guess < self.secret:
#                 print("Sorry, guess again. Too low.")
#             elif guess > self.secret:
#                 print("Sorry, guess again. Too high.")

#         print(f"Yay, congrats! You guessed the number {self.secret} correctly!!")

# if __name__ == "__main__":
#     x = 10  # or any upper limit you prefer
#     game = Guess(x)
#     game.play()

class Guess:
    def __init__(self, x):
        self.x = x

    def Play(self):
        low = 1
        high = self.x
        feedback = ''
        while feedback != 'c':
            if low != high:
                guess = random.randint(low, high)
            else:
                guess = low
            feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
            if feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1

        print(f'Yay! The computer guessed your number, {guess}, correctly!')

if __name__ == "__main__":
    x = 10  # or any upper limit you prefer
    game = Guess(x)
    game.Play()





