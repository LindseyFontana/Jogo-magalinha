import time

class Config():

    def __init__(self):
        '''Inicia as configurações estáticas do jogo'''

        # Configurações da tela
        self.tela_largura = 1350
        self.tela_altura = 700
        self.bg_color = (1, 52, 118)

        # Configurações da espaçonave
        self.nave_limit = 3

        #Configurações de projéteis
        self.balas_permitidas = 3

        # Configurações dos alienígenas
        self.velocidade_descida_frota = 25

        # Configurações das explosões
        self.começo_explosão = time.time()
        self.tempo_atual = time.time()

        # Tempo de duração da explosão, 1 equivale a 1 segundo
        self.duração_exploção = 1

        # A taxa com que a velocidade do jogo aumenta
        self.escala_velocidade = 1.3

        # A taxa com que os pontos de cada alienígena aumentam
        self.escala_pontuação = 1.5

        self.inicializa_configurações_dinamicas()

    def inicializa_configurações_dinamicas(self):
        '''Inicializa as configurações que mudam no decorrer do jogo.'''
        self.nave_fator_velocidade = 1.5
        self.bala_fator_velocidade = 1
        self.fator_velocidade_alien = 1

        # Direção_frota igual a 1 representa a direita; -1 representa a squerda
        self.direção_frota = 1

        # Pontuação
        self.pontos_alien = 50

    def aumenta_velocidade(self):
        """Aumenta as configurações de velocidade"""
        self.nave_fator_velocidade *= self.escala_velocidade
        self.bala_fator_velocidade *= self.escala_velocidade
        self.fator_velocidade_alien *= self.escala_velocidade
        self.pontos_alien = int(self.pontos_alien * self.escala_pontuação)