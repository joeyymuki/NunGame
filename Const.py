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
    'Level1Bg6': 2,
    'nun': 1,
    'Enemy1': 2,
    'Enemy2': 2,
    'Enemy3': 2,
    'Enemy4': 2,
    'Enemy5': 4,
    'Enemy6': 4,
    'Enemy7': 4,
    'Enemy8': 4,
    'Enemy9': 4,
    'Enemy10': 5,
    'Enemy11': 2,
    'Enemy12': 2,
    'Enemy13': 2,
    'Enemy14': 2,
    'Enemy15': 2,
    'Enemy16': 2
    }

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'nun': 3,
    'Enemy1': 2,
    'Enemy2': 2,
    'Enemy3': 2,
    'Enemy4': 2,
    'Enemy5': 2,
    'Enemy6': 2,
    'Enemy7': 2,
    'Enemy8': 2,
    'Enemy9': 2,
    'Enemy10': 2,
    'Enemy11': 2,
    'Enemy12': 2,
    'Enemy13': 2,
    'Enemy14': 2,
    'Enemy15': 2,
    'Enemy16': 2
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
WIN_WIDTH = 640
WIN_HEIGHT = 360