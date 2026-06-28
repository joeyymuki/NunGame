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

            case 'Level2Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Backgroud(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Backgroud(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'nun':
                return Player('nun', (10, 300))

            case 'Enemy1':
                return Enemy('Enemy1', ((WIN_WIDTH + 10), 240))

            case 'Enemy2':
                return Enemy('Enemy2', ((WIN_WIDTH + 10), 240))

            case 'Enemy3':
                return Enemy('Enemy3', ((WIN_WIDTH + 10), 240))

            case 'Enemy4':
                return Enemy('Enemy4', ((WIN_WIDTH + 10), 240))

            case 'Enemy5':
                return Enemy('Enemy5', (WIN_WIDTH + 10, random.randint(180, 236)))

            case 'Enemy6':
                return Enemy('Enemy6', (WIN_WIDTH + 10, random.randint(180, 236)))

            case 'Enemy7':
                return Enemy('Enemy7', (WIN_WIDTH + 10, random.randint(180, 236)))

            case 'Enemy8':
                return Enemy('Enemy8', (WIN_WIDTH + 10, random.randint(180, 236)))

            case 'Enemy9':
                return Enemy('Enemy9', (WIN_WIDTH + 10, random.randint(180, 236)))

            case 'Enemy10':
                return Enemy('Enemy10', (WIN_WIDTH + 10, random.randint(180, 236)))

            case 'Enemy11':
                return Enemy('Enemy11', ((WIN_WIDTH + 10), 240))

            case 'Enemy12':
                return Enemy('Enemy12', ((WIN_WIDTH + 10), 240))

            case 'Enemy13':
                return Enemy('Enemy3', ((WIN_WIDTH + 10), 240))

            case 'Enemy14':
                return Enemy('Enemy14', ((WIN_WIDTH + 10), 240))

            case 'Enemy15':
                return Enemy('Enemy15', ((WIN_WIDTH + 10), 240))

            case 'Enemy16':
                return Enemy('Enemy16', ((WIN_WIDTH + 10), 240))