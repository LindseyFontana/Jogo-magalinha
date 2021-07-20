import pygame
from pygame.sprite import Group
from config import Config
from nave import Nave
import funções_jogo as fj
from estatistica import Estatistica
import time
from botão import Botão
from pontuação import Pontuação
from musica import Musica
from fim_jogo import RodGanha, AnaGanha
from melancia import Melancia


def inicia_jogo():
    #Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    config = Config()
    tela = pygame.display.set_mode(
        (config.tela_largura, config.tela_altura))
    pygame.display.set_caption("SUREIA")

    # Cria a espaçonave, um grupo de projéteis e um grupo de alienígenas
    nave = Nave(config, tela)
    balas = Group()
    aliens = Group()
    explosões = Group()
    musica = Musica()
    rod_ganha = RodGanha(config)
    ana_ganha = AnaGanha(config)

    # Cria o botão Play
    botão_play = Botão(tela)
    enter_clicado = False

    # Cria instância para armazenar estatística do jogo e cria painel de pontuação
    estatistica = Estatistica(config)
    melancia = Melancia(config, tela, estatistica, musica)
    pontuação = Pontuação(config, tela, estatistica, melancia)
    # mouse_x, mouse_y = pygame.mouse.get_pos()

    #Inicia o laço principal do jogo
    while True:
        nave
        fj.checa_eventos(config, estatistica, tela, nave, aliens, balas, botão_play, pontuação, enter_clicado, musica, melancia)
        if estatistica.jogo_ativo:
            nave.atualiza()
            fj.atualiza_balas(config, estatistica, tela, nave, aliens, balas, explosões, botão_play, pontuação,
                              musica, ana_ganha, melancia)
            fj.update_aliens(config, estatistica, tela, nave, aliens, balas, melancia)
            tempo_atual = time.time()
            for explosão in explosões:
                if tempo_atual >= explosão.começo_explosão + config.duração_exploção:
                    explosão.remove(explosões)
            fj.termina_jogo(config, estatistica, tela, nave, aliens, balas, explosões, botão_play, pontuação, musica, rod_ganha, melancia)

        # Redesenha a tela a cada passagem pelo laço
        fj.reinicia_tela(config, estatistica, tela, nave, aliens, balas, explosões, botão_play, pontuação)

inicia_jogo()
