#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from Const import WIN_WIDTH, MENU_OPTION, C_WHITE, MENU_TIPS, C_CINZA, C_REDBLOOD, LEVEL_TIPS


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load('./asset/MENU1.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pg.mixer_music.load('./asset/SomMenu.wav')
        pg.mixer_music.play(-1) #loop -1

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(30, 'Nun Escape', (136, 8, 8),(170, 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_REDBLOOD, (170, 170 + 35 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_CINZA, (170, 170 + 35 * i))


            for i in range(len(MENU_TIPS)):
                self.menu_text(12, MENU_TIPS[i], C_CINZA, (480, 90 + 30 * i))

            for i in range(len(LEVEL_TIPS)):
                self.menu_text(12, LEVEL_TIPS[i], C_CINZA, (480, 190 + 30 * i))

            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

                #SELEÇÃO DE MENU------------------------------------------------------------------------------------
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_s:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pg.K_w:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pg.K_SPACE: #ESPAÇO
                        pg.mixer_music.stop()
                        return MENU_OPTION[menu_option]




    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.Font("./asset/PressStart2P-Regular.ttf", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)




