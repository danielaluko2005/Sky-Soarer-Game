from Birds_obstacles_ground import FlappingBird, Obstacle, Ground,display_game_interface
import pygame
pygame.init()
# Define window dimensions and font
WIN_WIDTH = 600
WIN_HEIGHT = 800
game_font = pygame.font.SysFont("arial", 50)

def play(easy,medium):
    """Main Driver of the game."""
    # Initialize game state

    if easy:
        obstacle_interval=700
        gap=400
    elif medium:
        obstacle_interval=650
        gap=330
    else:
        obstacle_interval=600
        gap=250
    flying = False
    bird = FlappingBird(230, 350)
    base = Ground(730)
    obstacles = [Obstacle(700,gap)]

    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    score = 0

    clock = pygame.time.Clock()
    
    preparations=True
    
    while preparations:
        # So as to make the game not start playing before the user is ready by clicking the left side of the mouse.
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN  and event.button == 1:
                preparations=False
        display_game_interface(win, WIN_WIDTH, game_font, bird, obstacles, base, score)


    run = True

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and not flying:
                flying = True

        add_obstacles = False
        rem = []

        for obstacle in obstacles:
            if obstacle.check_collision(bird):
                run = False

            if obstacle.x + obstacle.inverted_top_image.get_width() < 0:
                rem.append(obstacle)

            if not obstacle.has_passed and obstacle.x < bird.x:
                obstacle.has_passed = True
                add_obstacles = True

            obstacle.move()

        if add_obstacles:
            score += 1
            obstacles.append(Obstacle(obstacle_interval,gap))  # Adjust the speed the pipe shows.

        for r in rem:
            obstacles.remove(r)

        if bird.y + bird.display_image.get_height() >= 730 or bird.initial_height <= 0:
            break

        base.move()
        bird.move()
        display_game_interface(win, WIN_WIDTH, game_font, bird, obstacles, base, score)

    pygame.quit()
    quit()


def main():
    """Choose difficulty level"""
    print("Enter the level of difficulty you want")
    print("If `EASY` enter `E`.")
    print("If `MEDIUM` enter `M`.")
    print("If `HARD` enter `H`.")
    difficulty_level=input("Enter your choice:- ")

    if difficulty_level[0].lower()== "e":
        play(True,False)
    elif difficulty_level[0].lower()== "m":
        play(False,True)
    elif difficulty_level[0].lower()== "h":
        play(False,False)
    else:
        print("Invalid Input.")


if __name__=="__main__":
    main()
