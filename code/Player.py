#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Entity import Entity
import pygame as pg


class Player(Entity):
    def __init__(self, name, position: tuple):
        super().__init__(name, position)
        self.speed_y = 0
        self.gravity = 0.5
        self.jump_force = -12



    def move(self, ):
        pressed_key = pg.key.get_pressed()

        if pressed_key[pg.K_a] and self.rect.left > 0:
            self.rect.x -= 4
        if pressed_key[pg.K_d] and self.rect.right < 640:
            self.rect.x += 3

        if pressed_key[pg.K_w] and self.on_ground:
            self.speed_y = self.jump_force
            self.on_ground = False

        self.speed_y += self.gravity
        self.rect.y += self.speed_y

        linha_do_chao = 300

        if self.rect.bottom >= linha_do_chao:
            self.rect.bottom = linha_do_chao
            self.speed_y = 0
            self.on_ground = True