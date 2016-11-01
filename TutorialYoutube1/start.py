import pygame as pg
import time
import random

pg.init()

display_width = 800
display_height = 600

black = (0, 0, 0, 0)
white = (255, 255, 255, 255)

car_width = 50
car_height = 100

gameDisplay = pg.display.set_mode((display_width, display_height))
pg.display.set_caption('Fast Racer')
clock = pg.time.Clock()

carImg = pg.image.load('small_car.png')

#def things_dodged(count):
    

def things(thingx, thingy, thingw, thingh, color):
    pg.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x, y):
    gameDisplay.blit(carImg, (x, y)) #draw

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    
def message_display(text):
    largeText = pg.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pg.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('You Crashed')
    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.80)

    x_change = 0
    y_change = 0
    
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    gameExit = False

    while not gameExit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT: 
                    x_change = -5
                elif event.key == pg.K_RIGHT: 
                    x_change = 5
                elif event.key == pg.K_UP:
                    y_change = -5
                elif event.key == pg.K_DOWN:
                    y_change = 5
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                    x_change = 0
                elif event.key == pg.K_UP or event.key == pg.K_DOWN:
                    y_change = 0

            #if argmode == "debug": print(event)
        x += x_change
        y += y_change

        gameDisplay.fill(white)
        
        #things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        car(x, y)
        
        if x > display_width - car_width or x < 0:
            crash()
        
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            
        if thing_starty < y + car_height and thing_starty + thing_height > y:
            if thing_startx < x + car_width and thing_startx + thing_width > x:
                crash()
        
        pg.display.update() #refresh the entity provided as the pareameter
        clock.tick(60)
        
game_loop()
pg.quit()
quit()