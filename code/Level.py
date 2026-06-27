#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from asyncio import timeout
import random
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface
from code.EntityMediator import EntityMediator

from Const import WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE, COLOR_REDBLOOD, EVENT_ENEMY, SPAWN_TIME
from code.Entity import Entity
from code.EntityFactory import EntityFactory
import pygame as pg


class Level:
    def __init__(self, window, name):
        self.timeout = 20000  # 20 segundos
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('nun'))
        pg.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self):
        pg.mixer_music.load(f'./asset/{self.name}.wav')
        pg.mixer_music.play(-1)
        clock = pg.time.Clock()

        while True:
            clock.tick(60)
            self.window.fill((0, 0, 0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2', 'Enemy3', 'Enemy4','Enemy5',"Enemy6","Enemy7",'Enemy8',"Enemy9","Enemy10","Enemy11","Enemy12","Enemy13","Enemy14","Enemy15","Enemy16",))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()


            self.level_text(20, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_REDBLOOD, (10, 5))
            self.level_text(20, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(20, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            pg.display.flip()


            #COLLISIONS
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)