#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from Const import WIN_WIDTH
from code.Backgroud import Backgroud
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:


    @staticmethod
    def get_entity(entity_name: str, position = (0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Backgroud(f'Level1Bg{i}', (0, 0 )))
                    list_bg.append(Backgroud(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'nun':
                return Player('nun', (10, 395))

            case 'Enemy1':
                return Enemy('Enemy1', ((WIN_WIDTH + 10), 390))

            case 'Enemy2':
                return Enemy('Enemy2', ((WIN_WIDTH + 10), 400))

            case 'Enemy3':
                return Enemy('Enemy3', (WIN_WIDTH + 10, random.randint(280, 395)))

            case 'Enemy4':
                return Enemy('Enemy4', (WIN_WIDTH + 10, random.randint(280, 395)))
