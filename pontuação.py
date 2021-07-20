import pygame.font

class Pontuação():
    """Uma classe para mostrar informações sobre pontuação."""

    def __init__(self, config, tela, estatistica, melancia):
        """Inicializa os atributos da pontuação."""
        self.tela = tela
        self.tela_rect = tela.get_rect()
        self.config = config
        self.estatistica = estatistica
        self.melancia = melancia

        # Configurações de fonte para as informações de pontuação
        self.cor_texto = (253, 207, 0)
        self.fonte = pygame.font.SysFont(None, 40)

        # Prepara as imagens das pontuações iniciais
        self.prep_pontuação()
        self.prep_maior_pontuação()
        self.prep_nivel()
        self.melancia.prep_melancias()

    def prep_pontuação(self):
        """Transforma a pontução em uma imagem renderizada."""
        pont_arredondada = int(round(self.estatistica.pontuação, -1))
        pontuação_str = "Score : {:,}".format(pont_arredondada)
        self.pontuação_image = self.fonte.render(pontuação_str, True, self.cor_texto, self.config.bg_color)

        # Exibe a pontuação na parte superior direita da tela
        self.pontuação_rect = self.pontuação_image.get_rect()
        self.pontuação_rect.right = self.tela_rect.right - 20
        self.pontuação_rect.top = 10

    def mostra_pontuação(self):
        #Desenha a pontuação na tela.
        self.tela.blit(self.pontuação_image, self.pontuação_rect)
        self.tela.blit(self.maior_pontuação_image, self.maior_pontuação_rect)
        self.tela.blit(self.nivel_image, self.nivel_rect)
        self.melancia.prep_melancias()

    def prep_maior_pontuação(self):
        """Transforma a pontuação máxima em uma imagem renderizada"""
        maior_pont_arredondada = int(round(self.estatistica.maior_pontuação, -1))
        maior_pontuação_str = "HIGH SCORE: {:,}".format(maior_pont_arredondada)
        self.maior_pontuação_image = self.fonte.render(maior_pontuação_str, True, self.cor_texto, self.config.bg_color)

        # Centraliza a pontuação máxima na parte superior da tela
        self.maior_pontuação_rect = self.maior_pontuação_image.get_rect()
        self.maior_pontuação_rect.centerx = self.tela_rect.centerx
        self.maior_pontuação_rect.top = self.pontuação_rect.top

    def prep_nivel(self):
        """Transforma o nível em uma imagem renderizada."""
        nivel_image_int = int(self.estatistica.nivel)
        nivel_image_str = "Level : {:,}".format(nivel_image_int)
        self.nivel_image = self.fonte.render(nivel_image_str, True, self.cor_texto, self.config.bg_color)
        self.nivel_rect = self.nivel_image.get_rect()
        self.nivel_rect.right = self.pontuação_rect.right
        self.nivel_rect.top = self.pontuação_rect.bottom + 10
