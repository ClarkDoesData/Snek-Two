from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (0, -20), (0, -40)]

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def move(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment - 1].xcor()
            new_y = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(new_x, new_y)
        self.snake_head.forward(20)

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)

    def extend(self):
        # add a new segment  to the snake
        self.add_segment(self.snake_body[-1].position())

    def add_segment(self, positions):
        snake_part = Turtle("square")
        snake_part.penup()
        snake_part.goto(positions)
        snake_part.color("white")
        self.snake_body.append(snake_part)

    def reset(self):
        for segment in self.snake_body:
            segment.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()
        self.snake_head = self.snake_body[0]
