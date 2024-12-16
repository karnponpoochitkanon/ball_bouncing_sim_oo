Include a UML class diagram for your project
https://lucid.app/lucidchart/9ee55967-dcc4-41de-9318-73ffaff99d8d/edit?viewport_loc=-3842%2C-1268%2C5368%2C2603%2C0_0&invitationId=inv_5a6fed12-c9b3-4bff-8fcf-09598e68ea8f

In summary, what functions does each file have and how does it work?
1.file ball.py
class Ball
1.1 def init
   1.1.1 Initializes a ball object with size, position (x, y), velocity (vx, vy), color, and unique ID.
   1.1.2 Calculates the mass based on the size of the ball.
   1.1.3 Stores the screen dimensions for collision detection.
1.2 def draw
   1.2.1 Draws the ball at its current position using the turtle module.
   1.2.2 Sets the color and fills the ball as a circle.
1.3 def bounce_off_vertical_wall
   1.3.1 Draws the ball at its current position using the turtle module.
   1.3.2 Sets the color and fills the ball as a circle.
1.4 def bounce_off_horizontal_wall
   1.4.1 Reverses the y-velocity (vy) when the ball hits a horizontal wall.
   1.4.2 Your code updates the collision count, but the teacher's code repositions the ball within the frame boundaries.
1.5 def bounce_off
   1.5.1 Handles collisions between two balls.
   1.5.2 Calculates the new velocities for both balls based on the physics of elastic collisions.
   1.5.3 Updates the collision count for both balls.
1.6 def distance
   1.6.1 Calculates the Euclidean distance between the ball and another ball.
1.7 def move
   1.7.1 Updates the ball's position based on its velocity and the time step dt.
1.8 def time_to_hit
   1.8.1 Computes the time until the ball will collide with another ball.
   1.8.2 Uses relative positions and velocities to determine when the balls will touch.
1.9 def time_to_hit_vertical_wall
   1.9.1 Calculates the time until the ball hits a vertical wall.
   1.9.2 Takes into account the ball's current velocity and position.
1.10 def time_to_hit_horizontal_wall
   1.10.1 Calculates the time until the ball hits a horizontal wall.
1.11 def time_to_hit_paddle
   1.11.1 Determines when the ball will collide with a paddle.
   1.11.2 Uses the paddle's position, size, and the ball's velocity to calculate the time to collision.
1.12 def bounce_off_paddle
   1.12.1 Reverses the y-velocity (vy) when the ball hits the paddle.
   1.12.2 Updates the collision count for the ball.
1.13 def __str__
   1.13.1Returns a string representation of the ball's current position, velocity, collision count, and ID.
Summary of major differences from the original code
1.Removal of Position Adjustment for Wall Bounces:
Original code:  Adjusts the position of the ball to ensure it stays within the frame when bouncing off the walls (e.g., self.x = self.canvas_width - self.size).
My Code: Removes this adjustment, only reversing the velocity (vx or vy) without re-positioning the ball.
2.Use of Square Root in time_to_hit_paddle:
Original code: Directly calculates time using linear distance and ball/paddle size.
My Code: Adds math.sqrt when calculating time to hit the paddle:
3.Simplified bounce_off_vertical_wall and bounce_off_horizontal_wall:
Original Code: Handles velocity inversion and re-positioning within the frame.
My Code: Only reverses the velocity and increments the collision count:

2.file bricks.py
class Brick
2.1 def __init__
   2.1.1 Initializes the Brick object with position (x, y), size, color, and a turtle_instance for drawing.
   2.1.2 Sets is_active to True, indicating the brick is still intact and can be hit.
2.2 def draw
   2.2.1 Draws the brick on the screen using the turtle module.
   2.2.2 Starts at the top-left corner and draws a square with the specified size and color.
   2.2.3Does nothing if the brick is no longer active (is_active is False).
2.3 def clear
   2.3.1 Clears the drawing for this brick using the turtle instance.
2.4 def check_collision
   2.4.1 Checks if the ball's position intersects with the brick's boundaries.
   2.4.2 If a collision is detected:
             -Sets is_active to False, marking the brick as destroyed.
             -Returns True to indicate a collision.
   2.4.3 If no collision occurs or the brick is already destroyed, returns False.

Summary of major differences from the original code
This one has no original code, it's a class I created myself.

3.file my_event.py
class Event
3.1 def __init__
   3.1.1 Initializes an Event object representing a collision or interaction in the simulation.
   3.1.2 Takes the time of the event (time), two balls (ball_a and ball_b), and a paddle (paddle) involved in the event.
   2.1.3 Stores the current collision count (count_a and count_b) for the balls to validate the event later.
             -If a ball is None, assigns -1 to its collision count.
