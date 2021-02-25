# Snake-Game
Python program emulating the famous Snake Game

The player maneuvers a line which grows in length, with the line itself being a primary obstacle. The line will grow as the player successful captures food (blue dots) on the screen. This will also increase the player's score.

The project can be divided into 7 parts:

1. Create a snake body
2. Move the snake
3. Control the snake
4. Detect collision with food
5. Create a scoreboard
6. Detect a collision with the wall
7. Detect a collision with the tail

Creating the snake body

I used the Turtle Graphics GUI to do that. The snake body, initially is made up of 3 turtle objects, shaped as squares and white-colored.
The three squares are positioned to be together and side by side initially at positions on the x-axis. Therefore the snake is made up of segments (turtle objects forming a list of segments) and the first segment (the first item of that list) is 

Moving the snake

To implement the movement of the snake, I moved the pen up for all the squares created (as the square themselves are Turtle objects).
In order for the squares to move,one after the other, we have to assign the position of the segment before to the one that follows (see the move() method of the Snake class).
I also had to refactor my code and create 3 classes, each in its own separate .py file (Food, Snake and Scoreboard) in order to make it more easier to implement the game and use the benefits of OOP when it comes to modularity. I also disable the tracer and used the update() of the Screen class and sleep() of the Time class in order to implement a very sueful delay interms of rendering the movements of the segments.

Controlling the snake

To control the snake's movements, I used event listeners with the function onkey() inside the main.py file. Then inside the Snake class, I implemented methods that were bound to event listeners in the main.py file. Namely up(), down(), left() and right(). These four methods are pretty similar since they first check if the current heading (orientation) is the opposite of the direction wished by the user (such moves are forbidden in the rules of the game, one going upwards cannot then go downwards). If not then the change in orientation is allowed and the head of the snake (the first segment) gets a new orientation and all the other segments follows afterwards.

Detecting collision with food

I created a Food class for this purpose which inherits from the the Turtle class. Objects of the Food class are also Turtle objects but round-shaped and blue. 
The Food class also includes a refresh() method, which allows the Food object to reappears on the screen everytime the snake successfuly collide with it.
To detect such collisions, in our main.py file we check to see if the head of the snake (the first segment) reaches a distance of less than 15 pixels to the Food object on the screen. If so, then it counts as a collision, the Food object will reappear somewhere else, the player's score should increase and the snake's body should extend. I made a new class (Scoreboard) and methods for such purpose in the Scoreboard class with the increase_score() and in the Snake class with the method extend().

Creating a scoreboard

As I just mentionned, I made a class named Scoreboard responsible for the functionalities of the Scoreboard. That class is a subclass of the Turtle class and has a method called display() that writes onto the Screen the current score, increase_score() which increases by one the score to be displayed.

Detecting a collision with the wall

To detect such a collision with the wall (the borders of our screen), we need to check if the x or y-coordinate of the snake's head are greater than a certain limit (290 ,when the actual "wall" is at 300). If the limit is reached by the head, the game is over and the main loop in our main file stops.

Detecting a collision with the tail

To detect such a collision, we need to check for all the segments in the snake (except the head) if they are within a distance of the snake's head (in our case, less than 10 pixels). If it is the case, then it is game over and the main loop in our main file stops.

