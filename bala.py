import pygame
from pygame.sprite import Sprite

class Bala(Sprite):

    def __init__(self, config, tela, nave):
        super().__init__()
        self.tela = tela

        #Cria um retângulo para o projétil em (0, 0) e, após, define a  posição correta
        self.bala = pygame.image.load('imagens/gato-pequeno.png')
        self.rect = self.bala.get_rect()
        self.bala_rect = self.rect
        self.bala_rect.centerx = nave.image_rect.centerx
        self.bala_rect.bottom = nave.image_rect.top

        #Armazena a posição da bala como decimal
        self.y = float(self.bala_rect.y)

        self.fator_velocidade = config.bala_fator_velocidade

    def update(self):
        '''Move o projétil para cima na tela.'''
        #Atualiza a posição decimal do projétil
        self.y -= self.fator_velocidade
        #Atualiza a posição de rect
        self.bala_rect.y = self.y

    def desenha_bala(self):
        '''Desenha o projétil na tela.'''
        self.tela.blit(self.bala, self.bala_rect)