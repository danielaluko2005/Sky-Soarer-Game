# Sky-Soarer-Game
Sky Soarer Game
# Introduction
Welcome to the Flappy Bird game! This is a simple implementation of the popular Flappy Bird game using Python and Pygame.

# Features
Simple Gameplay: Navigate the bird through pipes by tapping the space bar or mouse left button.

Difficulty Level: Choose a difficulty level of your choice. (EASY, MEDIUM ,HARD).
Scoring System: Gain points for successfully passing through pipes.

Obstacle Animation: Pipes move from right to left, creating dynamic gameplay.

Ground Movement: Experience the feeling of flight with a scrolling ground.

Scalability: Designed the game to scale well as players progress. As the difficulty increases, the game remains responsive and enjoyable.

Frame Rate (FPS): Maintains a consistent and high frame rate. This ensures that the animation appears smooth and responsive, enhancing the player's ability to control the bird.

# Requirements
Python 3.x

Pygame library

# Code Overview
Main Game Loop: The game uses a standard Pygame loop to continuously update and draw the game elements.

Flappy Bird Class: Represents the player-controlled bird with methods for movement and animation.

Pipe Class: Defines the pipes as obstacles, with methods for movement and collision detection.

Ground Class: Manages the scrolling ground to simulate forward movement.

# How to Play
Go to main.py and run the code.

Press the space bar or click the mouse to make the bird flap and navigate through the pipes.

Score points for each successfully passed pipe.

The game ends if the 3 lives allocated for the bird becomes 0. The life reduces if the bird collides with a pipe or the ground or sky.

# License
This Flappy Bird game is open-source and available under the MIT License. Enjoy playing!