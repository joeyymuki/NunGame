import pygame as pg

from Const import C_CINZA, WIN_WIDTH, CREDITS_TEXT4, C_REDBLOOD, CREDITS_TEXT3, CREDITS_TEXT1, CREDITS_TEXT2


class Credits:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load('./asset/CREDITOS.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.credits_text(30, 'CRÉDITOS', (136, 8, 8), (320, 30))

            self.credits_text(16, 'Desenvolvimento Geral:', C_REDBLOOD, (170, 70))
            self.credits_text(16,'Kailany Joey S. Messias', C_CINZA, (170, 90))

            self.credits_text(16, 'Músicas:', C_REDBLOOD, (170, 140))
            for i in range(len(CREDITS_TEXT1)):
                self.credits_text(16, CREDITS_TEXT1[i], C_CINZA, (170, 160 + 25 * i))

            self.credits_text(16, "Fundo Menu:", C_REDBLOOD, (170, 230))
            for i in range(len(CREDITS_TEXT2)):
                self.credits_text(16, CREDITS_TEXT2[i], C_CINZA, (170, 250 + 25 * i))



            self.credits_text(16, 'Fundo Level1:', C_REDBLOOD, (480, 70))
            for i in range(len(CREDITS_TEXT3)):
                self.credits_text(16, CREDITS_TEXT3[i], C_CINZA, (480, 90 + 25 * i))


            self.credits_text(16, 'Sprite da Freira:', C_REDBLOOD, (480, 150 ))
            for i in range(len(CREDITS_TEXT4)):
                self.credits_text(16, CREDITS_TEXT4[i], C_CINZA, (480, 170 + 25 * i))

            self.credits_text(16, 'Pressione "ESPAÇO" para voltar', (136, 8, 8), (320, 330))




            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        return

    def credits_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pg.font.SysFont("Arial", text_size, bold=True)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)