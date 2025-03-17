import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1100, 700))

pygame.display.set_caption("Flappy Game")

fp1 = pygame.image.load("f1.png")
front1 = pygame.transform.scale(fp1 , (1100,700)).convert_alpha()

fp2 = pygame.image.load("f2.png")
front2 = pygame.transform.scale(fp2 , (1100,700)).convert_alpha()

navy = (11,12,48)
black = (0,0,0)
yellow2 = (255,255,0)
yellow1 = (156,0,76)
red1 = (255,0,0)
white = (255,255,255,50)
blue4 = (70,130,180)
blue1 = (205,133,63)
blue2 = (245,245,238)
grey = (112,135,150)
blue3 = (38,212,233)   #main_colour
purple = (178 , 102 , 250 , 100 )
purple1 = (76,153,0)

screen.blit(front1 , (0,0))
pygame.display.update()

pp = pygame.image.load("p1.png")
cp = pygame.transform.scale(pp , (1100,700)).convert_alpha()

page2_bird_list = { "yellow" : ["yellow_up.png" , "yellow_down.png" , (250,142),(220,180) , 0]    ,   "pink" : ["pink_up.png" , "pink_down.png" , (630,158),(220,160) ,0]  ,  "blue" : ["blue_up.png" , "blue_down.png" , (250,375),(220,180) ,0]   ,   "brown" : ["brown_up.png" , "brown_down.png" , (630,380),(220,180) , 0 ]   }

def choose_char():
    screen.blit(cp , (0,0))
    co = "o"
    for i in page2_bird_list.values():
        q = i[i[-1]]
        b = pygame.image.load(q)
        b0 = pygame.transform.scale(b , i[3]).convert_alpha()
        screen.blit(b0 , i[2])
        pygame.display.update()

def game_over():
    game = pygame.image.load("game_over.png")
    over = pygame.transform.scale(game , (880,560)).convert_alpha()
    screen.blit(over , (110,70) )
    pygame.display.update()

def paste(co , position):
    shade = pygame.image.load("shade.png")
    shade1 = pygame.transform.scale(shade , (280,255)).convert_alpha()
    pp = pygame.image.load(page2_bird_list[co][x])
    cp = pygame.transform.scale(pp , page2_bird_list[co][3]).convert_alpha()
    start = pygame.image.load("start.png")
    start = pygame.transform.scale(start , (150,70)).convert_alpha()

    if co!=h:
        screen.blit(shade1 , position)
        screen.blit(cp , page2_bird_list[co][2])
        screen.blit(start , (475,320))
                
    pygame.display.update()

pipeup1 = pygame.image.load("up.png")
pipedown1 = pygame.image.load("down.png")
place = 900

L = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]


for i in range(0,6):
    place = place +random.randint(250,550)
    L[i][0] = place
    size = random.randint(0,350)
    L[i][1] = size

