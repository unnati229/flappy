import pygame

pygame.init()

screen = pygame.display.set_mode((1100, 700))

pygame.display.set_caption("Flappy Game")

navy = (11,12,48)
black = (0,0,0)
yellow = (255,255,0)
yellow1 = (156,0,76)
red = (255,0,0)
white = (255,255,255)
blue = (70,130,180)
blue1 = (205,133,63)
blue2 = (245,245,238)
grey = (112,135,150)
blue3 = (0,153,153)
purple = (178,102,255)
purple1 = (76,153,0)

screen.fill(blue3)
font = pygame.font.SysFont('Cooper Black',70)
text = font.render("Start the Quiz", True, white)  
screen.blit(text, [290,200])
font = pygame.font.SysFont('Cooper Black',30)
tn = 'write your name : '
textn = font.render(tn,True,yellow)
screen.blit(textn,(150,400))
tr = 'write your Roll_No : '
textn = font.render(tr,True,yellow)
screen.blit(textn,(150,500))

pygame.draw.rect(screen,yellow,[450,400,300,40],2)
pygame.draw.rect(screen,yellow,[480,500,300,40],2)

font = pygame.font.SysFont('Cooper Black',20)
tn = 'press RIGHT ARROW KEY to start the quiz'
textn = font.render(tn,True,yellow)
screen.blit(textn,(330,600))
pygame.display.update()

font = pygame.font.SysFont(None,33)
text1 = ''
ans = []
lq = []
lpo = []

'''with open('quiz_questions.csv' , 'r') as f:
    r = csv.reader(f)
    x = []
    for rows in r:
        x.append(rows)'''

