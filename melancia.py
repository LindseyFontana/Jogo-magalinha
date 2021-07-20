import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

class Melancia(Sprite):

    def __init__(self, config, tela, estatistica, musica):
        """Inicializa a espaçonave e define sua posição inicial."""
        super().__init__()
        self.tela = tela
        self.config = config
        self.image = pygame.image.load('imagens/melancia.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.rect.width = self.rect.width * 1.5
        self.estatistica = estatistica
        self.musica = musica

    def prep_melancias(self):
        """Mostra quantas melancias (vidas) restam."""
        self.melancias = Group()
        melancias_estouradas = self.config.nave_limit - self.estatistica.naves_left
        for numero_melancia in range(self.config.nave_limit):
            melancia = Melancia(self.config, self.tela, self.estatistica, self.musica)
            melancia.rect.x = 10 + numero_melancia * melancia.rect.width
            melancia.rect.y = 10
            melancia.rect.right = melancia.rect.right
            self.melancias.add(melancia)
            if self.melancia_esta_quebrada(melancias_estouradas, numero_melancia):
                melancia.image = pygame.image.load('imagens/melancia_aberta.bmp')
                self.musica.som_melancia_explode()
        self.melancias.draw(self.tela)

    def melancia_esta_quebrada(self, melancias_estouradas, numero_melancia):
        return melancias_estouradas > numero_melancia