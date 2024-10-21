import pygame as pg 
from game_objects import *
import sys

class Game:
    def __init__(self):
        pg.init()
        self.WINDOW_SIZE = 650
        self.TILE_SIZE = 50
        self.SCREEN = pg.display.set_mode([self.WINDOW_SIZE] * 2)
        self.clock = pg.time.Clock()
        self.new_game()
        
        # ? Manage score and game breakers
        self.font = pg.font.Font(None, 36)  # Score Font
        self.score = 0  # Init score
        self.paused = False  
        self.game_over = False  
    
    def draw_grid(self):
        [pg.draw.line(self.SCREEN, [50] * 3, (x, 0), (x, self.WINDOW_SIZE)) for x in range(0, self.WINDOW_SIZE, self.TILE_SIZE)]
        [pg.draw.line(self.SCREEN, [50] * 3, (0, y), (self.WINDOW_SIZE, y)) for y in range(0, self.WINDOW_SIZE, self.TILE_SIZE)]
    
    
    def new_game(self):
        self.snake = Snake(self)
        self.food = Food(self)
        self.score = 0  # ReInit score
        self.game_over = False  
    
    def update(self):
        if not self.paused and not self.game_over:
            self.snake.update()
        pg.display.flip()
        self.clock.tick(60)  # Frames Per Second
    
    def draw(self):
        self.SCREEN.fill('#0c0a3e')
        self.draw_grid()
        self.food.draw()
        self.snake.draw()
        
         # Draw score
        score_surface = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.SCREEN.blit(score_surface, (10, 10))

        # Game Over
        if self.game_over:
            game_over_surface = self.font.render('Game Over! Press R to Restart', True, (255, 0, 0))
            self.SCREEN.blit(game_over_surface, (self.WINDOW_SIZE // 2 - 150, self.WINDOW_SIZE // 2))
        
        # Pause
        if self.paused:
            pause_surface = self.font.render('Paused', True, (255, 255, 0))
            self.SCREEN.blit(pause_surface, (self.WINDOW_SIZE // 2 - 50, self.WINDOW_SIZE // 2 - 50))
    
    
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            
            # * Control the snake
            if not self.game_over:
                self.snake.control(event)

            # * Control the pause (P key)
            if event.type == pg.KEYDOWN and event.key == pg.K_p:
                self.paused = not self.paused  # Toggle pause

            # * Restart the game if game over (R key)
            if event.type == pg.KEYDOWN and event.key == pg.K_r and self.game_over:
                self.new_game()
        
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
    
if __name__ == '__main__':
    game = Game()
    game.run()