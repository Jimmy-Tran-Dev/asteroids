import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids with pygame version: ", pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    
    dt = 0
    clock =pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = updatable, drawable
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        for drawing in drawable:
            drawing.draw(screen)
        updatable.update(dt)
        
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000.0
        


if __name__ == "__main__":
    main()
