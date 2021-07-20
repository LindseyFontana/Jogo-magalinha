import pygame.font

class Botão():

    def __init__(self, tela):
        '''Inicializa os atributor do botão'''
        self.tela = tela
        self.tela_rect = tela.get_rect()

        #Define as dimensões e as propriedades do botão
        self.botão_play = pygame.image.load('imagens/play.bmp')
        self.rect = self.botão_play.get_rect()

        #Constrói o objeto rect do botão e o centraliza
        self.rect.center = self.tela_rect.center

    def draw_botão(self):
        #Desenha um botão em branco e, em seguida, desenha a mensagem
        self.tela.blit(self.botão_play, self.rect)


