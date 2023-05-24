
import pygame

# Initialize the game
pygame.init()

# Create the screen
screen = pygame.display.set_mode((600, 400))

# Set the background color
screen.fill((255, 255, 255))

# Create the snake
snake = [(0, 0), (10, 0), (20, 0)]

# Create the food
food = (30, 30)

# Create the direction of the snake
direction = "up"

# Create the game loop
while True:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Move the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "up"
            elif event.key == pygame.K_DOWN:
                direction = "down"
            elif event.key == pygame.K_LEFT:
                direction = "left"
            elif event.key == pygame.K_RIGHT:
                direction = "right"

    # Move the snake
    for i in range(len(snake) - 1):
        snake[i] = snake[i + 1]

    # Move the head of the snake
    if direction == "up":
        snake[-1] = (snake[-1][0], snake[-1][1] - 10)
    elif direction == "down":
        snake[-1] = (snake[-1][0], snake[-1][1] + 10)
    elif direction == "left":
        snake[-1] = (snake[-1][0] - 10, snake[-1][1])
    elif direction == "right":
        snake[-1] = (snake[-1][0] + 10, snake[-1][1])

    # Check if the snake hit the food
    if snake[-1] == food:
        snake.append((0, 0))
        food = (random.randint(0, 590), random.randint(0, 390))

    # Check if the snake hit itself
    for i in range(len(snake) - 1):
        if snake[-1] == snake[i]:
            pygame.quit()
            sys.exit()

    # Draw the snake
    for i in range(len(snake)):
        pygame.draw.rect(screen, (0, 0, 255), (snake[i][0], snake[i][1], 10, 10))

    # Draw the food
    pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], 10, 10))

    # Update the screen
    pygame.display.update()