import pygame
pygame.init()
import sys
import pygame.font
import funções_jogo as fj

class FimJogo:

    def __init__(self, config):
        self.tela = pygame.display.set_mode(
            (config.tela_largura, config.tela_altura))
        self.tela_rect = self.tela.get_rect()

    def prep_botão_replay(self):
        self.botão_replay_rect = self.botão_replay.get_rect()
        self.botão_replay_rect.centerx = self.tela_rect.centerx
        self.botão_replay_rect.bottom = self.tela_rect.bottom - 60
        mouse_x, mouse_y = pygame.mouse.get_pos()

    def checa_eventos_replay(self, config, estatistica, tela, nave, aliens, balas, botão_play, pontuação, musica, melancia):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        while estatistica.jogo_ativo == False:
            # Deixa a tela mais recente visível
            pygame.display.flip()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    self.botão_replay_clicado = self.botão_replay_rect.collidepoint(mouse_x, mouse_y)
                    if self.botão_replay_clicado:
                        fj.botão_play_clicado(config, estatistica, tela, nave, aliens, balas, pontuação, musica, melancia)
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN or evento.key == pygame.K_KP_ENTER:
                        enter_clicado = True
                        fj.checa_botão_play(config, tela, estatistica, botão_play, nave, aliens, balas, pontuação, enter_clicado, mouse_x, mouse_y, musica, melancia)
                    elif evento.key == pygame.K_ESCAPE:
                        fj.checa_eventos_keydown(evento, config, tela, estatistica, botão_play, nave, aliens, balas, pontuação, musica, melancia)
                else:
                    None

class RodGanha(FimJogo):

    def __init__(self, config):
        #Armazena as imagens em variáveis
        super().__init__(config)
        self.rod_sorri = pygame.image.load('imagens/cebolinha-sorri.png')
        self.gato_chora = pygame.image.load('imagens/gato-chora.png')
        self.melancia = pygame.image.load('imagens/melancia_grande.bmp')
        self.botão_replay = pygame.image.load('imagens/restart.png')

        #Configurações de texto
        self.cor_texto = (253, 207, 0)
        self.fonte = pygame.font.SysFont(None, 60)

        # Prepara as imagens
        self.prep_rod()
        self.prep_cabeçalho(config)
        self.prep_melancia()
        self.prep_botão_replay()
        self.prep_gato()

    def prep_rod(self):
        self.rod_rect = self.rod_sorri.get_rect()
        self.rod_rect.right = self.tela_rect.right - 100
        self.rod_rect.top = 70

    def prep_gato(self):
        self.gato_rect = self.gato_chora.get_rect()
        self.gato_rect.left = self.tela_rect.left + 100
        self.gato_rect.bottom = self.tela_rect.bottom -90

    def prep_cabeçalho(self, config):
        cabeçalho = 'VOCÊ PERDEU !!'
        self.cabeçalho_image = self.fonte.render(cabeçalho, True, self.cor_texto, config.bg_color)
        self.cabeçalho_rect = self.cabeçalho_image.get_rect()
        self.cabeçalho_rect.centerx = self.tela_rect.centerx
        self.cabeçalho_rect.centery = self.tela_rect.top + 100

    def prep_melancia(self):
        self.melancia_rect = self.melancia.get_rect()
        self.melancia_rect.centerx = self.tela_rect.centerx + 10
        self.melancia_rect.centery = self.tela_rect.centery

    def mostra_tela_rod_ganha(self, config, estatistica, tela, nave, aliens, balas, explosões,
                              botão_play, pontuação, musica, melancia):
        # Limpa tela
        aliens.empty()
        balas.empty()
        explosões.empty()

        #Desenha tela
        self.tela.fill(config.bg_color)
        self.tela.blit(self.rod_sorri, self.rod_rect)
        self.tela.blit(self.cabeçalho_image, self.cabeçalho_rect)
        self.tela.blit(self.gato_chora, self.gato_rect)
        self.tela.blit(self.melancia, self.melancia_rect)
        self.tela.blit(self.botão_replay, self.botão_replay_rect)

        # Mantem cursor visivel
        pygame.mouse.set_visible(True)

        # Reproduz musica
        musica.reproduz_musica_rod()

        self.checa_eventos_replay(config, estatistica, tela, nave, aliens, balas, botão_play, pontuação, musica, melancia)

