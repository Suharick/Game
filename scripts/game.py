import pygame
from random import *
import os
import sys
from pygame.locals import *
from scripts import CONSTANTS

#поле представлена матрицей, где 0 - блоки, 1 - свободные, -1 - места, где в начале игры будут расставлены фишки
pole = [[-1,0,-1,0,-1],
        [-1,1,-1,1,-1],
        [-1,0,-1,0,-1],
        [-1,1,-1,1,-1],
        [-1,0,-1,0,-1]]
colors = [2, 3, 4, 5, 6]*3 #цветные фишки
shuffle(colors)

#расстановка фишек
def letsStart(pole, colors):
        i, j, k = 0, 0, 0
        while i <= 4:
                while j <= 4:
                        if j%2 == 0:
                                pole[i][j] = colors[k]
                                k += 1
                        j += 1
                j = 0
                i += 1
        return pole

#конец игры
def oneColor(lineNumber, pole):
        res = 1
        for i in [2, 4]:
                if pole[lineNumber][0] == pole[lineNumber][i]:
                        res += 1
        return res

def finish():
        if oneColor(0, pole) == oneColor(1, pole) == oneColor(2, pole) == oneColor(3, pole) == oneColor(4, pole) == 3:
                return True
        else:
                return False

#интерфейс
pygame.init()
win = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Flowers")

#активная ячейка
x1 = 297
x2 = 297
h, w = 20, 20
push = 0

#координаты для ориентира в матрице
coordX = 2
coordY = 2

run = True

pole = letsStart(pole, colors)


#определение клетки
def whichColor(i, j, pole):
        if pole[i][j] == 0:
                return CONSTANTS.BLACK
        elif pole[i][j] == 1:
                return CONSTANTS.GRAY
        elif pole[i][j] == 2:
                return CONSTANTS.PINK
        elif pole[i][j] == 3:
                return CONSTANTS.PURPLE
        elif pole[i][j] == 4:
                return CONSTANTS.RED
        elif pole[i][j] == 5:
                return CONSTANTS.WHITE_AND_PINK
        elif pole[i][j] == 6:
                return CONSTANTS.YELLOW

#текст
def printText(message, x, y, color = CONSTANTS.RGB000, size = 15):
        type = pygame.font.Font(CONSTANTS.FONT, size)
        text = type.render(message, True, color)
        win.blit(text, (x, y))

#кнопки
class Button:
        def __init__(self, width, height, inactiveColor, activeColor):
                self.width = width
                self.height = height
                self.inactiveColor = inactiveColor
                self.activeColor = activeColor

        def draw(self, x, y, message):
                mouse = pygame.mouse.get_pos()

                if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
                        pygame.draw.rect(win, self.activeColor, (x, y, self.width, self.height))
                else:
                        pygame.draw.rect(win, self.inactiveColor, (x, y, self.width, self.height))
                printText(message, x+3, y+5, size = 30)

win.blit(CONSTANTS.BG, (0, 0))
pygame.draw.rect(win, CONSTANTS.RGB204, (CONSTANTS.X_AREA, CONSTANTS.Y_AREA, CONSTANTS.WIDTH_AREA, CONSTANTS.HEIGHT_AREA))

printText(CONSTANTS.rules1, 620, 170)
printText(CONSTANTS.rules2, 620, 190)
printText(CONSTANTS.rules3, 620, 220)
printText(CONSTANTS.rules4, 620, 240)
printText(CONSTANTS.rules5, 620, 260)
printText(CONSTANTS.rules6, 620, 280)
printText(CONSTANTS.rules7, 620, 300)
printText(CONSTANTS.rules8, 620, 320)
printText(CONSTANTS.rules9, 620, 340)
printText(CONSTANTS.rules10, 620, 370)

