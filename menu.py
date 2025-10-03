import pygame

def draw_menu(screen):
    ''' Draws main menu on the screen '''
    font = pygame.font.Font(None, 50) # --- None = default font; 50 = size ---
    text = font.render("Press Enter to Play", True, (255, 255, 255))
    screen.blit(text, (350, 500)) # --- draws text at position x:500 y:500 --- # type: ignore ---