import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(x=(SCREEN_WIDTH/2), y=(SCREEN_HEIGHT/2))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black")
        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)


        pygame.display.flip()
        
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