def pipe():
    global place,L , marks , page , k
    k = k+1
    marks = (k//6)
    for m in range (0,6):
        size = random.randint(0,350)
        L[m][0] =L[m][0]-4
        pipeup = pygame.transform.scale(pipeup1 , (70,390-L[m][1])).convert_alpha()
        pipedown = pygame.transform.scale(pipedown1 , (70,L[m][1]+40)).convert_alpha()
        screen.blit(pipeup , (L[m][0] , L[m][1]+140))
        screen.blit(pipedown , (L[m][0] , 0) )


        if L[m][0]<-70:
            del L[m]
            place=L[-1][0]
            L.append([place +random.randint(160,450),random.randint(0,350)])

        if 380<L[m][0]<460:
            if (L[m][1]+35) < poop < (L[m][1]+138):
                pass
                
            else:
                page = 4
                game_over()
                break
            
    pygame.display.update()        

def page_3():
    global s , g , high , key , poop , page
    pp = pygame.image.load("grass1.jpg")
    cp = pygame.transform.scale(pp , (380,630)).convert_alpha()

    for i in range (0,4):
        z = i*380-(s//2)
        screen.blit(cp , (z , 0))
        if z==-380:
            s=0
    
    pp = pygame.image.load(page2_bird_list[co][v])
    cp = pygame.transform.scale(pp , (50,50+v*4)).convert_alpha()

    font = pygame.font.SysFont('Arial Rounded MT Bold',30)
    text = font.render("Score = "+ str(marks) , True, red1)
    
    g=0
    if key=="yes":
        g=5
    if key=="no":
        g=-5
    if key=="draw":
        g=0
                   
    b=20+(3*t)
    high = high + g
    poop = 400-v*5 - high
    if b<450:
        screen.blit(cp , (b , poop))
    else:
        screen.blit(cp , (450 , poop))
    pipe()
    screen.blit(text, [900,50])

    pygame.display.update()
    

def start():
    posb =(0,0)
    pos = (0,0)
    co = "o"
    page=1
    x=0
    t=0
    s=0
    high = 0
    key = "draw"
    g=0
    turn = []
    q=0
    marks = 0
    run = True
    post = (0,0)

k=0
posb =(0,0)
pos = (0,0)
co = "o"
page=1
x=0
t=0
s=0
high = 0
key = "draw"
g=0
turn = []
clock = pygame.time.Clock()
fps = 240
q=0
marks = 0
run = True
post = (0,0)

while run:
    t=t+1
    s=s+1
    q=q+1

    if t%240==0 :
        x=0
        
    elif t%240==120:
        x=1

    if t%20==0 :
        v=0
        
    elif t%20==10:
        v=1
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                key = "yes"                
            if event.key == pygame.K_DOWN:
                key = "no"
            if event.key == pygame.K_SPACE:
                key = "draw"

        if event.type == pygame.MOUSEBUTTONDOWN:            
            if page ==1:
                pos = pygame.mouse.get_pos()
                
            if page==2:
                posb = pygame.mouse.get_pos()
                print(posb)
                h = co

                if co!="o":
                    if 475<posb[0]<625:
                        if 320<posb[1]<390:
                            page = 3
                            s=0
                            t=0
                            q=0
                            screen.fill(blue3)
                            pygame.display.update()
                    else:
                        choose_char()

            if page == 4:
                post = pygame.mouse.get_pos()
                print(post)

                if 460< post[0] <645:
                    if 300< post[1] <355:
                        pos = (0,0)
                        L = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]
                        for i in range(0,6):
                            place = place +random.randint(250,550)
                            L[i][0] = place
                            size = random.randint(0,350)
                            L[i][1] = size
                        co = "o"
                        page=2
                        choose_char()
                        x=0
                        t=0
                        s=0
                        high = 0
                        key = "draw"
                        g=0
                        turn = []
                        q=0
                        marks = 0
                        post = (0,0)
                        
                    elif 410< post[1] <470:
                        pos = (0,0)
                        L = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]]
                        for i in range(0,6):
                            place = place +random.randint(250,550)
                            L[i][0] = place
                            size = random.randint(0,350)
                            L[i][1] = size
                        co = "o"
                        page=1
                        x=0
                        t=0
                        s=0
                        high = 0
                        key = "draw"
                        g=0
                        turn = []
                        q=0
                        marks = 0
                        post = (0,0)
                    
                print(post)
                    

    if page == 2:
        if t%240==0 or t%240==120 :

            if 250 <posb[0]<460:            
                if 170 <posb[1]< 305:
                    co="yellow"
                    position=(220,110)
                    paste(co , position)

                elif 400 <posb[1]< 540:
                    co="blue"
                    position=(220,340)
                    paste(co ,position)

            elif 640 <posb[0]<830:
                if 170 <posb[1]< 305:
                    co="pink"
                    position=(600,110)
                    paste(co , position)

                elif 400 <posb[1]< 540:
                    co="brown"
                    position=(600,340)
                    paste(co , position)

    if page ==1:
        if t%240==0 :
            screen.blit(front1 , (0,0))
            pygame.display.update()

        elif t%240==120:
            screen.blit(front2 , (0,0))
            pygame.display.update()

        if 445<pos[0]<645:
            if 350<pos[1]<415:
                choose_char()
                page=2

    """if page == 4:
        if 460< post[0] <650:
            if 295< post[1] <360:
                start()
                page=2
                        
            elif 405< post[1] <475:
                start()
                page=1
                screen.blit(front1 , (0,0))
                pygame.display.update()"""

                
    if page == 3:
        page_3()

    
         
    clock.tick(fps)
    
pygame.quit()
            
