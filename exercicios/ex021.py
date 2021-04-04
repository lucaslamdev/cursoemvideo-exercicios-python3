from pygame import mixer
from time import sleep
mixer.init()
mixer.music.load('mama.mp3')
mixer.music.play()
seg = int(0)
while (mixer.music.get_busy()):
    print(f'Rodando! Musica {seg}s')
    sleep(1)
    seg += 1
mixer.music.stop()
print('Terminou a Música!')
