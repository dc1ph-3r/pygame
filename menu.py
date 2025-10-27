import pygame # type: ignore
import os
from save_manager import save_exists

# ---colours---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
DARK_GREY = (100, 100, 100) # ---used for disabled buttons---

def draw_menu(screen):

    '''Draws main menu on the screen'''
    # ---loads assets once on import ---
    BASE_DIR = os.path.dirname(__file__)
    bg_path = os.path.join(BASE_DIR, "assets", "Castle.png")
    bg_image = pygame.image.load(bg_path).convert()
    screen_width, screen_height = screen.get_size()
    scaled_bg = pygame.transform.scale(bg_image, (screen_width, screen_height))
    screen.blit(scaled_bg, (0, 0))

    # ---FONT---
    font = pygame.font.Font(None, 50)

    # ---DRAW TITLE TEXT---
    title = font.render("Welcome to EVERLONG", True, WHITE)
    screen.blit(title, (screen_width // 2 - title.get_width() // 2, 200))

    # ---BUTTONS---
    button_font = pygame.font.Font(None, 40)

    # ---BUTTON DIMENTIONS---
    button_width = 200  # ---BUTTON RECT WIDTH---
    button_height = 100 # ---BUTTON RECT HEIGHT---
    button_padding = 40 # ---SPACE BETWEEN THE BUTTONS---

    # ---Y POS FOR BUTTONS NEAR BOTTOM OF SCREEN---
    button_y = screen_height - 200

    # ---CALCULATE POS FOR SIDE BY SIDE LAYOUTS---
    total_width = button_width * 2 + button_padding
    left_x = (screen_width - total_width) // 2
    lefter_x = left_x - button_width - button_padding
    right_x = left_x + button_width + button_padding
    righter_x = left_x + button_width*2 + button_padding*2

    # ---DEFINE BUTTONS---
    load_button = pygame.Rect(left_x, button_y, button_width, button_height)
    quit_button = pygame.Rect(right_x, button_y, button_width, button_height)
    settings_button = pygame.Rect(righter_x, button_y, button_width, button_height)
    newgame_button = pygame.Rect(lefter_x, button_y, button_width, button_height)

    mouse_pos = pygame.mouse.get_pos()

    # ---check if save exists---
    can_load = save_exists()

    # ---Draw Buttons---
    def draw_button(rect, text, enabled=True):
        color = GREY if enabled else DARK_GREY
        pygame.draw.rect(screen, color, rect, border_radius=10)
        label = button_font.render(text, True, WHITE if enabled else (160, 160, 160))
        screen.blit(label, label.get_rect(center=rect.center))
    
    draw_button(newgame_button, "New Game", True)
    draw_button(load_button, "Load", can_load)
    draw_button(settings_button, "Settings", True)
    draw_button(quit_button, "Quit", True)

    # ---return the buttons and load status for main.py to handle clicks
    return {
        "new_game":newgame_button,
        "load":load_button,
        "quit":quit_button,
        "settings":settings_button,
        "can_load":can_load
    }