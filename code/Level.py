#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from asyncio import timeout
import random
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface
from code.EntityMediator import EntityMediator

from Const import WIN_HEIGHT, C_WHITE, C_REDBLOOD, EVENT_ENEMY, SPAWN_TIME, C_GREEN, EVENT_TIMEOUT, TIMEOUT_STEP, \
    TIMEOUT_LEVEL
from code.Entity import Entity
from code.EntityFactory import EntityFactory
import pygame as pg

from code.Player import Player


class Level:
    def __init__(self, window, name):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        self.entity_list.append(EntityFactory.get_entity('nun'))
        pg.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pg.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

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
                    choice = random.choice(('Enemy1', 'Enemy2', 'Enemy3', 'Enemy4','Enemy5',"Enemy6","Enemy7",
                                            'Enemy8',"Enemy9","Enemy10","Enemy11","Enemy12","Enemy13","Enemy14",
                                            "Enemy15","Enemy16",))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        return True

                found_player = False

                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if ent.name == 'nun':
                    self.level_text(20, f'Player - HEALTH: {ent.health}', C_GREEN, (10, 22))


            self.level_text(20, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_REDBLOOD, (10, 5))
            self.level_text(20, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(20, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))

            pg.display.flip()


            #COLLISIONS
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)