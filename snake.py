from turtle import Turtle
move_distance = 20

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    ### Creating a snake
    def create_snake(self):
        for position in range(0,3):
            self.add_square(position)

    def add_square(self, position):
        square = Turtle(shape="square")
        square.color("SlateBlue3")
        square.penup()
        self.snake.append(square)

    def reset(self):
        for segments in self.snake:
            segments.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def extend(self):
        self.add_square(self.snake[-1].position())

    ### Coordinating the movements of the snake
    def move(self):
        for square_num in range(len(self.snake) - 1,0,-1):
            new_x = self.snake[square_num - 1].xcor()
            new_y = self.snake[square_num - 1].ycor()
            self.snake[square_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    ### Characterizing the movements
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)