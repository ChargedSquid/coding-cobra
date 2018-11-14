# coding-cobra's stopwatch

import pygame
import time
import random

pygame.init()

num = 0
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Stopwatch')
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255) 
crashed = False
count = False
    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/3))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
def submessage_display(text):
    SmallText = pygame.font.Font('freesansbold.ttf',60)
    TextSurf, TextRect = text_objects(text, SmallText)
    TextRect.center = ((display_width/2),(display_height/2.1))
    gameDisplay.blit(TextSurf, TextRect)   

def lbutton_display(text):
    lXsmalltext = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, lXsmalltext)
    TextRect.center = ((100),(500))
    gameDisplay.blit(TextSurf, TextRect) 

def mbutton_display(text):
    mXsmalltext = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, mXsmalltext)
    TextRect.center = ((400),(500))
    gameDisplay.blit(TextSurf, TextRect)
    
def rbutton_display(text):
    rXsmalltext = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, rXsmalltext)
    TextRect.center = ((700),(500))
    gameDisplay.blit(TextSurf, TextRect) 
    
while not crashed:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
        
    gameDisplay.fill(white)
    
    pygame.draw.rect (gameDisplay, black, [50, 450, 100, 100])
    pygame.draw.rect (gameDisplay, black, [350, 450, 100, 100])
    pygame.draw.rect (gameDisplay, black, [650, 450, 100, 100])

    if mouse[0] >= 60 and mouse[0] <= 140 and mouse[1] >= 460 and mouse[1] <= 540 and click[0] == 1:
        pygame.draw.rect (gameDisplay, (200, 200, 200), [60, 460, 80, 80])
        count = True
    else:
        pygame.draw.rect (gameDisplay, white, [60, 460, 80, 80])

    lbutton_display('Start')

    if mouse[0] >= 360 and mouse[0] <= 440 and mouse[1] >= 460 and mouse[1] <= 540 and click[0] == 1:
        pygame.draw.rect (gameDisplay, (200, 200, 200), [360, 460, 80, 80])
        count = False
    else:
        pygame.draw.rect (gameDisplay, white, [360, 460, 80, 80])

    mbutton_display('Stop')

    if mouse[0] >= 660 and mouse[0] <= 740 and mouse[1] >= 460 and mouse[1] <= 540 and click[0] == 1:
        pygame.draw.rect (gameDisplay, (200, 200, 200), [660, 460, 80, 80])
        num = 0
    else:
        pygame.draw.rect (gameDisplay, white, [660, 460, 80, 80])

    rbutton_display('Reset')
    
    if count == True:
        message_display(str(int(num)))
        num += 0.04
    else:
        message_display(str(int(num)))
    submessage_display('Seconds')
    pygame.display.update()
    clock.tick(25)

pygame.quit()
quit()
