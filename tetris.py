import pygame
import random

pygame.init()

grid_size=30
grid_width=10
grid_length=20

white=(255,255,255)
black=(0,0,0)
grey=(128,128,128)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
purple=(255,0,255)
cyan=(0,255,255)
brown=(255,255,0)
orange=(255,165,0)

window_width=grid_size*grid_width
window_length=grid_size*grid_length

shapes={
    'I':[[1,1,1,1]],
    'O':[[1,1],[1,1]],
    'T':[[0,1,0],[1,1,1]],
    'L':[[1,0],[1,0],[1,1]],
    'J':[[0,1],[0,1],[1,1]],
    'S':[[0,1,1],[1,1,0]],
    'Z':[[1,1,0],[0,1,1]]
}

colors={
    'I':red,
    'O':green,
    'T':blue,
    'L':brown,
    'J':cyan,
    'S':purple,
    'Z':orange
}

board=[[0]*grid_width for _ in range(grid_length)]

def get_pieces():
    piece=random.choice(list(shapes.keys()))
    return {
        'type':piece,
        'shape':shapes[piece],
        'color':colors[piece],
        'x':grid_width//2-1,
        'y':0
    }

current_piece=get_pieces()

screen=pygame.display.set_mode((window_width,window_length))
clock=pygame.time.Clock()

fall_time=0
fall_speed=500


def check_position(shape,x,y):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]==1:
                gx=x+col
                gy=y+row

                if gx<0:
                    return False

                if gx>=grid_width:
                    return False
                
                if gy>=grid_length:
                    return False

                if gy>=0 and board[gy][gx]!=0:
                    return False
    return True

def lock_piece():
    shape=current_piece['shape']
    color=current_piece['color']
    x=current_piece['x']
    y=current_piece['y']

    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]==1:
                gx=x+col
                gy=y+row
                if gy >= 0 and gy < grid_length and gx >= 0 and gx < grid_width:
                    board[gy][gx] = color

def draw_board():
    for row in range(grid_length):
        for col in range(grid_width):
            if board[row][col]!=0:
                x=col*grid_size
                y=row*grid_size

                pygame.draw.rect(screen,board[row][col],(x,y,grid_size,grid_size))
                pygame.draw.rect(screen,white,(x,y,grid_size,grid_size),2)

def draw_grid():
    for x in range(grid_width+1):
        pygame.draw.line(screen,grey,(x*grid_size,0),(x*grid_size,window_length))
    
    for y in range(grid_length+1):
        pygame.draw.line(screen,grey,(0,y*grid_size),(window_width,y*grid_size))

def draw_tetromono():
    shape=current_piece['shape']
    piecex=current_piece['x']
    piecey=current_piece['y']
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]==1:
                x=(piecex+col)*grid_size
                y=(piecey+row)*grid_size
                pygame.draw.rect(screen,current_piece['color'],(x,y,grid_size,grid_size))
                pygame.draw.rect(screen,white,(x,y,grid_size,grid_size),2)

running=True
while running:
    fall_time+=clock.get_rawtime()
    clock.tick(60)

    x=current_piece['x']
    y=current_piece['y']
    shape=current_piece['shape']

    if fall_time>=fall_speed:
        fall_time=0

        new=y+1
        if check_position(shape,x,new):
            current_piece['y']=new
        else:
            lock_piece()
            current_piece=get_pieces()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                running=False
            if event.key==pygame.K_a:
                new=x-1
                if check_position(shape,new,y):
                    current_piece['x']=new
            if event.key==pygame.K_s:
                new=y+1
                if check_position(shape,x,new):
                    current_piece['y']=new
            if event.key==pygame.K_d:
                new=x+1
                if check_position(shape,new,y):
                    current_piece['x']=new
    
    screen.fill(black)
    draw_grid()
    draw_board()
    draw_tetromono()
    pygame.display.flip()

pygame.quit()