import pygame
pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("First game")

#clock = pygame.time.Clock()
x=200
y=200
width=20
height=20

#base movement step and starting direction
i = 10
direct = "up"
run = True
clock = pygame.time.Clock()
while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run=False

    # movement increment
    def movement(x, y, width, height, direct):

        #define direction
        if y > 400-width-15:
            direct = "up"
        elif y < 0+15:
            direct = "down"
        if direct == "down":
            y += i
        elif direct == "up":
            y -= i

        #draw rectangle
        pygame.draw.rect(screen, (10,20,30), [x, y, width, height])
        return y, direct

    #without trace
    screen.fill((228,234,230))          
  
    #unpacking tuple from function and assigning it to function
    y, direct = movement(x, y, height, width, direct)
    pygame.display.update()
    clock.tick(60)