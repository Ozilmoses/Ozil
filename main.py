import random
import time

class Aviator:
    def __init__(self):
        self.score = 0
        self.game_over = False

    def display_welcome(self):
        print("Welcome to the Aviator Game!")
        print("Try to reach the highest score!")

    def play(self):
        self.display_welcome()
        while not self.game_over:
            self.take_turn()
            time.sleep(1)
        print(f"Game Over! Your final score is: {self.score}")

    def take_turn(self):
        self.score += random.randint(1, 10)
        print(f"Current Score: {self.score}")
        self.check_game_over()

    def check_game_over(self):
        if self.score >= 100:
            self.game_over = True

if __name__ == '__main__':
    game = Aviator()
    game.play()