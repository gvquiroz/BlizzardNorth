# -*- encoding: utf-8 -*-

# M�dulos
import pygame
from pygame.locals import *
import sys
import utils

WIDTH = 960
HEIGHT = 800

class Director:
    """Representa el objeto principal del juego.

    El objeto Director mantiene en funcionamiento el juego, se
    encarga de actualizar, dibuja y propagar eventos.

    Tiene que utilizar este objeto en conjunto con objetos
    derivados de Scene."""

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Yggdrasil")
        icon = pygame.image.load("../graficos/odin.png")
        pygame.display.set_icon(icon)
        self.scene = None
        self.fullscreen = False
        self.quit_flag = False
        self.mapa = None
        self.clock = pygame.time.Clock()

    def loop(self):
        "Pone en funcionamiento el juego."

        while not self.quit_flag:
            time = self.clock.tick(60)
            # propaga eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            sys.exit(0)

            self.scene.on_event()

            # actualiza la escena
            self.scene.on_update()

            # dibuja la pantalla
            self.scene.on_draw(self.screen)
            pygame.display.flip()

    def change_scene(self, scene):
        "Altera la escena actual."
        self.scene = scene

    def quit(self):
        self.quit_flag = True
