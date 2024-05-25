from screeninfo import get_monitors
import os
from dotenv import load_dotenv
#ajusta o tamanho da tela para o tamanho do monitor principal da pessoa
load_dotenv()
WIDTH = 0
HEIGHT = 0

for monitor in get_monitors():
    if monitor.is_primary == True:
        WIDTH = monitor.width
        HEIGHT = monitor.height
        break

SCREEN_SIZE = [WIDTH, HEIGHT]
FPS = 60
TILESIZE = 64
API_URL = os.getenv('API_URL')
