import os
import pygame
 

pygame.init()

text = os.environ.get('QOMOLO_ROBOT_ID')
font = pygame.font.Font(os.path.join(".", "simsun.ttc"), 100)
rtext = font.render(text, True, (255, 0, 0), (0, 0, 0))       #font 
 
pygame.image.save(rtext, "/scripts/pic/51.png")
