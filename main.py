import pygame
#from constants import * # This lets you use the variable, method, class names directly
import constants # with this you have to prefix everything with contants.
import player as playerLib
import asteroid as asteroidLib
import asteroidfield 
import shot as shotLib
import sys

def main():
    print("Starting Asteroids!")
    numpass, numfail = pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteros = pygame.sprite.Group()

    asteroidfield.AsteroidField.containers = updatable
    asteroidLib.Asteroid.containers = (asteros, updatable, drawable)
    playerLib.Player.containers = (updatable, drawable)
    shotLib.Shot.containers = (updatable, drawable, shots)


    asteroid_field = asteroidfield.AsteroidField() 
    player = playerLib.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    dt = 0
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        screen.fill((0,0,0))
        

        for each_asteroid in asteros:
            if each_asteroid.check_collision(player):
                print("Game over!")
                sys.exit()
            for each_shot in shots:
                if each_shot.check_collision(each_asteroid):
                    each_shot.kill()
                    each_asteroid.split()


        for each_drawable in drawable:
            each_drawable.draw(screen) 
        pygame.display.flip()

        #Delta time is calculated (/1000 is for miliseconds)
        dt = clock.tick(60) / 1000
    
    


# This line ensures that main is invoked if only that main.py is executed, if we did not encapsulate the main invocation inside this
# if statement, than when this file is imported to another program (file) main will be called, this is the pythonic way (use it)
# otherwise it would still work, this is just a good habit to have.

if __name__ == "__main__":
    main()