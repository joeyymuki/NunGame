import pygame as pg

# C
COLOR_REDBLOOD = (136, 8, 8)
COLOR_WHITE = (255, 255, 255)
COLOR_CINZA= (211, 211, 211)

#E
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 2,
    'Level1Bg2': 1,
    'Level1Bg3': 1,
    'Level1Bg4': 1,
    'Level1Bg5': 1,
    'Level1Bg6': 3,
    'nun': 1,
    'Enemy1': 3,
    'Enemy2': 3,
    'Enemy3': 2,
    'Enemy4': 4
    }

EVENT_ENEMY = pg.USEREVENT + 1

# M
MENU_OPTION = ('Novo Jogo',
               'Créditos',
               'Sair')

MENU_TIPS = ('Controle do Menu:',
             '"W" e "S" para selecionar',
             '"ESPAÇO" para confirmar')

LEVEL_TIPS = ('Controles do jogo:',
              '"W" para PULAR',
              '"A" e "D" para ANDAR',)


# S
SPAWN_TIME = 2000

# W
WIN_WIDTH = 960
WIN_HEIGHT = 540