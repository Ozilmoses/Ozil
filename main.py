import random
import time
import json
import os

class Aviator:
    def __init__(self):
        self.score = 0
        self.game_over = False
        self.high_scores_file = "high_scores.json"
        self.high_scores = self.load_high_scores()

    def load_high_scores(self):
        """Load high scores from file"""
        if os.path.exists(self.high_scores_file):
            try:
                with open(self.high_scores_file, "r") as f:
                    return json.load(f)
            except:
                return []
        return []

    def save_high_scores(self):
        """Save high scores to file"""
        with open(self.high_scores_file, "w") as f:
            json.dump(self.high_scores, f, indent=4)

    def add_high_score(self, score):
        """Add a new high score"""
        self.high_scores.append(score)
        self.high_scores.sort(reverse=True)
        self.high_scores = self.high_scores[:10]  # Keep top 10
        self.save_high_scores()

    def display_welcome(self):
        print("=" * 50)
        print("Welcome to the Aviator Game!")
        print("Try to reach the highest score!")
        print("=" * 50)
        self.display_high_scores()

    def display_high_scores(self):
        """Display top high scores"""
        print("\n🏆 TOP HIGH SCORES 🏆")
        if not self.high_scores:
            print("No high scores yet. Be the first!")
        else:
            for i, score in enumerate(self.high_scores[:5], 1):
                print(f"{i}. {score} points")
        print()

    def play(self):
        self.display_welcome()
        while not self.game_over:
            self.take_turn()
            time.sleep(1)
        
        print(f"\n{'=' * 50}")
        print(f"Game Over! Your final score is: {self.score}")
        
        # Check if it's a new high score
        if not self.high_scores or self.score > min(self.high_scores) or len(self.high_scores) < 10:
            self.add_high_score(self.score)
            print("🎉 NEW HIGH SCORE! 🎉")
        
        self.display_high_scores()
        print(f"{'=' * 50}\n")

    def take_turn(self):
        self.score += random.randint(1, 10)
        print(f"Current Score: {self.score}")
        self.check_game_over()

    def check_game_over(self):
        if self.score >= 100:
            self.game_over = True

if __name__ == '__main__':
    while True:
        game = Aviator()
        game.play()
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break