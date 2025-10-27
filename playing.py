import pygame
import os
import sys
from save_manager import save_exists, save_game, load_save
from player_class import Player

# ---COLOURS---
WHITE = (255,255,255)
BLACK = (0, 0, 0)
BLUE = (0, 120, 255)

def run_game(new_game=True):

    """
    This runs the main.py game loop.
    if new_game=True; starts fresh.
    if new_game=False; load save.
    """

    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("EVERLONG - playing")

    # ---load assets---
    BASE_DIR = os.path.dirname(__file__)
    bg_path = os.path.join(BASE_DIR, "assets", "Castle.png")

    # ---load and scale---
    background = pygame.image.load(bg_path).convert()
    background = pygame.transform.scale(background, (1000, 800))

    # ---Initialise player---
    if new_game or not save_exists():
        player_pos = [100, 100]
        level = 1
        score = 0
    else:
        data = load_save()
        player_pos = data.get("player_pos", [100, 100]) if data else [100, 100]
        level = data.get("level", 1) if data else 1
        score = data.get("score", 0) if data else 0

    player_sprite_folder = os.path.join(BASE_DIR, "assets", "sprite-sheets", "Warrior_1")
    player = Player(player_pos, player_sprite_folder, scale=(48, 48), speed=5)

    clock = pygame.time.Clock()

    # --- initialise game ---
    if new_game or not save_exists():
        print("Starting New Game ...")
        player_pos = [100, 100]
        level = 1
        score = 0
    else:
        print("Loading Saved Game ...")
        data = load_save()
        if data:
            player_pos = data.get("player_pos", [100, 100])
            level = data.get("level", 1)
            score = data.get("score", 0)
        else:
            # fallback in case something goes wrong
            player_pos = [100, 100]
            level = 1
            score = 0

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # --- escape key to exit --- will change this to show a settings menu later on
                if event.key == pygame.K_ESCAPE:
                    running = False

        # ---update player---
        player.update()

        # --- render ---
        screen.blit(background, (0, 0))
        player.draw(screen)

        # --- show simple hud ---
        font = pygame.font.Font(None, 36)
        hud_text = font.render(f"Level: {level} Score: {score}", True, WHITE)
        screen.blit(hud_text, (20, 20))

        pygame.display.flip() # update screen
        clock.tick(60)

    # --- when exiting, save progrss ---
    print("Saving game...")
    save_game({
        "player_pos": player_pos,
        "level": level,
        "score": score,
    })
    pygame.quit()
    print("Retuned to menu")
    return "menu"