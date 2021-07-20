import sys
import pygame
from bala import Bala
from alien import Alien
import time

def checa_eventos_keydown(evento, config, tela, estatistica, botão_play, nave, aliens, balas, pontuação, musica, melancia):
    #Responde a pressionamentos de teclas.
    if evento.key == pygame.K_RIGHT:
        nave.movendo_direita = True
    elif evento.key == pygame.K_LEFT:
        nave.movendo_esquerda = True
    elif evento.key == pygame.K_UP:
        nave.movendo_cima = True
    elif evento.key == pygame.K_DOWN:
        nave.movendo_baixo = True
    elif evento.key == pygame.K_SPACE:
        atira_bala(config, tela, nave, balas)
    elif evento.key == pygame.K_ESCAPE:
        sys.exit()
    elif evento.key == pygame.K_RETURN or evento.key == pygame.K_KP_ENTER:
        enter_clicado = True
        mouse_x, mouse_y = pygame.mouse.get_pos()
        checa_botão_play(config, tela, estatistica, botão_play, nave, aliens, balas, pontuação, enter_clicado, mouse_x, mouse_y, musica, melancia)

def checa_eventos_keyup(evento, nave):
    #Responde a solturas de teclas.
    if evento.key == pygame.K_RIGHT:
        nave.movendo_direita = False
    elif evento.key == pygame.K_LEFT:
        nave.movendo_esquerda = False
    elif evento.key == pygame.K_UP:
        nave.movendo_cima = False
    elif evento.key == pygame.K_DOWN:
        nave.movendo_baixo = False

def checa_eventos(config, estatistica, tela, nave, aliens, balas, botão_play, pontuação, enter_clicado, musica, melancia):
    #Responde a eventos de pressionamento de teclas e de mouse.
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
           checa_eventos_keydown(evento, config, tela, estatistica, botão_play, nave, aliens, balas, pontuação, musica, melancia)
        elif evento.type == pygame.KEYUP:
           checa_eventos_keyup(evento, nave)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            checa_botão_play(config, tela, estatistica, botão_play, nave, aliens, balas, pontuação, enter_clicado, mouse_x, mouse_y, musica, melancia)

def checa_botão_play(config, tela, estatistica, botão_play, nave, aliens, balas, pontuação, enter_clicado, mouse_x, mouse_y, musica, melancia):
    """Inicia um novo jogo quando o jogador clicar em Play"""
    botão_clicado = botão_play.rect.collidepoint(mouse_x, mouse_y)
    if botão_clicado or enter_clicado and not estatistica.jogo_ativo:
        botão_play_clicado(config, estatistica, tela, nave, aliens, balas, pontuação, musica, melancia)

def botão_play_clicado(config, estatistica, tela, nave, aliens, balas, pontuação, musica, melancia):
        musica.interrompe_musica_rod()
        musica.interrompe_musica_ana()

        # Reinicia as configurações do jogo
        config.inicializa_configurações_dinamicas()

        # Reinicia os dados estatísticos do jogo

        estatistica.inicia_vidas()
        pontuação.prep_pontuação()
        melancia.prep_melancias()
        pontuação.prep_nivel()
        estatistica.jogo_ativo = True

        # Oculta o cursor do mouse
        pygame.mouse.set_visible(False)

        # Esvazia a lista de alienígenas e de projéteis
        aliens.empty()
        balas.empty()

        # Cria uma nova frota e centraliza a espaçonave
        cria_frota(config, tela, nave, aliens)
        nave.center_nave()

def reinicia_tela(config, estatistica, tela, nave, aliens, balas, explosões, botão_play, pontuação):
    tela.fill(config.bg_color)
    # Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
    for bala in balas.sprites():
        bala.desenha_bala()

    nave.blitme()
    aliens.draw(tela)
    explosões.draw(tela)

    # Desenha a informação sobre pontuação
    pontuação.mostra_pontuação()

    # Desenha o botão Play se o jogo estiver inativo
    if not estatistica.jogo_ativo:
        botão_play.draw_botão()

    # Deixa a tela mais recente visível
    pygame.display.flip()

def atira_bala(config, tela, nave, balas):
    '''Dispara um projétil se o limite ainda não foi alcançado'''
    #Cria um novo projétil e o adiciona ao  grupo de projéteis
    if len(balas) < config.balas_permitidas:
        nova_bala = Bala(config, tela, nave)
        balas.add(nova_bala)

def atualiza_balas(config, estatistica, tela, nave, aliens, balas, explosões, botão_play, pontuação,
                              musica, ana_ganha, melancia):
    '''Atualiza a posição dos projéteis e se livra dos projéteis antigos.'''
    #Atualiza as posições dos projéteis
    balas.update()

    # Livra-se dos projéteis que desapareceram
    for bala in balas.copy():
        if bala.bala_rect.bottom <= 0:
            balas.remove(bala)
    checa_balas_alien_collisions(config, estatistica, tela, nave, aliens, balas, explosões, botão_play, pontuação,
                              musica, ana_ganha, melancia)

