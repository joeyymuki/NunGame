import pygame as pg

from Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Credits import Credits
from code.Menu import Menu
from code.Level import Level

class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'Level1')
                level_return = level.run()
                if level_return:
                    level = Level(self.window, 'Level2')
                    level_return = level.run()

            elif menu_return == MENU_OPTION[1]:
                credits_screen = Credits(self.window)
                credits_screen.run()

            elif menu_return == MENU_OPTION[2]:
                    pg.quit()
                    quit()
            else:
                pass

