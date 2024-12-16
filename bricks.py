class Brick:
    def __init__(self, x, y, size, color, turtle_instance):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.turtle = turtle_instance
        self.is_active = True  # Bricks that can still be hit

    def draw(self):
        if not self.is_active:
            return  # Do not draw if the brick is destroyed.
        self.turtle.penup()
        self.turtle.goto(self.x - self.size / 2, self.y + self.size / 2)  # Start at the top left corner.
        self.turtle.pendown()
        self.turtle.color(self.color)
        self.turtle.begin_fill()
        for _ in range(4):
            self.turtle.forward(self.size)
            self.turtle.right(90)
        self.turtle.end_fill()

    def clear(self):
        self.turtle.clear()

    def check_collision(self, ball):
        if not self.is_active:
            return False  # Brick has been destroyed.
        # Check for ball collisions
        if (self.x - self.size / 2 <= ball.x <= self.x + self.size / 2 and
                self.y - self.size / 2 <= ball.y <= self.y + self.size / 2):
            self.is_active = False  # Change brick status
            return True
        return False
    
