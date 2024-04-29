import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball properties
BALL_RADIUS = 15
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))

# Paddle properties
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
paddle_speed = 7
left_paddle_x = 50
left_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
right_paddle_x = WIDTH - 50 - PADDLE_WIDTH
right_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2

# Score
left_score = 0
right_score = 0
font = pygame.font.Font(None, 36)

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y < HEIGHT - PADDLE_HEIGHT:
        left_paddle_y += paddle_speed
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y < HEIGHT - PADDLE_HEIGHT:
        right_paddle_y += paddle_speed

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collisions with walls
    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_speed_y *= -1

    # Ball collisions with paddles
    if ball_x <= left_paddle_x + PADDLE_WIDTH and left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT:
        ball_speed_x *= -1
    elif ball_x >= right_paddle_x and right_paddle_y <= ball_y <= right_paddle_y + PADDLE_HEIGHT:
        ball_speed_x *= -1

    # Ball out of bounds
    if ball_x <= 0:
        right_score += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))
    elif ball_x >= WIDTH:
        left_score += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddles
    pygame.draw.rect(screen, WHITE, pygame.Rect(left_paddle_x, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, pygame.Rect(right_paddle_x, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw ball
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)

    # Draw score
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 50))
    screen.blit(right_text, (WIDTH * 3 // 4, 50))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
