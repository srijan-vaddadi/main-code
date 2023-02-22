import pygame

# Initialize pygame
pygame.init()

# Set the window size
win_width = 800
win_height = 600

# Create the window
win = pygame.display.set_mode((win_width, win_height))

# Load the car image
car_img = pygame.image.load("car.png")

# Set the initial position of the car
car_x = win_width // 2
car_y = win_height // 2

# Set the speed of the car
car_speed = 5

# Start the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys that are pressed
    keys = pygame.key.get_pressed()

    # Move the car based on the keys that are pressed
    if keys[pygame.K_UP]:
        car_y -= car_speed
    if keys[pygame.K_DOWN]:
        car_y += car_speed
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    # Clear the screen
    win.fill((255, 255, 255))

    # Draw the car
    win.blit(car_img, (car_x, car_y))

    # Update the screen
    pygame.display.update()

# Quit pygame
pygame.quit()
