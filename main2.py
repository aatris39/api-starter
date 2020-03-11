import requests
import pygame
from PIL import Image
pygame.init()




x = 300 
y = 500

win = pygame.display.set_mode((x, y))


URL = "http://placekitten.com/" + str(x) + "/" + str(y) 
CURL = "https://catfact.ninja/fact?max_length=140"

win.blit(URL, (x, y))

res = requests.get(URL)
res = res.json()

print(res)
