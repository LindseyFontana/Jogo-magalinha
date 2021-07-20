import pygame
from pygame.sprite import Sprite
import time
from random import randint
from musica import Musica

class Alien(Sprite):
    """Uma classe que representa um único aliengena da frota."""
    def __init__(self, config, tela):
        """Inicializa o alienígena e define sua posição inicial."""
        super().__init__()
        self.tela = tela
        self.config = config
        self.começo_explosão = None

        #Carrega a imagem do alienígena e define seu atributo rect
        self.image = pygame.image.load('imagens/rod.bmp')
        self.rect = self.image.get_rect()

        #Inicia cada novo alienígena próximo à parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do alienígena
        self.x = float(self.rect.x)

        #Armazena hora atual
        self.horário_da_explosão = time.gmtime()

    def blitme(self):
        """Desenha o alienígena em sua posição atual."""
        self.tela.blit(self.image, self.rect)

    def checa_direção(self):
        """Devolve True se o alienígena estiver na borda da tela."""
        tela_rect = self.tela.get_rect()
        if self.rect.right >= tela_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move o alienígena para a direita ou para a esquerda."""
        self.x += (self.config.fator_velocidade_alien * self.config.direção_frota)
        self.rect.x = self.x

    def explode(self, aliens, explosões):
        numero_aleatorio = randint(0, 1)
        if numero_aleatorio == 1:
            self.image = pygame.image.load('imagens/explosão.bmp')
        else:
            self.image = pygame.image.load('imagens/smack.bmp')
        self.começo_explosão = time.time()
        self.remove(aliens)
        self.add(explosões)