#!/usr/bin/python
# -*- coding: utf-8 -*-
from Const import WIN_WIDTH
from code.Backgroud import Backgroud


class EntityFactory:


    @staticmethod
    def get_entity(entiry_name: str, position = (0, 0)):
        match entiry_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(6):
                    list_bg.append(Backgroud(f'Level1Bg{i}', (0, 0 )))
                    list_bg.append(Backgroud(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg



