import pygame
import sys

# Initialize pygame
pygame.init()
 
 # Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 7
BALL_SPEED = 7
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Initialize positions
player1_x, player1_y = 50, HEIGHT // 2 - PADDLE_HEIGHT // 2
player2_x, player2_y =  WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = BALL_SPEED, BALL_SPEED

# Scores
player1_score = 0
player2_score = 0

# Fonts
score_font = pygame.font.SysFont(None, 50)

# Function to reset ball position
def reset_ball():
    global ball_x, ball_y, ball_dx
    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    ball_dx = BALL_SPEED if ball_dx > 0 else -BALL_SPEED

# Function to update player 2(computer) paddle position
def update_player2():
    global player2_y
    if player2_y + PADDLE_HEIGHT //2 < ball_y:
        player2_y += PADDLE_SPEED
    elif player2_y + PADDLE_HEIGHT // 2 > ball_y:
        player2_y -= PADDLE_SPEED

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move paddle 1 (player) based on input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1_y < HEIGHT - PADDLE_HEIGHT:
            player1_y += PADDLE_SPEED

    # Update player 2 (computer) paddle position
    update_player2()

    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with paddles
    if ball_x <= player1_x + PADDLE_WIDTH and player1_y <= ball_y <= player1_y + PADDLE_HEIGHT:
        ball_dx = BALL_SPEED
    if ball_x >= player2_x - BALL_RADIUS and player2_y <= ball_y <= player2_y + PADDLE_HEIGHT:
        ball_dx = -BALL_SPEED

    # BALL collision with walls
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_RADIUS:
        ball_dy = -ball_dy

    # Ball out of bounds
    if ball_x <= 0:
        player2_score += 1
        reset_ball()
    elif ball_x >= WIDTH:
        player1_score += 1
        reset_ball()

    # Clear the screen
    screen.fill(BLACK)  

    # Draw paddle and ball
    pygame.draw.rect(screen, WHITE, (player1_x, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (player2_x, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), BALL_RADIUS)

    # Draw scores
    players1_text = score_font.render(str(player1_score), True, WHITE)
    players2_text = score_font.render(str(player2_score), True, WHITE)
    screen.blit(players1_text, (WIDTH // 2 - 50, 20))
    screen.blit(players2_text, (WIDTH // 2 + 25, 20))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)









