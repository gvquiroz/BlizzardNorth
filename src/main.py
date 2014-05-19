#!/usr/bin/env python
# -*- coding: utf-8 -*-

# M�dulos
import pygame
import director
import escena_principal

def main():
    dir = director.Director()
    escena = escena_principal.EscenaPrincipal(dir)
    dir.change_scene(escena)
    dir.loop()

if __name__ == '__main__':
    pygame.init()
    main()
