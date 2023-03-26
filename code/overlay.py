import pygame
from settings import *


class Overlay:
    def __init__(self, player):

        self.display_surface = pygame.display.get_surface()
        self.player = player

        overlay_path = './graphics/overlay/'
        self.tools_surf = {tool: pygame.image.load(
            f'{overlay_path}{tool}.png').convert_alpha() for tool in player.tools}
        self.seeds_surf = {seed: pygame.image.load(
            f'{overlay_path}{seed}.png').convert_alpha() for seed in player.seeds}
        print(self.tools_surf)
        print(self.seeds_surf)

    def display(self):

        tool_surf = self.tools_surf[self.player.selected_tool]
        self.display_surface.blit(tool_surf, (0, 0))