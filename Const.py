import pygame as pg

# C
C_REDBLOOD = (136, 8, 8)
C_WHITE = (255, 255, 255)
C_CINZA= (211, 211, 211)
C_GREEN= (0,128,0)
C_BLACK = (0, 0, 0)

CREDITS_TEXT4 = ('Svetlana Kushnariova (Cabbit)',
                '& Jordan Irwin (AntumDeluge).',
                'Original sprite by Charles Gabriel',
                'commissioned by:',
                '(https://opengameart.org/).')

CREDITS_TEXT3 = ('Art by: PWL',
                 '(https://opengameart.org/users/pwl)')

CREDITS_TEXT2 = ('Trulio',
                 '(https://opengameart.org/users/trulio)')

CREDITS_TEXT1 = ('Coghezzi:',
                 '(https://freesound.org/people/Coghezzi/)')

#E
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 2,
    'Level1Bg2': 1,
    'Level1Bg3': 1,
    'Level1Bg4': 1,
    'Level1Bg5': 1,
    'Level1Bg6': 2,
    'Level2Bg0': 0,
    'Level2Bg1': 2,
    'Level2Bg2': 1,
    'Level2Bg3': 1,
    'Level2Bg4': 1,
    'Level2Bg5': 1,
    'Level2Bg6': 2,
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
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level2Bg5': 999,
    'Level2Bg6': 999,
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

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Level2Bg6': 0,
    'nun': 2,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3': 1,
    'Enemy4': 1,
    'Enemy5': 1,
    'Enemy6': 1,
    'Enemy7': 1,
    'Enemy8': 1,
    'Enemy9': 1,
    'Enemy10': 1,
    'Enemy11': 1,
    'Enemy12': 1,
    'Enemy13': 1,
    'Enemy14': 1,
    'Enemy15': 1,
    'Enemy16': 1
}

EVENT_ENEMY = pg.USEREVENT + 1
EVENT_TIMEOUT = pg.USEREVENT + 2

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

#T
TIMEOUT_STEP = 100 #100 ms
TIMEOUT_LEVEL = 20000 #20 seg

# W
WIN_WIDTH = 640
WIN_HEIGHT = 360