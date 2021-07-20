class Estatistica():
    """Armazena dados estatísticos da invasão Alienígena."""

    def __init__(self, config):
        """Inicializa os dados estatísticos"""
        self.config = config
        self.inicia_vidas()

        #Inicia o jogo em um estado ativo.
        self.jogo_ativo = False

        # A pontuação máxima jamais deverá ser reiniciada
        self.maior_pontuação = 0

    def inicia_vidas(self):
        """Inicializa os dados estataticos que podem mudar durante o jogo"""
        """Inicializa os dados estataticosque podem mudar durante o jogo"""
        self.naves_left = self.config.nave_limit
        self.pontuação = 0
        self.nivel = 1
