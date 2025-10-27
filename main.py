import pygame
from menu import draw_menu
import playing
from save_manager import save_exists

pygame.init()

# --- screen/caption setup ---
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("EVERLONG")

# --- game state ---
game_state = "menu"
run = True
clock = pygame.time.Clock()

# -- tracker whether to start a new game or load saved 
next_game_mode = True # default ot new game

# --- Main Loop ---
while run:

    # --- closing down the game cleanly using the x ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if game_state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = event.pos

                # --- get button rects and load status from menu
                buttons = draw_menu(screen)

                # --- check clicks ---
                if buttons["quit"].collidepoint(pos):
                    print("Quit button clicked")
                    run = False
                
                elif buttons["new_game"].collidepoint(pos):
                    print("New Game button clicked")
                    game_state = 'running'
                    playing.run_game(new_game=True)

                elif buttons["load"].collidepoint(pos):
                    if buttons["can_load"]:
                        print("Load button clicked")
                        game_state = "playing"
                        playing.run_game(new_game=False)
                    else:
                        print("No save file found - Load disabled")

                elif buttons["Settings"].collidepoint(pos):
                    print("Settings button clicked")
            
            elif game_state == "playing":
                # Launch the game loop inside playing.py
                # and wait for it to finish or return a state
                result = playing.run_game(new_game=next_game_mode)

                # When playing.py exits - decide what to do next
                if result == "menu":
                    print("Retuned to menu from playing")
                    game_state = "menu"

                elif result == "quit":
                    print("Quitting from playing")
                    run = False

    # --- draw background ---
    screen.fill((0, 0, 0))

    # --- draw current scene ---
    if game_state == "menu":
        draw_menu(screen)
    
    elif game_state == "playing":
        
        pass

    pygame.display.flip()
    clock.tick(60)

pygame.quit()