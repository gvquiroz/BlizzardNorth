#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from xml.dom import minidom, Node
from os.path import basename
import sys

from utils import *

class Map:
	def __init__(self, name):
		# Nombre del fichero xml que contiene el mapa.
		self.name = name
		# Capas del mapa.
		self.layers = []
		# Tilesets que usa el mapa.
		self.tilesets = []
		# Ancho del mapa en tiles.
		self.width = 0
		# Alto del mapa en tiles.
		self.height = 0
		# Obstáculos en el mapa.
		self.collisions = pygame.sprite.Group()
		#Cambios de escena en el mapa
		self.changeScene = pygame.sprite.Group()
		#Objetos
		self.objetos = pygame.sprite.Group()

		self.loadMap()

	def loadMap(self):
		'''Carga un mapa desde un fichero xml.'''
		xmlMap = minidom.parse("../mapas/"+self.name)
		mainNode = xmlMap.childNodes[0]

		self.width = int(mainNode.attributes.get("width").value)
		self.height = int(mainNode.attributes.get("height").value)

		for i in range(len(mainNode.childNodes)):
			if mainNode.childNodes[i].nodeType == 1:
				if mainNode.childNodes[i].nodeName == "tileset":
					tileset = Tileset(mainNode.childNodes[i])
					self.tilesets.append(tileset)
				if mainNode.childNodes[i].nodeName == "layer":
					layer = Layer(mainNode.childNodes[i])
					self.layers.append(layer)
					if layer.name == 'Colisiones': self.collisions = layer.getCollisions(self.tilesets[0].tile_size)
					if layer.name == 'CambiosEscena': self.changeScene = layer.getChangeScene(self.tilesets[0].tile_size)
					if layer.name == 'Objetos': self.objetos = layer.getObjetos(self.tilesets[0].tile_size)
					
	def drawCollisions(self, screen):
		'''Dibuja en el mapa los tiles de colisión.'''
		self.collisions.draw(screen)

	def drawBackground(self, screen):
		'''Dibuja la imagen de fondo en la pantalla.'''
		screen.blit(self.background, (0,0))

	def drawFloor(self, screen):
		'''Dibuja en pantalla la primera capa.'''
		self.layers[0].drawLayer(screen, self.tilesets)

	def drawObstacles(self, screen):
		'''Dibuja en pantalla la segunda capa.'''
		self.layers[1].drawLayer(screen, self.tilesets)

	def drawAir(self, screen):
		'''Dibuja en pantalla la tercera capa.'''
		self.layers[2].drawLayer(screen, self.tilesets)
		
	def drawChangeScene(self, screen):
		self.changeScene.draw(screen)
	
	def drawMap(self, screen):
		'''Dibuja el mapa.'''
		self.drawBackground(screen)
		self.drawFloor(screen)
		self.drawObstacles(screen)
		self.drawAir(screen)
		#self.drawCollisions(screen)

class Tileset:
	def __init__(self, tilesetNode):
		tilewidth = tilesetNode.attributes.get("tilewidth").value
		tileheight = tilesetNode.attributes.get("tileheight").value
		firstgid = tilesetNode.attributes.get("firstgid").value
		name = tilesetNode.childNodes[1].attributes.get("source").value
		# ID del primer tile.
		self.firstgid = int(firstgid)
		# Nombre del fichero imagen del tileset.
		self.name = basename(name).encode('ascii')
		# Tamaño de un tile.
		self.tile_size = (int(tilewidth), int(tileheight))
		# Tamaño de la imagen.
		self.image_size = (0,0)
		# Tabla de tiles.
		self.table = []

		self.loadTileset()

	def loadTileset(self):
		'''Carga la tabla de tiles.'''
		image = loadImage('../graficos/tilesets/'+self.name, True)
		self.image_size = image.get_size()
		for tile_x in range(0, self.image_size[0]/self.tile_size[0]):
			line = []
			self.table.append(line)
			for tile_y in range(0, self.image_size[1]/self.tile_size[1]):
				rect = (tile_x*self.tile_size[0], tile_y*self.tile_size[1], self.tile_size[0], self.tile_size[1])
				line.append(image.subsurface(rect))

	def drawTile(self, id, posx, posy, screen):
		'''Dibuja un tile en una posición dada.'''
		id = id - (self.firstgid-1)
		y = id/len(self.table)
		if id%len(self.table) == 0: y-=1
		x = (id - len(self.table)*y)-1
		screen.blit(self.table[x][y], (posx*self.tile_size[0],posy*self.tile_size[1]))


class Layer:
	def __init__(self, layerNode):
		layer = decode(layerNode.childNodes[1].childNodes[0].data.replace("\n", "").replace(" ", ""))
		# Número de tiles por fila (ancho de la capa medido en tiles).
		self.width = int(layerNode.attributes.get("width").value)
		# Número de filas de tiles (alto de la capa medido en tiles).
		self.height = int(layerNode.attributes.get("height").value)
		# Nombre de la capa.
		self.name = layerNode.attributes.get("name").value
		# Matriz de ID's que representan los tiles de cada posición de la capa.
		self.matrix = psplit(layer, self.width)
		#self.printLayer()

	def getCollisions(self, tile_size):
		'''Obtiene los puntos de colisión de una capa.
		Devuelve un grupo de Sprites que representa las zonas de colisión.'''
		collisions = pygame.sprite.Group()
		for i in range(0,len(self.matrix)):
			for j in range(0,len(self.matrix[i])):
				id = self.matrix[i][j]
				if id!=0:
					sprite = pygame.sprite.Sprite(collisions)
					sprite.image = pygame.Surface(tile_size)
					sprite.rect = sprite.image.get_rect()
					sprite.rect.left = j*tile_size[0]
					sprite.rect.top = i*tile_size[1]
		return collisions
		
	def getChangeScene(self, tile_size):
		'''Obtiene los puntos de colisión de una capa.
		Devuelve un grupo de Sprites que representa las zonas de colisión.'''
		changeScene = pygame.sprite.Group()
		for i in range(0,len(self.matrix)):
			for j in range(0,len(self.matrix[i])):
				id = self.matrix[i][j]
				if id!=0:
					sprite = pygame.sprite.Sprite(changeScene)
					sprite.image = pygame.Surface(tile_size)
					sprite.rect = sprite.image.get_rect()
					sprite.rect.left = j*tile_size[0]
					sprite.rect.top = i*tile_size[1]
		return changeScene
		
	def getObjetos(self, tile_size):
		'''Obtiene los puntos de colisión de una capa.
		Devuelve un grupo de Sprites que representa las zonas de colisión.'''
		objetos = pygame.sprite.Group()
		for i in range(0,len(self.matrix)):
			for j in range(0,len(self.matrix[i])):
				id = self.matrix[i][j]
				if id!=0:
					sprite = pygame.sprite.Sprite(objetos)
					sprite.image = pygame.Surface(tile_size)
					sprite.rect = sprite.image.get_rect()
					sprite.rect.left = j*tile_size[0]
					sprite.rect.top = i*tile_size[1]
		return objetos	


	def drawLayer(self, screen, tilesets):
		'''Dibuja una capa.'''
		for i in range(0,len(self.matrix)):
			for j in range(0,len(self.matrix[i])):
				id = self.matrix[i][j]
				if id!=0:
					for k in range(0,len(tilesets)):
						if id >= tilesets[len(tilesets)-k-1].firstgid:
							tilesets[len(tilesets)-k-1].drawTile(id, j, i, screen)
							break
