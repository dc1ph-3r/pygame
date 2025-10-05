import pygame # type: ignore
import os

# ---colours---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)

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
    title = font.render("Welcome to EverLong", True, WHITE)
    screen.blit(title, (screen_width // 2 - title.get_width() // 2, 200))

    # ---BUTTONS---
    button_font = pygame.font.Font(None, 50)

    # ---BUTTON DIMENTIONS---
    button_width = 200  # ---BUTTON RECT WIDTH---
    button_height = 100 # ---BUTTON RECT HEIGHT---
    button_padding = 40 # ---SPACE BETWEEN THE BUTTONS---

    # ---Y POS FOR BUTTONS NEAR BOTTOM OF SCREEN---
    button_y = screen_height - 100

    # ---CALCULATE POS FOR SIDE BY SIDE LAYOUTS---
    total_width = button_width * 2 + button_padding
    left_x = (screen_width - total_width) // 2
    right_x = left_x + button_width + button_padding

    # ---DEFINE BUTTONS---
    play_button = pygame.Rect(left_x, button_y, button_width, button_height)
    quit_button = pygame.Rect(right_x, button_y, button_width, button_height)

    mouse_pos = pygame.mouse.get_pos()

    # ---PLAY BUTTON---
    if play_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, GREY, play_button, border_radius=10)
    else:
        pygame.draw.rect(screen, GREY, play_button, border_radius=10)
    play_text = button_font.render("Play", True, WHITE)
    screen.blit(play_text, play_text.get_rect(center=play_button.center))

    # ---Quit Button---
    if quit_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, GREY, quit_button, border_radius=10)
    else:
        pygame.draw.rect(screen, GREY, quit_button, border_radius=10)
    quit_text = button_font.render("Quit", True, WHITE)
    screen.blit(quit_text, quit_text.get_rect(center=quit_button.center))

    return play_button, quit_button