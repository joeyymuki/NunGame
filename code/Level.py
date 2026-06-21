#!/usr/bin/python
# -*- coding: utf-8 -*-
from Const import WIN_WIDTH, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory
import pygame as pg


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):
        clock = pg.time.Clock()
        while True:
            clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return


            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pg.display.flip()