from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 260)
        self.color("white")
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
        self.penup()
        self.hideturtle()

    def display(self):  # method to display the score
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):  # method to increase the score
        self.clear()  # clears the screen
        self.score += 1   # increments score
        self.display()  # displays again the score
