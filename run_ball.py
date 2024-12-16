import ball
import my_event
import turtle
import random
import heapq
import paddle
import math
import bricks
import tkinter as tk


class BouncingSimulator:
    def __init__(self, num_balls):
        self.num_balls = num_balls
        self.ball_list = []
        self.bricks = []  # Add bricks list
        self.t = 0.0
        self.pq = []
        self.HZ = 5
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        print(self.canvas_width, self.canvas_height)

        # Reduce the size of the ball by 75%
        ball_radius = 0.05 * self.canvas_width * 0.25  # Size 25% of original
        scale = 0.02  # Scale (1 meter = 20 pixels)
        speed = 250 * 1000 / 3600 * scale  # Constant speed 80 km/hr

        # Create a ball
        for i in range(self.num_balls):
            x = 0  # Starting position in the middle
            y = -250
            angle = random.uniform(0, 360)  # Random direction of movement
            vx = speed * math.cos(math.radians(angle))
            vy = speed * math.sin(math.radians(angle))
            ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.ball_list.append(ball.Ball(ball_radius, x, y, vx, vy, ball_color, i))

        # Add bricks with spaces
        brick_size = 50  # Size of each brick
        brick_rows = 2
        brick_cols = 5
        gap_x = 10  # The gap between bricks horizontally
        gap_y = 10  # Vertical gap between bricks
        brick_y_start = self.canvas_height * 0.3  # Starting y position
        tom = turtle.Turtle()
        for row in range(brick_rows):
            for col in range(brick_cols):
                x = (-brick_cols * (brick_size + gap_x) / 2 + col * (brick_size + gap_x) + brick_size / 2)
                y = brick_y_start - row * (brick_size + gap_y)
                self.bricks.append(bricks.Brick(x, y, brick_size, "blue", tom))

        # Create paddle
        self.my_paddle = paddle.Paddle(200, 50, (255, 0, 0), tom)
        paddle_y_position = -self.canvas_height + self.my_paddle.height / 2 + 20
        self.my_paddle.set_location([0, paddle_y_position])
        self.screen = turtle.Screen()

        # Create score
        self.score = 0  # Scoring variables
        self.score_turtle = turtle.Turtle()  # Turtle for displaying scores
        self.score_turtle.hideturtle()
        self.score_turtle.penup()
        self.score_turtle.color("black")
        self.update_score()  # Draw starting score

        self.lives = 1  # จำนวนชีวิตเริ่มต้น
        self.lives_turtle = turtle.Turtle()  # Turtle for drawing hearts
        self.lives_turtle.hideturtle()
        self.lives_turtle.penup()
        self.update_lives()  # Draw a starting heart

        # Create timer
        self.timer = 0.0  
        self.timer_turtle = turtle.Turtle() 
        self.timer_turtle.hideturtle()
        self.timer_turtle.penup()
        self.timer_turtle.color("black")

        self.screen = turtle.Screen()
        self.screen.bgcolor("#FFece8")  # Set background color outside the black box

    def update_lives(self):
        self.lives_turtle.clear()
        x_start = self.canvas_width - 20  # Start at the far right corner.
        y_position = self.canvas_height - 40
        for i in range(self.lives):
            self.lives_turtle.goto(x_start - i * 30, y_position)  # Position each heart
            self.lives_turtle.color("red")  # Set color to red
            self.lives_turtle.write("❤️", align="center", font=("Arial", 16, "normal"))

    def update_timer(self):
        self.timer_turtle.clear()
        self.timer_turtle.goto(0, self.canvas_height + 30)  # Position at the top-center of the screen
        self.timer_turtle.write(f"Timer: {self.timer:.1f} ss", align="center", font=("Arial", 16, "normal"))

    def display_win_message(self):
        self.score_turtle.goto(0, self.canvas_height - 40)  # Top center position
        self.score_turtle.color("red")
        self.score_turtle.write("You Win!", align="center", font=("Arial", 16, "normal"))

    # updates priority queue with all new events for a_ball
    def __predict(self, a_ball):
        if a_ball is None:
            return

        # particle-particle collisions
        for i in range(len(self.ball_list)):
            dt = a_ball.time_to_hit(self.ball_list[i])
            # insert this event into pq
            heapq.heappush(self.pq, my_event.Event(self.t + dt, a_ball, self.ball_list[i], None))

        # particle-wall collisions
        dtX = a_ball.time_to_hit_vertical_wall()
        dtY = a_ball.time_to_hit_horizontal_wall()
        heapq.heappush(self.pq, my_event.Event(self.t + dtX, a_ball, None, None))
        if dtY < math.inf:  # ชนในแนว y
            heapq.heappush(self.pq, my_event.Event(self.t + dtY, None, a_ball, None))

    def __draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2 * self.canvas_width)
            turtle.left(90)
            turtle.forward(2 * self.canvas_height)
            turtle.left(90)

    def __redraw(self):
        turtle.clear()
        self.my_paddle.clear()
        self.__draw_border()
        self.my_paddle.draw()
        for brick in self.bricks:
            brick.draw()  # draw bricks
        for i in range(len(self.ball_list)):
            self.ball_list[i].draw()
        turtle.update()
        heapq.heappush(self.pq, my_event.Event(self.t + 1.0 / self.HZ, None, None, None))

    def __paddle_predict(self):
        for i in range(len(self.ball_list)):
            a_ball = self.ball_list[i]
            dtP = a_ball.time_to_hit_paddle(self.my_paddle)
            heapq.heappush(self.pq, my_event.Event(self.t + dtP, a_ball, None, self.my_paddle))

    # move_left and move_right handlers update paddle positions
    def move_left(self):
        if (self.my_paddle.location[0] - self.my_paddle.width / 2 - 40) >= -self.canvas_width:
            self.my_paddle.set_location([self.my_paddle.location[0] - 40, self.my_paddle.location[1]])

    # move_left and move_right handlers update paddle positions
    def move_right(self):
        if (self.my_paddle.location[0] + self.my_paddle.width / 2 + 40) <= self.canvas_width:
            self.my_paddle.set_location([self.my_paddle.location[0] + 40, self.my_paddle.location[1]])

    def update_score(self):
        self.score_turtle.clear()
        self.score_turtle.goto(-self.canvas_width + 20, self.canvas_height - 40)  # ตำแหน่งมุมบนซ้าย
        self.score_turtle.write(f"Score: {self.score}", font=("Arial", 16, "normal"))

    def run(self):
        # Initialize priority queue with collision events and redraw event
        for i in range(len(self.ball_list)):
            self.__predict(self.ball_list[i])
        heapq.heappush(self.pq, my_event.Event(0, None, None, None))

        # Listen to keyboard events and activate move handlers
        self.screen.listen()
        self.screen.onkey(self.move_left, "Left")  # left arrow
        self.screen.onkey(self.move_right, "Right")  # right arrow
        self.screen.onkey(self.move_left, "a")  # a button
        self.screen.onkey(self.move_left, "A")  # A button
        self.screen.onkey(self.move_right, "d")  # d button
        self.screen.onkey(self.move_right, "D")  # D button

        while True:
            e = heapq.heappop(self.pq)
            if not e.is_valid():
                continue

            ball_a = e.a
            ball_b = e.b
            paddle_a = e.paddle

            # Update positions
            for i in range(len(self.ball_list)):
                self.ball_list[i].move(e.time - self.t)
            self.t = e.time

            # Update the timer
            self.timer = self.t
            self.update_timer()

            # Check if any ball hits the bottom boundary
            for ball in self.ball_list:
                if ball.y - ball.size <= -self.canvas_height:  # Ball hits the bottom
                    self.lives -= 1
                    self.update_lives()
                    print(f"Ball hit bottom at y={ball.y}. Lives remaining: {self.lives}")

                    if self.lives > 0:
                        # Reset ball position and velocity
                        ball.x = 0
                        ball.y = 0
                        ball.vx = random.uniform(-200, 200)
                        ball.vy = 200
                    else:
                        # End game if no lives left
                        self.score_turtle.goto(0, 0)
                        self.score_turtle.color("red")
                        self.score_turtle.write("Game Over!", align="center", font=("Arial", 24, "bold"))
                        return  # Exit the game loop

            # Check for collisions with bricks
            for brick in self.bricks:
                for ball in self.ball_list:
                    if brick.check_collision(ball):
                        self.score += 1
                        self.update_score()
                        # Adjust ball direction based on collision
                        if abs(ball.x - brick.x) > abs(ball.y - brick.y):
                            ball.vx = -ball.vx
                        else:
                            ball.vy = -ball.vy
                        break

            # Check if all bricks are destroyed
            if all(not brick.is_active for brick in self.bricks):
                self.display_win_message()
                break  # Exit the game loop

            # Handle collisions
            if (ball_a is not None) and (ball_b is not None) and (paddle_a is None):
                ball_a.bounce_off(ball_b)
            elif (ball_a is not None) and (ball_b is None) and (paddle_a is None):
                ball_a.bounce_off_vertical_wall()
            elif (ball_a is None) and (ball_b is not None) and (paddle_a is None):
                ball_b.bounce_off_horizontal_wall()
            elif (ball_a is None) and (ball_b is None) and (paddle_a is None):
                self.__redraw()
            elif (ball_a is not None) and (ball_b is None) and (paddle_a is not None):
                ball_a.bounce_off_paddle()

            self.__predict(ball_a)
            self.__predict(ball_b)
            self.__paddle_predict()

        # Hold the window; close it by clicking the window close 'X' mark
        turtle.done()


