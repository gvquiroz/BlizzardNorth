#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import pygame
import sys
import escena
import utils
import escena_juego

# Constantes


# Clases
# ---------------------------------------------------------------------

class EscenaPrincipal(escena.Escena):
    """Escena inicial del juego, esta es la primera que se carga cuando inicia"""
    
    def __init__(self, director):
		escena.Escena.__init__(self, director)
		pygame.mixer.music.load("../musica/divano.mp3")
		pygame.mixer.music.play(-1, 0.0)
		self.menu = utils.loadImage('../graficos/menu/foto.png', True, (480, 400))
		self.espadita = utils.loadImage("../graficos/menu/espadita.png", True)
		self.r_espadita = self.espadita.get_rect()
		self.r_espadita.centerx = 310
		self.r_espadita.centery = 290
		
		self.texto_comenzar, self.r_texto_comenzar = utils.text("Comenzar", 490, 290)
		self.texto_salir, self.r_texto_salir = utils.text("Salir", 490, 490)
		
		self.option = 1 # Opción del menú que está seleccionada.
		
    def on_update(self):
        pass

    def on_event(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.change_option(1)
            pygame.time.wait(30)
        elif keys[pygame.K_UP]:
            self.change_option(-1)
            pygame.time.wait(30)
        elif keys[pygame.K_KP_ENTER] or keys[pygame.K_RETURN]:
            if self.option == 1:
               escena = escena_juego.EscenaJuego(self.director)
               self.director.change_scene(escena)
               pygame.time.wait(750)
               pygame.mixer.music.stop()
            if self.option == 2:
                sys.exit(0)
           

    def on_draw(self, screen):
        screen.fill((255, 255, 255))
        screen.blit(self.menu, (0,0))
        screen.blit(self.espadita, self.r_espadita)
        screen.blit(self.texto_comenzar, self.r_texto_comenzar)
        screen.blit(self.texto_salir, self.r_texto_salir)
        

    def change_option(self, option):
        if option == 1 and not self.option == 2:
            self.r_espadita.centery += 200
            self.option += 1
        if option == -1 and not self.option == 1:
            self.r_espadita.centery -= 200
            self.option -= 1

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------



# ---------------------------------------------------------------------

def main():
	pass

if __name__ == '__main__':
	main()