x = [['General Science', '', '', '', '', '', ''], ['Science', '', '', '', '', '', ''], ['10', '', '', '', '', '', ''], ['30', '', '', '', '', '', ''], ['4', '', '', '', '', '', ''], ['1', 'Brass gets discoloured in the air because of the presence of which of the following gases in air?', 'Oxygen', 'Hydrogen Sulphide', 'Carbon dioxide', 'Nitrogen', '2'], ['2', ' Which of the following is a non-metal that remains liquid at room temperature?', 'Phosphorous', 'Bromine', 'Chlorine', 'Helium', '2'], ['3', 'Chlorophyll is a naturally occurring chelate compound in which central metal is', 'copper', 'magnesium', 'iron', 'calcium', '2'], ['4', 'Which of the following is used in pencils?', 'Graphite', 'Silicon', 'Charcoal', 'Phosphorous', '2'], ['5', 'Which of the following metals forms an amalgam with other metals?', 'Tin', 'Mercury', 'Lead', 'Zinc', '2'], ['6', 'Chemical formula for water is', 'NaAlO2', 'H2O', 'Al2O3', 'CaSiO3', '2'], ['7', 'The gas usually filled in the electric bulb is', 'nitrogen', 'hydrogen', 'carbon dioxide', 'oxygen', '1'], ['8', 'Washing soda is the common name for', 'Sodium carbonate', 'Calcium bicarbonate', 'Sodium bicarbonate', 'Calcium carbonate', '1'], ['9', 'Quartz crystals normally used in quartz clocks etc. is chemically', 'silicon dioxide', 'germanium oxide', 'a mixture of germanium oxide and silicon dioxide', 'sodium silicate', '1'], ['10', 'Which of the gas is not known as green house gas?', 'Methane', 'Nitrous oxide', 'Carbon dioxide', 'Hydrogen', '4'], ['11', 'Bromine is a', 'black solid', 'red liquid', 'colourless gas', 'highly inflammable gas', '2'], ['12', 'The hardest substance available on earth is', 'Gold', 'Iron', 'Diamond', 'Platinum', '3'], ['13', 'The variety of coal in which the deposit contains recognisable traces of the original plant material is', 'bitumen', 'anthracite', 'lignite', 'peat', '4'], ['14', 'Tetraethyl lead is used as', 'Tetraethyl lead is used as', 'fire extinguisher', 'mosquito repellent', 'petrol additive', '4'], ['15', 'petrol additive', 'Graphite', 'Silica', 'Iron Oxide', 'Diamond', '1'], ['16', 'The inert gas which is substituted for nitrogen in the air used by deep sea divers for breathing, is', 'Argon', 'Xenon', 'Helium', 'Krypton', '3'], ['17', 'The gases used in different types of welding would include', 'oxygen and hydrogen', 'oxygen, hydrogen, acetylene and nitrogen', 'oxygen, acetylene and argon', 'oxygen and acetylene', '4'], ['18', 'The property of a substance to absorb moisture from the air on exposure is called', 'osmosis', 'deliquescence', 'efflorescence', 'desiccation', '2'], ['19', 'In which of the following activities silicon carbide is used?', 'Making cement and glass', 'Disinfecting water of ponds', 'cutting very hard substances', 'Making casts for statues', '3'], ['20', 'The average salinity of sea water is', '3%', '3.50%', '2.50%', '2%', '2'], ['21', 'When an iron nail gets rusted, iron oxide is formed', 'without any change in the weight of the nail', 'with decrease in the weight of the nail', 'with increase in the weight of the nail', 'without any change in colour or weight of the nail', '3'], ['22', 'Galvanised iron sheets have a coating of', 'lead', 'chromium', 'zinc', 'tin', '3'], ['23', 'Among the various allotropes of carbon,', 'coke is the hardest, graphite is the softest', 'diamond is the hardest, coke is the softest', 'diamond is the hardest, graphite is the softest', 'diamond is the hardest, lamp black is the softest', '3'], ['24', 'The group of metals Fe, Co, Ni may best called as', 'transition metals', 'main group metals', 'alkali metals', 'rare metals', '1'], ['25', 'Heavy water is', 'deuterium oxide', 'PH7', 'rain water', 'tritium oxide', '1'], ['26', 'The element common to all acids is', 'hydrogen', 'carbon', 'sulphur', 'oxygen', '1'], ['27', 'Non stick cooking utensils are coated with', 'Teflon', 'PVC', 'black paint', 'polystyrene', '1'], ['28', 'Monazite is an ore of', 'titanium', 'zirconium', 'iron', 'thorium', '4'], ['29', 'Carbon, diamond and graphite are together called', 'allotropes', 'isomers', 'isomorphs', 'isotopes', '1'], ['30', 'Potassium nitrate is used in', 'medicine', 'fertiliser', 'salt', 'glass', '2']]
topic = x[0][0]
subject = x[1][0]
time_limit = int(x[2][0])
qno = int(x[3][0])
opn = int(x[4][0])

for i in range (1,qno+1):
    lp = []
    n = str(i)
    que = x[4+i][1]
    lq.append(que)
    for r in range(1,opn+1):
        v = str(r)
        op = x[4+i][1+r]
        lp.append(op)
    h = int(x[4+i][opn+2])
    
    ans.append(h)    
    lpo.append(lp)

colour = []
for e in range(qno):
    col = []
    for b in range(opn):
        col.append(yellow1)
    colour.append(col)

LARGE_LIST = {}
for j in range (qno+1):
    page0 = {}
    
    page0['page_no'] = j
    LARGE_LIST[j]= page0
    z = j-1
    if j==0:
        continue
    page0['que'] = lq[z]
    for d in range (opn):
        i = [lpo[z][d],colour[z][d]]
        page0['option'+str(d+1)] = i

    c = ans[z]-1
    page0['ans'] = str(ans[z])+' : '+ lpo[z][c]
    page0['your_answer'] = 'unattempted'
             
def last():
    if LARGE_LIST[p]['ans'] == LARGE_LIST[p]['your_answer']:
        com = white
    else:
        com = red
    font = pygame.font.SysFont('Arial Rounded MT Bold',40)
    text = font.render(LARGE_LIST[p]['ans']+' :       CORRECT ANSWER  ', True, white)
    screen.blit(text, [60,480])
    text = font.render(LARGE_LIST[p]['your_answer'] +'   :   YOUR ANSWER         marks:' + str(marks[p-1]) , True, com)
    screen.blit(text, [60,400])
    font = pygame.font.SysFont('Arial Rounded MT Bold',50)
    text = font.render('TOTAL MARKS YOU GOT IN THE QUIZ  :  ' + str(sum(marks)), True, yellow)
    screen.blit(text, [30,600])                       
    pygame.display.update()
    
