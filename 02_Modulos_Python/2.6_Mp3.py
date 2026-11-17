'''Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.'''

from pathlib import Path

import pygame


ARQUIVO_MP3 = Path(__file__).with_name("allwant.mp3")


def main():
    pygame.init()
    pygame.mixer.music.load(str(ARQUIVO_MP3))
    pygame.mixer.music.play()

    tela = pygame.display.set_mode((600, 220))
    pygame.display.set_caption("Tocador de MP3")
    fonte = pygame.font.SysFont(None, 30)
    relogio = pygame.time.Clock()
    pausado = False
    executando = True

    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    executando = False
                elif evento.key == pygame.K_SPACE:
                    if pausado:
                        pygame.mixer.music.unpause()
                        pausado = False
                    elif pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                        pausado = True
                    else:
                        pygame.mixer.music.play()
                elif evento.key == pygame.K_s:
                    pygame.mixer.music.stop()
                    pausado = False
                elif evento.key == pygame.K_r:
                    pygame.mixer.music.play()
                    pausado = False

        tela.fill((30, 30, 30))
        status = "Pausado" if pausado else (
            "Reproduzindo" if pygame.mixer.music.get_busy() else "Parado"
        )
        linhas = (
            ("Tocador de MP3", (220, 220, 220)),
            (f"Arquivo: {ARQUIVO_MP3.name}", (180, 180, 180)),
            (f"Status: {status}", (100, 220, 140)),
            (
                "Espaco: pausar/continuar | S: parar | R: reiniciar | Esc: sair",
                (220, 220, 220),
            ),
        )

        for indice, (texto, cor) in enumerate(linhas):
            imagem = fonte.render(texto, True, cor)
            tela.blit(imagem, (20, 20 + indice * 45))

        pygame.display.flip()
        relogio.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()