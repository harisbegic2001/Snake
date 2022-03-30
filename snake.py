from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake(Turtle):


    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()



    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)



    def move(self):
        for seg_num in range(len(self.segments)-1,0, -1):
            new_x = self.segments[seg_num-1].xcor();
            new_y = self.segments[seg_num-1].ycor();
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
        else:
            pass

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
        else:
            pass

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
        else:
            pass

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
        else:
            pass

    def eating(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.speed("fastest")
        self.segments.append(new_segment)