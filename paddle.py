class Paddle:
    def __init__(self, width, height, color, my_turtle):
        self.width = width * 0.5  # Reduce width by 50%
        self.height = height * 0.5  # Reduce the height by 50%
        self.location = [0, 0]
        self.color = color
        self.my_turtle = my_turtle
        self.my_turtle.penup()
        self.my_turtle.setheading(0)
        self.my_turtle.hideturtle()

    def set_location(self, location):
        self.location = location
        self.my_turtle.goto(self.location[0], self.location[1])

    def draw(self):
        self.my_turtle.color(self.color)
        self.my_turtle.penup()
    
        # Move to the top-left corner of the paddle
        self.my_turtle.goto(self.location[0] - self.width / 2, self.location[1] + self.height / 2)
        self.my_turtle.pendown()
        self.my_turtle.begin_fill()

        # Draw rounded rectangle
        corner_radius = min(self.width, self.height) / 5  # Set the radius of the curve
        for _ in range(2):  # Draw 2 sections on each side (1 curved corner + 1 straight side)
            self.my_turtle.forward(self.width - 2 * corner_radius)
            self.my_turtle.circle(corner_radius, 90)
            self.my_turtle.forward(self.height - 2 * corner_radius)
            self.my_turtle.circle(corner_radius, 90)

        self.my_turtle.end_fill()
        self.my_turtle.penup()

    def clear(self):
        self.my_turtle.clear()

    def __str__(self):
        return "paddle"
    
