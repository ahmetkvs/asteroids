import pygame
#from constants import * # This lets you use the variable, method, class names directly
import constants # with this you have to prefix everything with contants.
import player as playerLib

def main():
    print("Starting Asteroids!")
    numpass, numfail = pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = playerLib.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    dt = 0
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()

        #Delta time is calculated (/1000 is for miliseconds)
        dt = clock.tick(60) / 1000
    
    


# This line ensures that main is invoked if only that main.py is executed, if we did not encapsulate the main invocation inside this
# if statement, than when this file is imported to another program (file) main will be called, this is the pythonic way (use it)
# otherwise it would still work, this is just a good habit to have.

if __name__ == "__main__":
    main()