3.2 def __lt__
   3.2.1 Defines a "less than" operator to compare two Event objects based on their time attribute.
   3.2.2 This allows events to be sorted and prioritized (e.g., in a priority queue).
3.3 def is_valid
   3.3.1 Checks if the event is still valid by comparing the stored collision counts of the balls with their current collision counts.
   3.3.2 Returns False if the collision count of either ball has changed (indicating the event is outdated).
   3.3.3 Returns True if the event is still valid.
Summary of major differences from the original code
Exactly the same

4 file paddle.py
class Paddle
4.1 def __init__
   4.1.1 Initializes a Paddle object with specified dimensions (width, height), color, and a turtle instance for drawing.
   4.1.2 Reduces the paddle’s width and height by 50% for scaling purposes.
   4.1.3 Sets the paddle's location to [0, 0] and prepares the turtle instance by lifting the pen, setting the direction, and hiding the turtle cursor.
4.2 def set_location
   4.2.1 Updates the paddle's location to a new position (location).
   4.2.2Moves the turtle to the new location.
4.3 def draw
   4.3.1 Draws the paddle on the screen as a rounded rectangle using the turtle module.
   4.3.2 Moves to the top-left corner of the paddle.
   4.3.3 Uses the circle method to create rounded corners.
             -Fills the paddle with the specified color.
4.4 def clear
   4.4.1 Clears the paddle's drawing using the turtle instance.
4.5 def __str__
   4.5.1 Returns a simple string representation "paddle".
Summary of major differences from the original code
1. Paddle Size
Original Code:  Full width and height
My Code:  Reduced width and height by 50%  
2.  Drawing Start Position
Original Code:  Starts drawing from the center
My Code:  Starts drawing from the top-left corner
3.  Shape
Original Code:  Standard rectangle
My Code:  Rounded rectangle with curved corners
4.  Rounded Corners
Original Code:  Not implemented
My Code: Uses turtle.circle for rounded edges
5.  Code for Rounded Rectangle
Original Code:  Not present
My Code:  Added loop to draw curved corners



5 file run_ball.py
class BouncingSimulator
5.1.1 def __init__
   5.1.1.1 Initializes the game with a specified number of balls.
   5.1.1.2 Sets up the canvas dimensions, game variables (score, lives, timer), and objects (balls, paddle, bricks).
   5.1.1.3 Randomizes ball directions and creates a grid of bricks.
   5.1.14 Prepares the turtle graphics and sets the background color.
5.1.2 def update_lives
   5.1.2.1 Updates the display of the player’s remaining lives.
   5.1.2.2 Draws red heart emojis on the top-right of the screen for each life left.
5.1.3 def update_timer
   5.1.3.1 Displays the elapsed game time in the top-center of the screen.
5.1.4 def display_win_message
   5.1.4.1 Displays a "You Win!" message in red at the top-center of the screen when all bricks are destroyed.
5.1.5 def __predict
   5.1.5.1 Predicts future events for a specific ball, such as:
             -Collisions with other balls.
             -Collisions with walls (vertical and horizontal).
   5.1.5.2 Adds these events to a priority queue for efficient handling.
5.1.6 def __draw_border
   5.1.6.1 Draws a black-bordered rectangular frame for the game area.
5.1.7 def __redraw
   5.1.7.1 Clears the canvas and redraws the paddle, bricks, and balls.
   5.1.7.2 Updates the graphics to reflect the current state of the game.
5.1.8 def __paddle_predict
   5.1.8.1 Predicts future collisions between the ball and the paddle.
   5.1.8.2 Adds paddle-related events to the priority queue.
5.1.9 def move_left
   5.1.9.1 Moves the paddle left by a fixed amount (40 pixels), ensuring it doesn’t go out of bounds.
5.1.10 def move_right
   5.1.10.1 Moves the paddle right by a fixed amount (40 pixels), ensuring it stays within the canvas.
5.1.11 def update_score
   5.1.11.1 Updates the player’s score display at the top-left of the screen.
5.1.12 def run
   5.1.12.1 Implements the main game loop:
             -Processes events from the priority queue.
             -Updates ball positions and checks for collisions (walls, bricks, paddle).
             -Updates the score, timer, and remaining lives.
             -Ends the game if lives are exhausted or all bricks are destroyed.
   5.1.12.2 Listens for keyboard input to control the paddle.
