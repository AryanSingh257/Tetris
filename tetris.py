import pygame

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

window_width=grid_size*grid_width
window_length=grid_size*grid_length

shapes={
    'I':[[1,1,1,1]],
    'O':[[1,1],[1,1]],
    'T':[[0,1,0],[1,1,1]]
}

colors={
    'I':red,
    'O':green,
    'T':blue
}

current_piece='T'
current_shape=shapes[current_piece]
current_color=colors[current_piece]
piecex=3
piecey=0

screen=pygame.display.set_mode((window_width,window_length))
clock=pygame.time.Clock()

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
    return True

def draw_grid():
    for x in range(grid_width+1):
        pygame.draw.line(screen,grey,(x*grid_size,0),(x*grid_size,window_length))
    
    for y in range(grid_length+1):
        pygame.draw.line(screen,grey,(0,y*grid_size),(window_width,y*grid_size))

def draw_tetromono():
    for row in range(len(current_shape)):
        for col in range(len(current_shape[row])):
            if current_shape[row][col]==1:
                x=(piecex+col)*grid_size
                y=(piecey+row)*grid_size
                pygame.draw.rect(screen,current_color,(x,y,grid_size,grid_size))
                pygame.draw.rect(screen,white,(x,y,grid_size,grid_size),2)

running=True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                running=False
            if event.key==pygame.K_a:
                new=piecex-1
                if check_position(current_shape,new,piecey):
                    piecex=new
            if event.key==pygame.K_s:
                new=piecey+1
                if check_position(current_shape,piecex,new):
                    piecey=new
            if event.key==pygame.K_d:
                new=piecex+1
                if check_position(current_shape,new,piecey):
                    piecex=new
    
    screen.fill(black)
    draw_grid()
    draw_tetromono()
    pygame.display.flip()

pygame.quit()