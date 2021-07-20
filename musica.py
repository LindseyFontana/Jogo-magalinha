import pygame
import time
pygame.init()

class Musica():

    def __init__(self):
        self.rod_ganha = pygame.mixer.Sound('musicas/linger.ogg')
        self.ana_ganha = pygame.mixer.Sound('musicas/folha_de_jurema.ogg')
        self.gato_mia = pygame.mixer.Sound('musicas/miado.ogg')
        pygame.mixer.music.load('musicas/melancia_explode.mp3')


    def reproduz_musica_rod(self):
        self.rod_ganha.play()

    def interrompe_musica_rod(self):
        pygame.mixer.pause()

    def reproduz_musica_ana(self):
        self.ana_ganha.play()

    def interrompe_musica_ana(self):
        pygame.mixer.pause()

    def som_melancia_explode(self):
        pygame.mixer.music.play()

    def som_bala(self):
        self.gato_mia.stop()
        self.gato_mia.play()