Summary of major differences from the original code
1.  Bricks List
Original Code:   Not present
My Code:  Added a bricks list to manage bricks.eg.  self.bricks = []
2.  Ball Size Adjustment
Original Code:   ball_radius = 0.05 * self.canvas_width
My Code: Reduced ball size to 25% of the original. eg.  ball_radius = 0.05 * self.canvas_width * 0.25
3.  Ball Speed and Angle
Original Code:   Randomized vx and vy
My Code:   Enhanced ball movement with precise angles eg.Added angle-based velocity (cos/sin)
4.  Scale for Ball Speed
Original Code:   Not implemented
My Code:  Added realistic ball speed scaling. 
5.  Bricks Setup
Original Code:  Not implemented
My Code:  Added rows of bricks with configurable spacing.
6.  Brick Drawing
Original Code: Not present
My Code:  Bricks are added with their positions.
7.  Score Tracking
Original Code:  Not implemented
My Code:  Added score tracking for the game.
8.  Lives Tracking
Original Code:   Not implemented
My Code:  Added lives tracking for the game.
9.  Timer Feature
Original Code:   Not implemented
My Code:  Added a timer to track the elapsed time.
10.  New Method:  update_score()
Original Code:  Not present
My Code:  Displays current score on the screen.
11. New Method:  update_timer()
Original Code:  Not present
My Code:  Tracks and shows elapsed simulation time.
12.  New Method:  display_win_message()
Original Code:  Not present 
My Code:  Added a victory condition when all bricks are destroyed.
13.  Brick Collision Handling
Original Code:  Not implemented
My Code:  Adjusts ball direction and updates score when bricks are hit.
14.  Game Over Condition
Original Code:  Not implemented
My Code:  Exits the game when the player loses all lives.
15.  Win Condition
Original Code:  Not implemented  
My Code:  Displays win message when all bricks are hit.
16.  Background Color
Original Code:   Default white
My Code:  Changed the background color outside the game box. #FFece8
17.  Redraw Adjustments
Original Code:  Draws border and balls only
My Code:  Enhanced the redraw logic to include bricks.
18.  Timer Update in Loop
Original Code:  Not implemented  
My Code:  Timer updates as the game progresses.
19.  Ball Bottom Collision (Lives)
Original Code:   Not implemented
My Code:  Reduces lives and resets ball position.
20.  Paddle Movement Enhancements
Original Code:  Only uses "Left" and "Right" keys
My Code:  Added support for "a", "A", "d", and "D"
21.  Event Queue
Original Code: Manages ball and paddle collisions
My Code:  Extended to handle bricks and timers

class StartScreen
5.2.1 def __init__
   5.2.1.1Sets up a tkinter window with:
             -A welcome message.
             -Buttons to start the game or exit.
5.2.2 def start_game
   5.2.2.1 Destroys the start screen window and initializes the BouncingSimulator game.
   5.2.2.2 Starts the game with one or more balls (can be configured).
5.2.3 def exit_game
   5.2.3.1 Closes the tkinter application, effectively exiting the program.
5.2.4 def run
   5.2.4.1 Runs the tkinter event loop to display the start screen.
Summary of major differences from the original code
This one has no original code, it's a class I created myself.


Rules of the Game 
When the code runs, a welcome screen will appear with the text "Welcome to Break Bricks Game." If you want to play the game, press the "Start Game" button at the top. If you don’t want to play, press the "Exit" button, and the game will close automatically. If you decide to start the game by pressing the "Start Game" button, it will take you to the gameplay screen. The rules of the game are as follows: This is a game where you use a red paddle to bounce the ball and destroy bricks. Each brick destroyed earns you 1 point. If you destroy all the bricks, a message saying "You Win!" will appear, and the game will end. However, you must ensure the ball does not fall below the paddle and touch the black line at the bottom. If it does, you will lose a life. If all lives are lost, the game will display "Game Over." Initially, I planned to provide 2-3 lives (red hearts), but I encountered a bug while implementing this. Despite my efforts to debug, I couldn't fix it within the limited time and knowledge I currently have. As a result, the game now only gives 1 life, meaning you lose immediately if the ball touches the black line. Additionally, the game includes a timer that counts the time taken to complete the game, measured in the in-game unit "ss." The timer keeps track of your fastest time.

Describe how you test your code and report whether your project is working 100% correctly or there are know bugs that are still to be resolved
Regarding my work, if you ask if it’s 100%, I’d say no, because there are many things I wanted to do but couldn’t. Some things didn’t work as intended, and some were buggy. I’d rate it at around 70%. For example, I created a heart shape, and initially, I wanted to have multiple hearts, but when I implemented it, they disappeared during gameplay, and I still don’t know why. Another example is the background color—I wanted to apply it only outside the rectangular frame in black, but I didn’t know how to do it, so I ended up applying it to everything.
Moving forward, I’ll strive to gain more knowledge and work harder to accomplish things I currently can’t do or don’t understand. I hope to make those ideas a reality in the future. Thank you for your support, understanding, and assistance throughout this project. I truly appreciate it!
