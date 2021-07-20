import pygame
from pygame.sprite import Sprite

class Nave(Sprite):

    def __init__(self, config, tela):
        # Inicia cada nova espaçonave e define sua posição inicial
        super().__init__()
        self.tela = tela
        self.config = config
        self.image = pygame.image.load('imagens/nave.bmp')
        self.rect = self.image.get_rect()
        self.image_rect = self.rect

        self.tela_rect = tela.get_rect()
        self.image_rect.centerx = self.tela_rect.centerx
        self.image_rect.bottom = self.tela_rect.bottom

        #Armazena um valor decimal  para o centro da espaçonave
        self.center = float(self.image_rect.centerx)
        self.image_rect.bottom = float(self.image_rect.bottom)

        #Flag de movimento
        self.movendo_direita = False
        self.movendo_esquerda = False
        self.movendo_cima = False
        self.movendo_baixo = False

    def atualiza(self):
        if self.movendo_direita and self.image_rect.right < self.tela_rect.right:
            self.center = self.center + self.config.nave_fator_velocidade
        if self.movendo_esquerda and self.image_rect.left > 0:
            self.center = self.center - self.config.nave_fator_velocidade
        if self.movendo_cima and self.image_rect.top > 0:
            self.image_rect.top = self.image_rect.top - self.config.nave_fator_velocidade
        if self.movendo_baixo and self.image_rect.bottom < self.tela_rect.bottom:
            self.image_rect.bottom = self.image_rect.bottom + self.config.nave_fator_velocidade

        self.image_rect.centerx = self.center

    def blitme(self):
        self.tela.blit(self.image, self.image_rect)

    def center_nave(self):
        """ Centraliza a espaçonave natela."""
        self.center = self.tela_rect.centerx
        self.image_rect.bottom = self.tela_rect.bottom
        self.movendo_direita = False
        self.movendo_esquerda = False
        self.movendo_cima = False
        self.movendo_baixo = False