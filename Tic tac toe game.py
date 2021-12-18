import time

from pygame.locals import *
import pygame
import numpy as np
pygame.init()

surface = pygame.display.set_mode((400, 400))
surface.fill((92, 25, 64))
pygame.display.flip()


board=np.array([['-','-','-'],['-','-','-'],['-','-','-']])
line1=board[0][0]+' | '+board[0][1]+' | '+board[0][2]
line2=board[1][0]+' | '+board[1][1]+' | '+board[1][2]
line3=board[2][0]+' | '+board[2][1]+' | '+board[2][2]

arr_dict={1:[[0],[0]],2:[[0],[1]],3:[[0],[2]],4:[[1],[0]],5:[[1],[1]],6:[[1],[2]],7:[[2],[0]],8:[[2],[1]],9:[[2],[2]]}

def display_board(msg):
    surface.fill((92, 25, 64))

    font = pygame.font.SysFont('arial', 50)
    score = font.render(line1, True, (255, 255, 255))
    surface.blit(score, (150, 75))

    font = pygame.font.SysFont('arial', 50)
    score = font.render(line2, True, (255, 255, 255))
    surface.blit(score, (150, 150))

    font = pygame.font.SysFont('arial', 50)
    score = font.render(line3, True, (255, 255, 255))
    surface.blit(score, (150, 225))

    font = pygame.font.SysFont('arial', 30)
    score = font.render(msg, True, (255, 255, 255))
    surface.blit(score, (140, 300))

    pygame.display.flip()

def check_rows(board):
    row1 = board[0][0] == board[0][1] == board[0][2] != '-'
    row2 = board[1][0] == board[1][1] == board[1][2] != '-'
    row3 = board[2][0] == board[2][1] == board[2][2] != '-'
    if row1 or row2 or row3:
        return True
    return False

def check_cols(board):
    col1 = board[0][0] == board[1][0] == board[2][0] != '-'
    col2 = board[0][1] == board[1][1] == board[2][1] != '-'
    col3 = board[0][2] == board[1][2] == board[2][2] != '-'
    if col1 or col2 or col3:
        return True
    return False

def check_diag(board):
    dia1=board[0][0] == board[1][1] == board[2][2] != '-'
    dia2=board[2][0] == board[1][1] == board[0][2] != '-'
    if dia1 or dia2:
        return True
    return False

i=1
running = True
while i < 10  and running==True:
    display_board('Please enter position')
    if i%2==0:
        letter='o'
    else:
        letter='x'
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_1:
                board_position = arr_dict[1]
                if board[board_position[0], board_position[1]] == '-':
                    board[board_position[0], board_position[1]] = letter
                    i += 1
                else:
                    print('Please enter any other position')
                line1 = board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2]
                display_board('Please enter position')
            elif event.key == K_2:
                board_position = arr_dict[2]
                if board[board_position[0], board_position[1]] == '-':
                    board[board_position[0], board_position[1]] = letter
                    i += 1
                else:
                    print('Please enter any other position')
                line1 = board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2]
                display_board('Please enter position')
            elif event.key == K_3:
                board_position = arr_dict[3]
                if board[board_position[0], board_position[1]] == '-':
                    board[board_position[0], board_position[1]] = letter
                    i += 1
                else:
                    print('Please enter any other position')
                line1 = board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2]
                display_board('Please enter position')
            elif event.key == K_4:
                board_position = arr_dict[4]
                if board[board_position[0], board_position[1]] == '-':
                    board[board_position[0], board_position[1]] = letter
                    i += 1
                else:
                    print('Please enter any other position')
                line2=board[1][0]+' | '+board[1][1]+' | '+board[1][2]
                display_board('Please enter position')
            elif event.key == K_5:
                board_position = arr_dict[5]
                if board[board_position[0], board_position[1]] == '-':
                    board[board_position[0], board_position[1]] = letter
                    i += 1
                else:
                    print('Please enter any other position')
                line2=board[1][0]+' | '+board[1][1]+' | '+board[1][2]
                display_board('Please enter position')
            elif event.key == K_6:
                board_position = arr_dict[6]
                if board[board_position[0], board_position[1]] == '-':
                    board[board_position[0], board_position[1]] = letter
                    i += 1
                else:
                    print('Please enter any other position')
                line2=board[1][0]+' | '+board[1][1]+' | '+board[1][2]
                display_board('Please enter position')
            elif event.key == K_7:
                board_position = arr_dict[7]
                if board[board_position[0], board_position[1]] == '-':
                    board[board_position[0], board_position[1]] = letter
                    i += 1
                else:
                    print('Please enter any other position')
                line3=board[2][0]+' | '+board[2][1]+' | '+board[2][2]
                display_board('Please enter position')
            elif event.key == K_8:
                board_position = arr_dict[8]
                if board[board_position[0], board_position[1]] == '-':
                    board[board_position[0], board_position[1]] = letter
                    i += 1
                else:
                    print('Please enter any other position')
                line3=board[2][0]+' | '+board[2][1]+' | '+board[2][2]
                display_board('Please enter position')
            elif event.key == K_9:
                board_position = arr_dict[9]
                if board[board_position[0], board_position[1]] == '-':
                    board[board_position[0], board_position[1]] = letter
                    i += 1
                else:
                    print('Please enter any other position')
                line3=board[2][0]+' | '+board[2][1]+' | '+board[2][2]
                display_board('Please enter position')

    c1 = check_cols(board)
    c2 = check_rows(board)
    c3 = check_diag(board)
    if c1 or c2 or c3:
        display_board(f'Letter {letter} won')
        time.sleep(0.6)
        surface.fill((92, 25, 64))
        font = pygame.font.SysFont('arial', 30)
        score = font.render('GAME OVER', True, (255, 255, 255))
        surface.blit(score, (125, 150))
        pygame.display.flip()
        time.sleep(0.7)
        break

else:
    display_board('DRAW')
    time.sleep(0.6)
    surface.fill((92, 25, 64))
    font = pygame.font.SysFont('arial', 30)
    score = font.render('GAME OVER', True, (255, 255, 255))
    surface.blit(score, (125, 150))
    pygame.display.flip()
    time.sleep(0.7)