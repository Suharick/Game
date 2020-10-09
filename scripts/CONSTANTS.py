import pygame

RULES = \
    '''
    Цель игры: в каждом ряду должны стоять\n
    по три одинаковых цветка\n
    Правила игры: используя клавиши «вверх»,\n
    «вниз», «вправо», «влево» перемещайте\n
    курсор (белый квадрат). Если вы хотите\n
    переместить цветок на свободную ячейку,\n
    то нажмите пробел, квадрат увеличится,\n
    после чего укажите направление, в сторону\n
    которого хотите переместить цветок\n
    Удачи!\n
    '''

# pole
X_AREA = 50
Y_AREA = 50
WIDTH_AREA = 515
HEIGHT_AREA = 515

#картинки
BG = pygame.image.load("media/bg.jpg")
PINK = pygame.image.load("media/pink.png")
PURPLE = pygame.image.load("media/purple.png")
RED = pygame.image.load("media/red.png")
WHITE_AND_PINK = pygame.image.load("media/white and pink.png")
YELLOW = pygame.image.load("media/yellow.png")
BLACK = pygame.image.load("media/black.png")
GRAY = pygame.image.load("media/gray.png")

#цвета
RGB204 = (204,204,204)
RGB000 = (0,0,0)
RGB250 = (250,250,250)
RGB154 = (154,154,154)
RGB255 = (255,255,255)

#правила игры
rules1 = "Цель игры: в каждом ряду должны стоять"
rules2 = "по три одинаковых цветка"
rules3 = "Правила игры: используя клавиши «вверх»,"
rules4 = "«вниз», «вправо», «влево» перемещайте"
rules5 = "курсор (белый квадрат). Если вы хотите"
rules6 = "переместить цветок на свободную ячейку,"
rules7 = "то нажмите пробел, квадрат увеличится,"
rules8 = "после чего укажите направление, в сторону"
rules9 = "которого хотите переместить цветок"
rules10 = "Удачи!"

#шрифты
FONT = "media/9202.otf"
