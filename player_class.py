import pygame
import os

class Player:
    
    def __init__(self, pos, sprite_folder, scale=(48,48), speed=5):
        self.pos = pos
        self.speed = speed
        self.sprites = self.load_sprites(sprite_folder, scale)
        self.current_frame = 0
        self.animation_speed = 0.2

    def load_sprites(self, folder, scale):
        sprites = []
        for file_name in sorted(os.listdir(folder)):
            if file_name.endswith(".png"):
                img = pygame.image.load(os.path.join(folder, file_name)).convert_alpha()
                img = pygame.transform.scale(img, scale)
                sprites.append(img)
        return sprites
    
    def update(self):
        # ---handle movement---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.pos[0] -= self.speed
        if keys[pygame.K_RIGHT]:
            self.pos[0] += self.speed
        if keys[pygame.K_UP]:
            self.pos[1] -= self.speed
        if keys[pygame.K_DOWN]:
            self.pos[1] += self.speed
        
        # --- keep inside screen ---
        self.pos[0] = max(0, min(self.pos[0], 1000 - self.sprites[0].get_width()))
        self.pos[1] = max(0, min(self.pos[1], 800 - self.sprites[1].get_height()))

        # ---animate---
        self.current_frame += self.animation_speed
        if self.current_frame >= len(self.sprites):
            self.current_frame = 0
    
    def draw(self, screen):

        screen.blit(self.sprites[int(self.current_frame)], self.pos)