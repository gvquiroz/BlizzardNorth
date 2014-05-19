#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import pygame
import escena
import mapas
import utils
import escena_principal
import director
import jugador

# Constantes


# Clases
# ---------------------------------------------------------------------

class EscenaJuego(escena.Escena):
    """Escena principal del juego"""
    
    def __init__(self, director):
		escena.Escena.__init__(self, director)
		self.m = mapas.Map('casita.tmx')
		self.jugador = jugador.Jugador(32, 32)
		self.jugador.posicionInicial(480, 400)
		
		
    def on_update(self):
		pass
		
    def on_event(self):
		keys = pygame.key.get_pressed()
		self.colisiones = self.m.collisions
		self.cambiosDeEscena = self.m.changeScene
		self.objetos = self.m.objetos
		self.jugador.mover(60, keys, self.colisiones, self.cambiosDeEscena, self.objetos)
		if self.jugador.cambiarEscena(self.jugador.rect, self.cambiosDeEscena):
			self.m = mapas.Map('escenario1.tmx')
			self.jugador.mover(60, keys, self.colisiones, self.cambiosDeEscena, self.objetos)
			self.jugador.posicionInicial(465, 240)
			pygame.time.wait(650)
			if self.jugador.interactuarObjeto(self.jugador.rect, self.objetos):
				if keys[K_z]:
					self.textoCartel, self.r_textoCartel = ("Bosque al sur", 550, 700)
					screen.blit(self.textoCartel, self.r_textoCartel)
		self.cambiosDeEscena = self.m.changeScene
		self.jugador.mover(60, keys, self.colisiones, self.cambiosDeEscena, self.objetos)	
		if self.jugador.cambiarEscena(self.jugador.rect, self.cambiosDeEscena):
			if (self.jugador.rect.centerx < 480 and self.jugador.rect.centerx > 448 ) and (self.jugador.rect.centery < 256 and self.jugador.rect.centery > 224):
				self.m = mapas.Map('casita.tmx')
				self.jugador.mover(60, keys, self.colisiones, self.cambiosDeEscena, self.objetos)
				self.jugador.posicionInicial(496, 624)
				pygame.time.wait(650)
			else:
				self.m = mapas.Map('escenario2.tmx')
				self.jugador.mover(60, keys, self.colisiones, self.cambiosDeEscena, self.objetos)
				self.jugador.posicionInicial(465, 50)
				self.cambiosDeEscena = self.m.changeScene
				self.jugador.mover(60, keys, self.colisiones, self.cambiosDeEscena, self.objetos)
		#if self.jugador.cambiarEscena(self.jugador.rect, self.cambiosDeEscena):
			#self.m = mapas.Map('escenario1.tmx')			
			#self.jugador.mover(60, keys, self.colisiones, self.cambiosDeEscena, self.objetos)
			#self.jugador.posicionInicial(465, 750)
				
    def on_draw(self, screen):
		self.m.drawFloor(screen)
		self.m.drawObstacles(screen)
		self.jugador.dibujar(screen)
		self.m.drawAir(screen)
		
	
    #def exit(self):
        #if config.mapas.select_mapas == config.mapas.n_mapas-1:
            #escena = escena_principal.EscenaPrincipal(self.director)
            #self.director.change_scene(escena)
            #config.mapas.select_mapas = 0
            #return 0
        #config.mapas.select_mapas += 1
        #self.__init__(self.director)
        
# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------



# ---------------------------------------------------------------------

def main():
	pass

if __name__ == '__main__':
	main()

		