def checa_balas_alien_collisions(config, estatistica, tela, nave, aliens, balas, explosões, botão_play, pontuação,
                              musica, ana_ganha, melancia):
    # Responde a colisões entre projéteis e alienígenas
    # Remove qualquer projétil e alienígena que tenha colidido

    collisions = pygame.sprite.groupcollide(aliens, balas, False, True)
    for alien_atingido in collisions:
        alien_atingido.explode(aliens, explosões)
        musica.som_bala()


    if collisions:
        for aliens in collisions.values():
            estatistica.pontuação += config.pontos_alien * len(aliens)
            pontuação.prep_pontuação()
        checa_maior_pontuação(estatistica, pontuação)

    if len(aliens) == 0:
        # Se a frota toda for destruída, inicia um novo nível
        balas.empty()
        explosões.empty()
        config.aumenta_velocidade()

        # Aumenta o nível
        estatistica.nivel += 1
        pontuação.prep_nivel()
        time.sleep(0.3)
        cria_frota(config, tela, nave, aliens)

        # Confere se o nívfel máximo foi atingido e finaliza o jogo
        if estatistica.nivel > 2:
            time.sleep(0.3)
            estatistica.jogo_ativo = False
            ana_ganha.mostra_tela_ana_ganha(config, estatistica, tela, nave, aliens, balas, explosões, botão_play, pontuação, musica, melancia)



def pega_numero_linhas(config, nave_altura, alien_altura):
    '''Determina o número de linhas com alienígenas que cabem na tela.'''
    espaço_disponivel_y = (config.tela_altura -
                           (2 * alien_altura) - nave_altura)
    numero_linhas = int(espaço_disponivel_y / (2 * alien_altura))
    return numero_linhas

def pega_numero_aliens_x(config, alien_largura):
    """Determina o número de alienígenas que cabem em uma linha."""
    espaço_disponivel_x = config.tela_largura - 1 * alien_largura
    numero_aliens_x = int(espaço_disponivel_x / (2 * alien_largura))
    return numero_aliens_x

def cria_alien(config, tela, aliens, numero_alien, numero_linha):
    #Cria um alienígena e posiciona na linha
    alien = Alien(config, tela)
    alien_largura = alien.rect.width
    alien.x = alien_largura + 2 * alien_largura * numero_alien
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * numero_linha
    aliens.add(alien)

def cria_frota(config, tela, nave, aliens):
    '''Cria uma frota completa de alienígenas.'''
    #Cria um alienígena e calcula o númeto de alienígenas em uma linha
    alien = Alien(config, tela)
    numero_aliens_x = pega_numero_aliens_x(config, alien.rect.width)
    numero_linhas = pega_numero_linhas(config, nave.image_rect.height, alien.rect.height)

    # Cria a primeira liha de alienígenas
    for numero_linha in range(numero_linhas):
        for numero_alien in range(numero_aliens_x):
            cria_alien(config, tela, aliens, numero_alien, numero_linha)

def checa_direção_frota(config, aliens):
    '''Responde apropriadamente se algum alienígena alcançou uma borda.'''
    for alien in aliens.sprites():
        if alien.checa_direção():
            muda_direção_frota(config, aliens)
            break

def muda_direção_frota(config, aliens):
    """Faz toda a frota descer e muda sua direção."""
    for alien in aliens.sprites():
        alien.rect.y += config.velocidade_descida_frota
    config.direção_frota *= -1

def nave_hit(config, estatistica, tela, nave, aliens, balas, melancia):
    """Responde ao fato de a espaçonave ter sido atingida por um alienígena."""
    # Decrementa naves_left
    if estatistica.naves_left > 0:
        #Descrementa nave_left
        estatistica.naves_left -= 1
        # Atualiza o painel de pontuações
        melancia.prep_melancias()

        # Esvazia a lista de alienígenas e de projéteis
        balas.empty()
        aliens.empty()

        # Faz uma pausa no jogo
        time.sleep(1)

        # Cria uma nova frota e centraliza a espaçonave
        nave.center_nave()
        cria_frota(config, tela, nave, aliens)

def termina_jogo(config, estatistica, tela, nave, aliens, balas, explosões, botão_play, pontuação, musica, rod_ganha, melancia):
    if estatistica.naves_left == 0:
        estatistica.jogo_ativo = False
        rod_ganha.mostra_tela_rod_ganha(config, estatistica, tela, nave, aliens, balas, explosões, botão_play, pontuação, musica, melancia)

def checa_aliens_bottom(config, estatistica, tela, nave, aliens, balas, melancia):
    """Verifica se algum alienígena alcançou a parte inferior da tela."""
    tela_rect = tela.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= tela_rect.bottom:
            # Trata esse caso do mesmo modo que é feito quando a espaçonave é atingida
            nave_hit(config, estatistica, tela, nave, aliens, balas, melancia)
            break

def update_aliens(config, estatistica, tela, nave, aliens, balas, melancia):
    """Verifica se a frota está em uma das bordas e entao atualiza as posições"""
    checa_direção_frota(config, aliens)
    aliens.update()
    # Verifica se houve colisões entre alienígenas e a espaçonave
    if pygame.sprite.spritecollideany(nave, aliens):
        nave_hit(config, estatistica, tela, nave, aliens, balas, melancia)
    #Verifica se há algum alienígena que atingiu a parte inferior da tela
    checa_aliens_bottom(config, estatistica, tela, nave, aliens, balas, melancia)


def checa_maior_pontuação(estatistica, pontuação):
    """Verifica se há uma nova pontuação máxima."""
    if estatistica.pontuação > estatistica.maior_pontuação:
        estatistica.maior_pontuação = estatistica.pontuação
        pontuação.prep_maior_pontuação()