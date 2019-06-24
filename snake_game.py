import pygame,sys
from pygame.locals import *
import random
import os

#initialize to access all the modules of the pygame like font images etc
pygame.init()


#window variable
screen_width= 600
screen_height = 600

#color variables
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
brown = (138,61,0)
purple = (34,6,75)
#creating screen
gameScreen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('My game')
font = pygame.font.SysFont(None,45)

#time-clock
clock = pygame.time.Clock()
fps = 20

#load image
backGround = pygame.image.load('Images/homeBg.jpg')
OverBg = pygame.image.load('Images/gameOverBG.jpg')



#music loads
pygame.mixer.music.load('background_song/eminem.mp3')
pygame.mixer.music.play(-1,0.0)

#creating-snake function
def plot_snake(screen,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(screen,color,[x,y,snake_size,snake_size])

        
#showing the score to the screen
def text_screen(text,color,x,y):
    text_to_show = font.render(text,True,color)
    gameScreen.blit(text_to_show,[x,y])

    
def welcome():
    while True:
        gameScreen.blit(backGround,(0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.exit()
                sys.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    gameLoop()
        pygame.display.update()
        clock.tick(30)
    
def gameLoop():
    #games variables
    Run = True
    game_over = False
    snakex= 40
    snakey= 50
    snake_size = 20
    velocity_x = 0
    velocity_y = 0
    init_velocity = 10

    #fixing bug
    if(not os.path.exists('highscore.txt')):
       with open('highscore.txt','w') as f:
           f.write('0')
    #reading file
    with open('highscore.txt','r') as f:
        highscore = f.read()


    food_x = random.randint(20,screen_width/2)
    food_y = random.randint(20,screen_height/2)
    food_size = 20

    score = 0

    snake_list = []
    snake_length = 1
    while Run:
        #filling the screen white
        gameScreen.fill(purple)
        if game_over:
            with open('highscore.txt','w') as f:
                f.write(str(highscore))
            gameScreen.blit(OverBg,(0,0))
            text_screen('Score : ' + str(score) +'  High Score: ' +str(highscore),brown,130,430)
            
                
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        welcome()
        else:
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                        
                    if event.key == K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                        
                    if event.key == K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                        
                    if event.key == K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == K_q:
                        score+=10
            if abs(snakex - food_x)<6 and abs(snakey- food_y)<6:
                score += 10
                food_x = random.randint(20,screen_width/2)
                food_y = random.randint(20,screen_height/2)
                snake_length +=1
                if score > int(highscore):
                    highscore = score


               #appending snakex and snakey position to head and appending again to snake_list
            head = []
            head.append(snakex)
            head.append(snakey)
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]

            if snakex <0 or snakex>screen_width or snakey <0 or snakey> screen_height:
                game_over = True
            if head in snake_list[:-1]:
                game_over =True
                

         
            snakex = snakex + velocity_x
            snakey = snakey + velocity_y
            #function call
            plot_snake(gameScreen,white,snake_list,snake_size)
            pygame.draw.rect(gameScreen,green,[food_x,food_y,food_size,food_size])
            text_screen('Score : '+ str(score)+'  HighScore : ' + str(highscore),red,0,0)
            
        clock.tick(fps)
        pygame.display.update()
        




welcome()



    
            

            