class AnaGanha(FimJogo):

    def __init__(self, config):
        # Armazena as imagens em variáveis
        super().__init__(config)
        self.ana_sorri = pygame.image.load('imagens/magali-sorri.png')
        self.gato_sorri = pygame.image.load('imagens/gato-sorri.png')
        self.suco = pygame.image.load('imagens/suco_de_melancia.bmp')
        self.botão_replay = pygame.image.load('imagens/restart.png')

        # Configurações de texto
        self.cor_texto = (253, 207, 0)
        self.fonte = pygame.font.SysFont(None, 60)

        # Prepara as imagens
        self.prep_ana()
        self.prep_cabeçalho(config)
        self.prep_suco_de_melancia()
        self.prep_botão_replay()
        self.prep_gato()

    def prep_ana(self):
        self.ana_rect = self.ana_sorri.get_rect()
        self.ana_rect.right = self.tela_rect.right - 100
        self.ana_rect.top = 70

    def prep_gato(self):
        self.gato_rect = self.gato_sorri.get_rect()
        self.gato_rect.left = self.tela_rect.left + 100
        self.gato_rect.bottom = self.tela_rect.bottom - 50

    def prep_cabeçalho(self, config):
        # Cabeçalho 1
        cabeçalho = 'PARABÉNS !!'
        self.fonte = pygame.font.SysFont(None, 80)
        self.cabeçalho_image = self.fonte.render(cabeçalho, True, self.cor_texto, config.bg_color)
        self.cabeçalho_rect = self.cabeçalho_image.get_rect()
        self.cabeçalho_rect.centerx = self.tela_rect.centerx
        self.cabeçalho_rect.centery = self.tela_rect.top + 100

        # Cabeçalho 2
        cabeçalho2 = 'Você ganhou'
        self.fonte = pygame.font.SysFont(None, 60)
        self.cabeçalho2_image = self.fonte.render(cabeçalho2, True, self.cor_texto, config.bg_color)
        self.cabeçalho2_rect = self.cabeçalho2_image.get_rect()
        self.cabeçalho2_rect.centerx = self.tela_rect.centerx
        self.cabeçalho2_rect.top = self.cabeçalho_rect.bottom + 10

    def prep_suco_de_melancia(self):
        self.suco_rect = self.suco.get_rect()
        self.suco_rect.centerx = self.tela_rect.centerx + 10
        self.suco_rect.centery = self.tela_rect.centery

    def mostra_tela_ana_ganha(self, config, estatistica, tela, nave, aliens, balas, explosões, botão_play, pontuação, musica, melancia):
        # Limpa tela
        aliens.empty()
        balas.empty()
        explosões.empty()

        # Desenha tela
        self.tela.fill(config.bg_color)
        self.tela.blit(self.ana_sorri, self.ana_rect)
        self.tela.blit(self.cabeçalho_image, self.cabeçalho_rect)
        self.tela.blit(self.cabeçalho2_image, self.cabeçalho2_rect)
        self.tela.blit(self.gato_sorri, self.gato_rect)
        self.tela.blit(self.suco, self.suco_rect)
        self.tela.blit(self.botão_replay, self.botão_replay_rect)

        # Deixa cursor visivel na tela
        pygame.mouse.set_visible(True)

        # Reproduz musica
        musica.reproduz_musica_ana()

        self.checa_eventos_replay(config, estatistica, tela, nave, aliens, balas, botão_play,
                                  pontuação, musica, melancia)