from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("../../data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.sety(260)
        self.score = -1
        self.update_score()

    #updates the score everytime the snake hits the food
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Arial', 20, 'normal'))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("../../data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Arial', 20, 'normal'))