def rect():
    for u in range (opn):
        color = LARGE_LIST[x]['option'+str(u+1)][1]
        pygame.draw.rect(screen ,color,[60, 145+u*42,650,30])
    pygame.display.update()
          
def ques():
    screen.fill(purple)
    font = pygame.font.SysFont('Arial Rounded MT Bold',30)
    text = font.render(str(x)+' : '+lq[x-1], True, white)
    screen.blit(text, [20,80])
    pygame.display.update()

def option():
    for a in range(opn):
        font = pygame.font.SysFont('Arial Rounded MT Bold',30)
        text = font.render(str(a+1)+' : '+lpo[x-1][a], True, white)
        screen.blit(text, [80,152+40*a])
        pygame.display.update()

def rect0():
    for u in range (opn):
        color = LARGE_LIST[p]['option'+str(u+1)][1]
        if color == red:
            font = pygame.font.SysFont('Arial Rounded MT Bold',30)
            text = font.render('YOUR ANSWER', True, yellow)
            screen.blit(text, [720,145+u*42])
        pygame.draw.rect(screen ,color,[60, 145+u*42,650,30])
    pygame.display.update()
   
def ques0():
    screen.fill(purple1)
    font = pygame.font.SysFont('Arial Rounded MT Bold',30)
    text = font.render(str(p)+' : '+lq[p-1], True, white)
    screen.blit(text, [20,80])
    pygame.display.update()

def option0():
    for a in range(opn):
        font = pygame.font.SysFont('Arial Rounded MT Bold',30)
        text = font.render(str(a+1)+' : '+lpo[p-1][a], True, white)
        screen.blit(text, [80,152+40*a])
        pygame.display.update()
        
