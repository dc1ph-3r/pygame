import pygame
from menu import draw_menu

pygame.init()

screen_width = 1000
screen_height = 1000

# --- screen/caption setup ---
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Ripply & Claret Game")

game_state = "menu"

run = True
# --- Main Loop ---
while run:

    # --- closing down the game cleanly using the x ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if game_state == "menu":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_state = "playing"
        
        elif game_state == "playing":

            # --- fill in what happens when playing the game ---
            pass
    
    # --- refreshing background ---
    screen.fill((0, 0, 0))

    # --- display menu ---
    if game_state == "menu":
        draw_menu(screen)

    # --- display playing ---
    elif game_state == "playing":
        
        pass # configure later

    pygame.display.flip()

pygame.quit()