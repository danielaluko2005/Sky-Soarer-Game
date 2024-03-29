from Birds_obstacles_ground import FlappingBird, Obstacle, Ground,display_game_interface
from saving import load_value, edit_file_line
import pygame
pygame.init()
# Define window dimensions and font
WIN_WIDTH = 600
WIN_HEIGHT = 800
game_font = pygame.font.SysFont("arial", 50)

def play(easy,medium,lives,score):
    """Main Driver of the game."""
    # Initialize game state

    
    file_name="values.txt" #Name of the file to save the highest score.

    
    if easy:
        obstacle_interval=700
        gap=400
        difficulty_number=1
        difficulty="easy"
    elif medium:
        obstacle_interval=650
        gap=330
        difficulty_number=2
        difficulty="medium"   
    else:
        obstacle_interval=600
        gap=250
        difficulty_number=3
        difficulty="hard"

        
        
    flying = False
    bird = FlappingBird(230, 350)
    base = Ground(730)
    obstacles = [Obstacle(700,gap)]

    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    clock = pygame.time.Clock()
    
    preparations=True

    maximum_score=load_value(file_name,difficulty_number)

    
    
    while preparations:
        # So as to make the game not start playing before the user is ready by clicking the left side of the mouse.
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN  and event.button == 1:
                preparations=False
        display_game_interface(win, WIN_WIDTH, game_font, bird, obstacles, base, score,lives,maximum_score,difficulty)


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
                if lives>0:
                    # Used recursions to keep replaying as long as lives is not negative
                    lives-=1
                    play(easy,medium,lives,score)
                    
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
            if lives>0:
                lives-=1
                play(easy,medium,lives,score)
                
            break
        

        base.move()
        bird.move()
        maximum_score=load_value(file_name,difficulty_number)
        if score>int(maximum_score):
            edit_file_line(file_name,difficulty_number,score)

        display_game_interface(win, WIN_WIDTH, game_font, bird, obstacles, base, score,lives,maximum_score,difficulty)

    pygame.quit()
    quit()


def main():
    """Choose difficulty level"""
    print("Enter the level of difficulty you want")
    print("If `EASY` enter `E`.")
    print("If `MEDIUM` enter `M`.")
    print("If `HARD` enter `H`.")
    difficulty_level=input("Enter your choice:- ")
    lives=3
    score=0
    if difficulty_level[0].lower()== "e":
        play(True,False,lives,score)
    elif difficulty_level[0].lower()== "m":
        play(False,True,lives,score)
    elif difficulty_level[0].lower()== "h":
        play(False,False,lives,score)
    else:
        print("Invalid Input.")


if __name__=="__main__":
    main()
