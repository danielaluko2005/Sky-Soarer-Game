import pygame
import os
from random import randint
flapping_creature_images = [
    pygame.image.load(os.path.join("Images","bird" + str(x) + ".png")) for x in range(1,4)]


obstacle_image = pygame.transform.scale2x(pygame.image.load(os.path.join("Images", "pipe.png")))

ground_image = pygame.transform.scale2x(pygame.image.load(os.path.join("Images", "base.png")))

background_image = pygame.image.load(os.path.join("Images", "background.jpg"))

class FlappingBird:

    IMAGES = flapping_creature_images
    MAX_ANGLE = 25
    ROTATION_SPEED = 20
    ANIMATION_DURATION = 5

    def __init__(self, x_pos, y_pos) -> None:
        """
        Initialize the FlappingBird object.

        Args:
        - x_pos (int): The initial x-coordinate of the bird.
        - y_pos (int): The initial y-coordinate of the bird.
        """
        self.x = x_pos
        self.y = y_pos
        self.initial_height = self.y
        self.time_elapsed = 0
        self.angle = 0
        self.speed = 0
        self.display_image = self.IMAGES[0]
        self.image_count = 0

    
    def generate_collision_mask(self):
        """
        Generate a collision mask for the current display image.

        Returns:
        - pygame.mask.Mask: The collision mask for the current display image.
        """
        return pygame.mask.from_surface(self.display_image)
    
    def move(self):

        """
        Move the bird based on user input.

        This method handles the bird's motion, taking into account user input.
        """
        if pygame.mouse.get_pressed()[0] == 1:
            self.launch()
        self.time_elapsed += 1
        energy = (self.speed * self.time_elapsed) + (1.5 * pow(self.time_elapsed, 2))

        if energy >= 16:
            energy = 16

        if energy < 0:
            energy -= 2

        self.y = self.y + energy

        if energy < 0 or self.y < self.initial_height + 50:
            if self.angle < self.MAX_ANGLE:
                self.angle = self.MAX_ANGLE
        else:
            if self.angle > -90:
                self.angle -= self.ROTATION_SPEED

    def launch(self):
        """
        Launch the bird upwards.

        This method is called when the user initiates a jump.
        """
        self.speed = -10.5
        self.time_elapsed = 0
        self.initial_height = self.y

    def draw(self, display_surface):

        """
        Draw the bird on the display surface.

        Args:
        - display_surface (pygame.Surface): The surface on which to draw the bird."""

        self.image_count = (self.image_count + 1) % (self.ANIMATION_DURATION * 4 + 2)

        if self.angle <= -90:
            self.display_image = self.IMAGES[1]
        else:
            self.display_image = self.IMAGES[(self.image_count // self.ANIMATION_DURATION) % 3]

        rotated_image = pygame.transform.rotate(self.display_image, self.angle)
        new_rect = rotated_image.get_rect(center=self.display_image.get_rect(topleft=(self.x, self.y)).center)
        display_surface.blit(rotated_image, new_rect.topleft)

   

class Obstacle:
    """Obstacle class."""
    MOVEMENT_SPEED = 5

    def __init__(self, initial_x,space) -> None:
        """
        Initialize an obstacle.

        Args:
        - initial_x (int): The initial x-coordinate of the obstacle.
        - space (int): The space between the top and bottom parts of the obstacle.
        """
        self.x = initial_x
        self.top_height = 0
        self.top_y = 0
        self.bottom_y = 0
        
        self.inverted_top_image = pygame.transform.flip(obstacle_image, False, True)
        self.bottom_image = obstacle_image
        self.space=space #change with difficulty.
        self.has_passed = False
        self.setup_height()

    def setup_height(self):
        """Set up the height of the top and bottom parts of the obstacle."""

        self.top_height = randint(50, 400)
        self.top_y = self.top_height - self.inverted_top_image.get_height()
        self.bottom_y = self.top_height + self.space

    def move(self):
        """Move the obstacle to the left."""

        self.x -= self.MOVEMENT_SPEED

    def display(self, display_surface):
        """
        Display the obstacle on the given surface.

        Args:
        - display_surface (pygame.Surface): The surface on which to display the obstacle.
        """
        display_surface.blit(self.inverted_top_image, (self.x, self.top_y))
        display_surface.blit(self.bottom_image, (self.x, self.bottom_y))

    def check_collision(self, flying_entity):
        """
        Check for collision between the obstacle and a flying entity.

        Args:
        - flying_entity (FlappingBird): The flying entity to check for collision.

        Returns:
        - bool: True if a collision is detected, False otherwise.
        """
        flying_entity_mask = flying_entity.generate_collision_mask()
        top_mask = pygame.mask.from_surface(self.inverted_top_image)
        bottom_mask = pygame.mask.from_surface(self.bottom_image)

        top_offset = (self.x - flying_entity.x, self.top_y - round(flying_entity.y))
        bottom_offset = (self.x - flying_entity.x, self.bottom_y - round(flying_entity.y))

        bottom_point = flying_entity_mask.overlap(bottom_mask, bottom_offset)
        top_point = flying_entity_mask.overlap(top_mask, top_offset)

        if top_point or bottom_point:
            return True
        return False


class Ground:
    """Class representing the ground in the game."""

    MOVEMENT_SPEED = 5
    WIDTH = ground_image.get_width()
    IMAGE = ground_image

    def __init__(self, y_position) -> None:
        """
        Initialize the ground.

        Args:
        - y_position (int): The y-coordinate of the ground.
        """

        self.y = y_position
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        """Move the ground to the left."""

        self.x1 -= self.MOVEMENT_SPEED
        self.x2 = self.MOVEMENT_SPEED

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def render(self, display_surface):
        """
        Render the ground on the given surface.

        Args:
        - display_surface (pygame.Surface): The surface on which to render the ground.
        """

        display_surface.blit(self.IMAGE, (self.x1, self.y))
        display_surface.blit(self.IMAGE, (self.x2, self.y))


def display_game_interface(surface,WINDOW_WIDTH,game_font, player, obstacles, ground, player_score):
    """
    Display the game interface.

    Args:
    - surface (pygame.Surface): The surface on which to display the game interface.
    - WINDOW_WIDTH (int): The width of the game window.
    - game_font (pygame.font.Font): The font used for displaying the score.
    - player (FlappingBird): The player character.
    - obstacles (list): List of obstacle objects.
    - ground (Ground): The ground object.
    - player_score (int): The current player score.
    """
    surface.blit(background_image, (0, 0))

    for obstacle in obstacles:
        obstacle.display(surface)

    ground.render(surface)
    player.draw(surface)

    score_display = game_font.render("Current Score: " + str(player_score), 1, (255, 255, 255))
    
    surface.blit(score_display, (WINDOW_WIDTH - score_display.get_width() - 15, 10))
    pygame.display.update()
    
