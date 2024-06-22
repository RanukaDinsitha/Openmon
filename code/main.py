# Imports
from settings import *
from pytmx.util_pygame import load_pygame
from os.path import join
import pygame

from sprites import Sprite

class Game:
    def __init__(self):
        # Initial setup message
        launch = "Opénmon Launched"
        print(launch)

        # Initialize pygame
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Opénmon - Open Source Pokémon")

        # Groups

        # Load and set the game icon
        icon = pygame.image.load(join("..", "data", "images", "icon.png"))
        pygame.display.set_icon(icon)

        # Import game assets
        self.import_assets()

        # Setup the game with the loaded map
        self.setup(self.tmx_maps["world"])

    def import_assets(self):
        """Load all game assets such as maps."""
        self.tmx_maps = {"world": load_pygame(join("..", "data", "maps", "world.tmx"))}
        print("Assets imported:", self.tmx_maps)

    def setup(self, tmx_map):
        """Setup the game with the given TMX map."""
        # Print each tile in the Terrain layer of the map
        for x, y, surf in tmx_map.get_layer_by_name("Terrain").tiles():
            print(f"Tile at ({x * TILE_SIZE}, {y * TILE_SIZE}) with surface {surf}")

    def run(self):
        """Main game loop."""
        while True:
            # Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Exit message and cleanup
                    exited = "Opénmon Closed"
                    print(exited)
                    pygame.quit()
                    exit()

            # Game Logic (to be implemented)

            # Update the display
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()