x=0
marks = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
roll = ''
#timer
clock = pygame.time.Clock()
fps = 120
p = 0
l = 0
minute = time_limit-1
sec = 59
run = True
while run:            
    for c in range(qno):
        f = ans[c]
        if LARGE_LIST[c+1]['option'+str(f)][1] == red:
            LARGE_LIST[c+1]['marks']=4
            marks[c]=4
        else:
            LARGE_LIST[c+1]['marks']=0
            marks[c]=0
            
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if x==0:
                screen.fill(blue3)
                font = pygame.font.SysFont('Arial Rounded MT Bold',50)
                top = font.render(topic,True,yellow1)
                screen.blit(top, [350,80])

                font = pygame.font.SysFont('Arial Rounded MT Bold',40)
                top = font.render(subject,True,yellow1)
                screen.blit(top, [350,130])
                
                font = pygame.font.SysFont('Cooper Black',70)
                text = font.render("Start the Quiz", True, white)
                screen.blit(text, [290,200])
                font = pygame.font.SysFont('Cooper Black',30)
                tn = 'write your name : '
                textn = font.render(tn,True,yellow)
                screen.blit(textn,(150,400))
                
                font = pygame.font.SysFont('Cooper Black',30)
                tr = 'write your Roll_No : '
                textn = font.render(tr,True,yellow)
                screen.blit(textn,(150,500))

                pygame.draw.rect(screen,yellow,[450,400,300,40],2)
                pygame.draw.rect(screen,yellow,[480,500,300,40],2)

                font = pygame.font.SysFont('Cooper Black',20)
                tn = 'press RIGHT ARROW KEY to start the quiz'
                textn = font.render(tn,True,yellow)
                screen.blit(textn,(330,600))
                
                font = pygame.font.SysFont('Cooper Black',30)
                if event.unicode.isdigit():
                    roll = roll + event.unicode

                else:
                    text1 = text1 + event.unicode
                            
                if event.key == pygame.K_BACKSPACE:
                    text1 = ''
                    roll = ''
                text0 = font.render(text1,True,yellow1)
                screen.blit(text0,(480,400))
                                    
                textr = font.render(roll,True,yellow1)
                screen.blit(textr,(510,500))

                pygame.display.update()

                            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if x == 2*qno+2:
                    run = False
                    
            if event.key == pygame.K_RIGHT:
                if x<(qno):
                    x = x+1
                    ques()
                    rect()
                    option()

                elif x==(qno):
                    screen.fill(blue)
                    font = pygame.font.SysFont('Cooper Black',30)
                    text = font.render("Are you sure you want to end the quiz", True, white)
                    screen.blit(text, [250,120])
                    tex = 'if yes than press RIGHT ARROW KEY'
                    text0 = font.render(tex,True,yellow)
                    screen.blit(text0,(270,180))
                    text2 = 'TO SEE YOUR RESULT'
                    text0 = font.render(text2,True,yellow)
                    screen.blit(text0,(350,280))
                    pygame.display.update()
                    x = x+1

                elif x==(qno+1):
                    screen.fill(blue)
                    font = pygame.font.SysFont('Arial Rounded MT Bold',40)
                    ko = 'YOUR MARKS ARE : '+str(sum(marks))
                    text = font.render(ko, True, white)
                    screen.blit(text, [420,300])
                    
                    s = 'press RIGHT ARROW KEY to see answer keys'
                    text = font.render(s, True, white)
                    screen.blit(text, [270,400])
                    
                    font = pygame.font.SysFont('Arial Rounded MT Bold',50)
                    text0 = font.render(text1,True,yellow)
                    screen.blit(text0,(475,250))
                    
                    x = x + 1
                    pygame.display.update()

                elif x == 2*qno+2:
                    screen.fill(black)
                    font = pygame.font.SysFont('Cooper Black',40)
                    text = font.render("press SPACE to EXIT the QUIZ", True, white)
                    screen.blit(text, [200,200])

                elif (2*qno+2)>x>(qno+1):
                    p = x-qno-1
                    ques0()
                    rect0()
                    option0()
                    last()
                    x = x+1 
                    pygame.display.update()   
                                    
            if event.key == pygame.K_LEFT:
                if (qno+2)>x>1:
                    x = x-1
                    ques()
                    rect()
                    option()

                if (2*qno+3)>x>(qno+2):
                    x = x-1
                    p = x-qno-1
                    ques0()
                    rect0()
                    option0()
                    last()                 

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            if 10 < pos[0] < 650:
                for m in range(opn):
                    y1 = (145+(m*42))
                    y2 = (145+((m+1)*42))
                    LARGE_LIST[x]['option'+str(m+1)][1] = yellow1
                    rect()
                    option()
                    if y1<pos[1]<y2:
                        rect()
                        pygame.draw.rect(screen ,red,[60, 145+m*42,650,30])
                        LARGE_LIST[x]['option'+str(m+1)][1] = red
                        LARGE_LIST[x]['your_answer'] = str(m+1)+' : '+lpo[x-1][m]
                        option()
                        pygame.display.update()
            
    if 0<x<(qno+2):
        p = p+1
        font = pygame.font.SysFont('Cooper Black',30)
        pygame.draw.rect(screen ,red,[790, 600,210,40])
        time = font.render("Time : "+str(minute)+' : '+str(sec), True, white)
        screen.blit(time, [800,600])
        pygame.display.update()
        if p%120==0:
            if p%7200==0:
                minute = int(time_limit-1-(p/7200))
            sec = int(59 - (p%7200)/120)

        if minute == 0:
            if sec==0:
                x = qno+1
                screen.fill(blue)
                font = pygame.font.SysFont('Arial Rounded MT Bold',40)
                ko = 'YOUR TIME IS OVER'
                text = font.render(ko, True, white)
                screen.blit(text, [420,300])
                    
                s = 'press RIGHT ARROW KEY to see RESULT'
                text = font.render(s, True, white)
                screen.blit(text, [330,350])
                    
                font = pygame.font.SysFont('Arial Rounded MT Bold',50)
                text0 = font.render(text1,True,yellow)
                screen.blit(text0,(475,250))
                    
                x = x + 1
                pygame.display.update()
            
    pygame.display.update()
    clock.tick(fps)
                
pygame.quit()




