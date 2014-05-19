# -*- coding: utf-8 -*-

# Módulos
import pygame
from pygame.locals import *
import utils
import director

# Constantes


# Clases
# ---------------------------------------------------------------------

class Jugador(pygame.sprite.Sprite):
	"Clase que representa a un jugador ya sea humano o de la IA"
	def __init__(self, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.width = width
		self.height = height
		self.chara = utils.cortar_chara("../graficos/character_chico.png", 4, 4)
		self.imagen = self.chara[0][0]
		self.rect = self.imagen.get_rect()
		self.speed = 0.04
		
	def posicionInicial(self, posx, posy):
		self.rect.centery = posy
		self.rect.centerx = posx	
		
	def colisionar(self, rect, collisions):
		'''Comprueba si un rectángulo colisiona con cualquier otro de un grupo de sprites.'''
		for sprite in collisions:
			if sprite.rect.colliderect(rect): return True
		return False
		
	def cambiarEscena(self, rect, changeScene):
		'''Comprueba si un rectángulo colisiona con cualquier otro de un grupo de sprites.'''
		for sprite in changeScene:
			if sprite.rect.colliderect(rect): return True
		return False
		
	def interactuarObjeto(self, rect, objetos):
		'''Comprueba si un rectángulo colisiona con cualquier otro de un grupo de sprites.'''
		for sprite in objetos:
			if sprite.rect.colliderect(rect): return True
		return False			
	
	def cambiarVelocidad(self, speed):
		self.speed = speed
	
	def actualizarImagen(self, imagen):
		self.imagen = imagen
	
	def mover(self, time, keys, collisions, changeScene, objetos):
		
		if self.rect.top >= 0:
			if keys[K_UP]:
				self.imagen = self.chara[3][0]
				self.rect.centery -= self.speed * time
				if self.colisionar(self.rect, collisions):
					if keys[K_UP]:
						self.rect.centery -= -3
				#if self.cambiarEscena(self.rect, changeScene):
					#if keys[K_UP]:
						#self.rect.centery -= -3		
			if keys[K_UP] and keys[K_LSHIFT]:
				self.cambiarVelocidad(0.045)
				self.rect.centery -= self.speed * time
				if self.colisionar(self.rect, collisions):
					if keys[K_UP] and keys[K_LSHIFT]:
						self.rect.centery -= -6
				if keys[K_UP]:
					self.speed = 0.04
					self.rect.centery -= self.speed * time
		
		if self.rect.bottom <= director.HEIGHT:
			if keys[K_DOWN]:
				self.imagen = self.chara[0][0]
				self.rect.centery += self.speed * time
			if self.colisionar(self.rect, collisions):
				if keys[K_DOWN]:
					self.rect.centery += -2
			#if self.cambiarEscena(self.rect, changeScene):
				#if keys[K_DOWN]:
					#self.rect.centery += -3		
			if keys[K_DOWN] and keys[K_LSHIFT]:
				self.cambiarVelocidad(0.045)
				self.rect.centery += self.speed * time
				if self.colisionar(self.rect, collisions):
					if keys[K_DOWN] and keys[K_LSHIFT]:
						self.rect.centery += -6
				if keys[K_DOWN]:
					self.speed = 0.04
					self.rect.centery += self.speed * time
		
		if self.rect.left >= 0:
			if keys[K_LEFT]:
				self.imagen = self.chara[1][0]
				self.rect.centerx -= self.speed * time
			if self.colisionar(self.rect, collisions):
				if keys[K_LEFT]:
					self.rect.centerx -= -3
			#if self.cambiarEscena(self.rect, changeScene):
				#if keys[K_LEFT]:
					#self.rect.centerx -= -3		
			if keys[K_LEFT] and keys[K_LSHIFT]:
				self.cambiarVelocidad(0.045)
				self.rect.centerx -= self.speed * time
				if self.colisionar(self.rect, collisions):
					if keys[K_LEFT] and keys[K_LSHIFT]:
						self.rect.centerx -= -6
				if keys[K_LEFT]:
					self.speed = 0.04
					self.rect.centerx -= self.speed * time
		
		if self.rect.right <= director.WIDTH:
			if keys[K_RIGHT]:
				self.imagen = self.chara[2][0]
				self.rect.centerx += self.speed * time
			if self.colisionar(self.rect, collisions):
				if keys[K_RIGHT]:
					self.rect.centerx += -2
			#if self.cambiarEscena(self.rect, changeScene):
				#if keys[K_RIGHT]:
					#self.rect.centerx += -3
			if keys[K_RIGHT] and keys[K_LSHIFT]:
				self.cambiarVelocidad(0.045)
				self.rect.centerx += self.speed * time
				if self.colisionar(self.rect, collisions):
					if keys[K_RIGHT] and keys[K_LSHIFT]:
						self.rect.centerx += -6
				if keys[K_RIGHT]:
					self.speed = 0.04
					self.rect.centerx += self.speed * time
					
	def dibujar(self, screen):
		screen.blit(self.imagen, self.rect)
		
# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------



# ---------------------------------------------------------------------

def main():
	pass

if __name__ == '__main__':
	main()
