import pygame
import random

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen_width = 900
screen_height = 600

gameWindow = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Snake Game By Chunamani ")
pygame.display.update()

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 43)


def sc_score(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(black)
        sc_score("WELCOME TO SNAKES !!!!!", red, screen_width / 5, screen_height / 5)
        sc_score("Press Enter To Continue", red, screen_width / 5, screen_height / 7)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()

        pygame.display.update()
        clock.tick(40)


def gameloop():
    exit_game = False
    game_over = False

    snk_list = []
    snk_len = 1
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_size = 27
    fps = 40
    score = 0

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)

    init_velocity = 5

    with open("hiscore.txt", "r+") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(black)
            sc_score("Game Over ! Press Enter to Continue ", red, screen_width / 5, screen_height / 5)

            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

                    if event.key == pygame.K_ESCAPE:
                        quit()


        else:

            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 9 and abs(snake_y - food_y) < 9:
                score += 10
                # print("score : ",score *10)

                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_len += 5
                if score > int(hiscore):
                    hiscore = score

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_len:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            gameWindow.fill(black)
            sc_score("Score : " + str(score) + "  Hiscore : " + str(hiscore), red, 2, 2)
            # pygame.draw.rect(gameWindow, black , [snake_x , snake_y , snake_size, snake_size])
            plot_snake(gameWindow, white, snk_list, snake_size)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()


if __name__ == "__main__":
    welcome()
    # gameloop()