class StartScreen:
    def __init__(self):
        # Create main window
        self.root = tk.Tk()
        self.root.title("Break bricks Game Start")
        self.root.configure(bg='#F7E5E5')  # Background color
        self.root.geometry("700x400")  # Window size

        # Add a welcome message
        self.label_title = tk.Label(self.root, text="Welcome to Break Bricks Game!",
                                    font=('Times New Roman', 28, 'bold'), bg='#F7E5E5', fg='#5E4343')
        self.label_title.pack(pady=30)

        # Description
        self.label_subtitle = tk.Label(self.root, text="Press Start to Play or Exit to Quit",
                                       font=('Times New Roman', 20), bg='#F7E5E5', fg='#5E4343')
        self.label_subtitle.pack(pady=10)

        # Game start button
        self.button_start = tk.Button(self.root, text="Start Game", command=self.start_game,
                                      font=('Times New Roman', 18, 'bold'), bg='#D1AFAF', fg='#5E4343', width=15,
                                      height=2)
        self.button_start.pack(pady=15)

        # Exit game button
        self.button_exit = tk.Button(self.root, text="Exit", command=self.exit_game,
                                     font=('Times New Roman', 18, 'bold'), bg='#D1AFAF', fg='#5E4343', width=15,
                                     height=2)
        self.button_exit.pack(pady=15)

    def start_game(self):
        # Start the ball game
        self.root.destroy()  # Close the Start Screen window.
        num_balls = 1  # You can change the number of balls here.
        game = BouncingSimulator(num_balls)  # Create a ball game
        game.run()  # Run the ball game

    def exit_game(self):
        # Close the program
        self.root.destroy()

    def run(self):
        # Start the home screen
        self.root.mainloop()


# Create and call the home screen.
if __name__ == "__main__":
    start_screen = StartScreen()
    start_screen.run()