while(run == True):
        pygame.time.delay(100)

        pygame.draw.rect(win, CONSTANTS.RGB204,
                         (CONSTANTS.X_AREA, CONSTANTS.Y_AREA, CONSTANTS.WIDTH_AREA, CONSTANTS.HEIGHT_AREA))

        win.blit(whichColor(0, 0, pole), (60, 60))
        win.blit(whichColor(0, 1, pole), (160, 60))
        win.blit(whichColor(0, 2, pole), (260, 60))
        win.blit(whichColor(0, 3, pole), (360, 60))
        win.blit(whichColor(0, 4, pole), (460, 60))

        win.blit(whichColor(1, 0, pole), (60, 160))
        win.blit(whichColor(1, 1, pole), (160, 160))
        win.blit(whichColor(1, 2, pole), (260, 160))
        win.blit(whichColor(1, 3, pole), (360, 160))
        win.blit(whichColor(1, 4, pole), (460, 160))

        win.blit(whichColor(2, 0, pole), (60, 260))
        win.blit(whichColor(2, 1, pole), (160, 260))
        win.blit(whichColor(2, 2, pole), (260, 260))
        win.blit(whichColor(2, 3, pole), (360, 260))
        win.blit(whichColor(2, 4, pole), (460, 260))

        win.blit(whichColor(3, 0, pole), (60, 360))
        win.blit(whichColor(3, 1, pole), (160, 360))
        win.blit(whichColor(3, 2, pole), (260, 360))
        win.blit(whichColor(3, 3, pole), (360, 360))
        win.blit(whichColor(3, 4, pole), (460, 360))

        win.blit(whichColor(4, 0, pole), (60, 460))
        win.blit(whichColor(4, 1, pole), (160, 460))
        win.blit(whichColor(4, 2, pole), (260, 460))
        win.blit(whichColor(4, 3, pole), (360, 460))
        win.blit(whichColor(4, 4, pole), (460, 460))

        pygame.draw.rect(win, CONSTANTS.RGB250, (x1, x2, w, h))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and pole[coordY][coordX] != 1:
                if push == 0:
                        x1 -= 10
                        x2 -= 10
                        w += 20
                        h += 20
                        push = 1
                elif push == 1:
                        x1 += 10
                        x2 += 10
                        w -= 20
                        h -= 20
                        push = 0

        for event in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if event.type == pygame.QUIT: #кнопка закрытия
                        run = True
                        pygame.quit()
                        sys.exit()
                elif event.type == KEYDOWN and event.key == K_DOWN:
                        if coordY + 1 >= 0 and coordY + 1 <= 4:
                                if push == 0 and pole[coordY + 1][coordX] != 0:
                                        coordY += 1
                                        x2 += 100
                                elif push == 1 and pole[coordY + 1][coordX] == 1:
                                        pole[coordY + 1][coordX] = pole[coordY][coordX]
                                        pole[coordY][coordX] = 1
                                        coordY += 1
                                        x1 += 10
                                        x2 += 110
                                        push = 0
                                        w -= 20
                                        h -= 20
                elif event.type == KEYDOWN and event.key == K_UP:
                        if coordY - 1 >= 0 and coordY - 1 <= 4:
                                if push == 0 and pole[coordY - 1][coordX] != 0:
                                        coordY -= 1
                                        x2 -= 100
                                elif push == 1 and pole[coordY - 1][coordX] == 1:
                                        pole[coordY - 1][coordX] = pole[coordY][coordX]
                                        pole[coordY][coordX] = 1
                                        coordY -= 1
                                        x1 += 10
                                        x2 -= 90
                                        push = 0
                                        w -= 20
                                        h -= 20
                elif event.type == KEYDOWN and event.key == K_RIGHT:
                        if coordX + 1 >= 0 and coordX + 1 <= 4:
                                if push == 0 and pole[coordY][coordX + 1] != 0:
                                        coordX += 1
                                        x1 += 100
                                elif push == 1 and pole[coordY][coordX + 1] == 1:
                                        pole[coordY][coordX + 1] = pole[coordY][coordX]
                                        pole[coordY][coordX] = 1
                                        coordX += 1
                                        x2 += 10
                                        x1 += 110
                                        push = 0
                                        w -= 20
                                        h -= 20
                elif event.type == KEYDOWN and event.key == K_LEFT:
                        if coordX - 1 >= 0 and coordX - 1 <= 4:
                                if push == 0 and pole[coordY][coordX - 1] != 0:
                                        coordX -= 1
                                        x1 -= 100
                                elif push == 1 and pole[coordY][coordX - 1] == 1:
                                        pole[coordY][coordX - 1] = pole[coordY][coordX]
                                        pole[coordY][coordX] = 1
                                        coordX -= 1
                                        x1 -= 90
                                        x2 += 10
                                        push = 0
                                        w -= 20
                                        h -= 20
                elif event.type == pygame.MOUSEBUTTONDOWN and 700 < mouse[0] < 700 + 160 and 110 < mouse[1] < 110 + 50:
                        pole = [[-1, 0, -1, 0, -1],
                                [-1, 1, -1, 1, -1],
                                [-1, 0, -1, 0, -1],
                                [-1, 1, -1, 1, -1],
                                [-1, 0, -1, 0, -1]]
                        shuffle(colors)
                        letsStart(pole, colors)

        buttonNewGame = Button(160, 50, CONSTANTS.RGB204, CONSTANTS.RGB154)
        buttonNewGame.draw(700, 115, "New Game")

        if finish():
                printText("Победа!", 115, 250, CONSTANTS.RGB255, size = 100)

        pygame.display.update()

pygame.quit()