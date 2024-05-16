from screeninfo import get_monitors

#ajusta o tamanho da tela para o tamanho do monitor principal da pessoa
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

