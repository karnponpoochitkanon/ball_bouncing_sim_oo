import turtle
import random
import heapq
import math


class Ball:
    def __init__(self, size, x, y, vx, vy, color, id):
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.mass = 50 * size ** 2
        self.count = 0
        self.id = id
        self.canvas_width = turtle.screensize()[1]
        self.canvas_height = turtle.screensize()[0]

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y - self.size)
        turtle.pendown()
        turtle.color(self.color)  # กำหนดสีลูกบอล
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        # Bounce off walls
        margin = 50
        if self.x - self.size < -self.canvas_width + margin or self.x + self.size > self.canvas_width - margin:
            self.vx = -self.vx

        if self.y + self.size > self.canvas_height - margin:
            self.vy = -self.vy

    def bounce_off_paddle(self):
        self.vy = -self.vy

    def bounce_off_vertical_wall(self):
        self.vx = -self.vx

    def bounce_off_horizontal_wall(self):
        self.vy = -self.vy


class Paddle:
    def __init__(self, width, height, color, turtle_instance):
        self.width = width
        self.height = height
        self.location = [0, -250]
        self.color = color
        self.turtle_instance = turtle_instance

    def draw(self):
        self.turtle_instance.penup()
        self.turtle_instance.goto(self.location[0] - self.width / 2, self.location[1] - self.height / 2)
        self.turtle_instance.pendown()
        self.turtle_instance.color(self.color)
        self.turtle_instance.begin_fill()
        for _ in range(2):
            self.turtle_instance.forward(self.width)
            self.turtle_instance.left(90)
            self.turtle_instance.forward(self.height)
            self.turtle_instance.left(90)
        self.turtle_instance.end_fill()

    def move_left(self):
        self.location[0] -= 20

    def move_right(self):
        self.location[0] += 20


class Brick:
    def __init__(self, x, y, width, height, color, turtle_instance):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.visible = True
        self.turtle_instance = turtle_instance

    def draw(self):
        if not self.visible:
            return
        self.turtle_instance.penup()
        self.turtle_instance.goto(self.x - self.width / 2, self.y - self.height / 2)
        self.turtle_instance.fillcolor(self.color)
        self.turtle_instance.begin_fill()
        for _ in range(2):
            self.turtle_instance.forward(self.width)
            self.turtle_instance.left(90)
            self.turtle_instance.forward(self.height)
            self.turtle_instance.left(90)
        self.turtle_instance.end_fill()

    def hit_by_ball(self, ball):
        if not self.visible:
            return False
        return (self.x - self.width / 2 <= ball.x <= self.x + self.width / 2) and \
               (self.y - self.height / 2 <= ball.y <= self.y + self.height / 2)

    def destroy(self):
        self.visible = False


class BouncingSimulator:
    def __init__(self, num_balls):
        turtle.colormode(255)  # เปิดใช้งานโหมด RGB
        self.num_balls = num_balls
        self.ball_list = []
        self.bricks = []
        self.t = 0.0
        self.pq = []
        self.HZ = 60
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.canvas_width = turtle.screensize()[1]
        self.canvas_height = turtle.screensize()[0]

        # Screen setup
        self.screen = turtle.Screen()
        self.screen.bgcolor("gray55")
        self.screen.listen()

        # Create balls
        for i in range(self.num_balls):
            size = 10
            x = random.uniform(-self.canvas_width + size, self.canvas_width - size)
            y = random.uniform(-self.canvas_height + size, self.canvas_height / 2)
            vx = random.uniform(-200, 200)
            vy = random.uniform(-200, 200)
            color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            self.ball_list.append(Ball(size, x, y, vx, vy, color, i))

        # Create paddle
        paddle_turtle = turtle.Turtle()
        self.paddle = Paddle(150, 20, "blue", paddle_turtle)

        # Create bricks
        brick_turtle = turtle.Turtle()
        rows, cols = 3, 6
        brick_width = (2 * self.canvas_width - 100) / cols
        brick_height = 30
        start_x = -self.canvas_width + brick_width / 2 + 50
        start_y = self.canvas_height - brick_height / 2 - 50

        for row in range(rows):
            for col in range(cols):
                x = start_x + col * (brick_width + 10)
                y = start_y - row * (brick_height + 10)
                color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
                self.bricks.append(Brick(x, y, brick_width, brick_height, color, brick_turtle))

        # Paddle controls
        self.screen.onkeypress(self.paddle.move_left, "a")
        self.screen.onkeypress(self.paddle.move_right, "d")

    def draw(self):
        turtle.clear()
        for ball in self.ball_list:
            ball.draw()
        self.paddle.draw()
        for brick in self.bricks:
            brick.draw()
        turtle.update()

    def update(self, dt):
        for ball in self.ball_list:
            ball.move(dt)

            # Check collisions
            if ball.x - ball.size < -self.canvas_width or ball.x + ball.size > self.canvas_width:
                ball.bounce_off_vertical_wall()

            if ball.y + ball.size > self.canvas_height:
                ball.bounce_off_horizontal_wall()

            if self.paddle.location[0] - self.paddle.width / 2 <= ball.x <= self.paddle.location[0] + self.paddle.width / 2 and \
                    self.paddle.location[1] - self.paddle.height / 2 <= ball.y <= self.paddle.location[1] + self.paddle.height / 2:
                ball.bounce_off_paddle()

            for brick in self.bricks:
                if brick.visible and brick.hit_by_ball(ball):
                    brick.destroy()
                    ball.bounce_off_horizontal_wall()
                    break

    def run(self):
        import time
        last_time = time.time()

        while True:
            current_time = time.time()
            dt = current_time - last_time
            last_time = current_time

            self.update(dt)
            self.draw()

            if all(not brick.visible for brick in self.bricks):
                print("You Win!")
                break


# Run the simulation
num_balls = 1
my_simulator = BouncingSimulator(num_balls)
my_simulator.run()
