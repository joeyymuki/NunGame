import pygame as pg
from pygame.font import Font

from Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, C_REDBLOOD
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

                    if level_return:
                        self.show_you_win()

                    if level_return == False:
                        self.show_game_over()

                elif level_return == False:
                    self.show_game_over()

            elif menu_return == MENU_OPTION[1]:
                credits_screen = Credits(self.window)
                credits_screen.run()

            elif menu_return == MENU_OPTION[2]:
                    pg.quit()
                    quit()
            else:
                pass

    def show_game_over(self):
        text_font: Font = pg.font.Font('./asset/PressStart2P-Regular.ttf', 30)
        text_surf = text_font.render('GAME OVER', True, C_REDBLOOD)
        text_rect = text_surf.get_rect(center=(320, 140))

        text_font: Font = pg.font.Font('./asset/PressStart2P-Regular.ttf', 15)
        sub_surf = text_font.render('Pressione "ESPAÇO" para voltar ao Menu', True, (255, 255, 255))
        sub_rect = sub_surf.get_rect(center=(320, 220))

        while True:
            self.window.fill((0, 0, 0))
            self.window.blit(text_surf, text_rect)
            self.window.blit(sub_surf, sub_rect)
            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        return

    def show_you_win(self):
        font_titulo = pg.font.Font('./asset/PressStart2P-Regular.ttf', 30)
        text_surf = font_titulo.render("YOU WIN!", True, (0, 200, 0))
        text_rect = text_surf.get_rect(center=(320, 140))

        font_sub = pg.font.Font('./asset/PressStart2P-Regular.ttf', 10)
        sub_surf = font_sub.render('Pressione "ESPAÇO" para voltar ao Menu', True, (255, 255, 255))
        sub_rect = sub_surf.get_rect(center=(320, 220))

        while True:
            self.window.fill((0, 0, 0))
            self.window.blit(text_surf, text_rect)
            self.window.blit(sub_surf, sub_rect)
            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        return