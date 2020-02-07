import pygame
import random
pygame.init()
ind = None
#Icon
icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)
#SETTINGS FUNKCE
pocet_x = 0
pocet_y = 0
pocetmin = 0
def settings():
    global pocet_x,pocet_y,pocetmin
    print("\n\n--Please select your difficulty settings--\n\nRecommended difficulty levels are:")
    print("Easy = width/height: 9x9, Number of mines: 10\nIntermediate = width/height: 16x16, Number of mines: 40\nExpert = width/height:30x16, Number of mines: 99\n")
    while type(pocet_x) != int or pocet_x <9 or pocet_x>30:
        try:
            pocet_x = int(input("Choose your width: (has to be an integer in range(9-30))"))
            if pocet_x < 9 or pocet_x > 30:
                print("Invalid input, try again.")
        except:
            print("Invalid input, try again.")
    while type(pocet_y) != int or pocet_y <9 or pocet_y>25:
        try:
            pocet_y = int(input("Choose your height: (has to be an integer in range(9-25))"))
            if pocet_y < 9 or pocet_y > 30:
                print("Invalid input, try again.")
        except:
            print("Invalid input, try again.")
    while type(pocetmin) != int or pocetmin <1 or pocetmin>pocet_x*pocet_y-1:
        try:
            pocetmin = int(input("Choose your number of mines: (has to be in range(1-"+str(pocet_x*pocet_y-9)+")"))
            if pocetmin <1 or pocetmin > pocet_x*pocet_y-9:
                print("Invalid input, try again.")
        except:
            print("Invalid input, try again.")
settings()
#REKURZE
def hledej():
    global ind
    queue = []
    queue.append(ind)
    def obsluha_rekurze(i):
        global rekurze,miny_index
        if i == pos[0] or i == pos[3] or i == pos[5]:
            podminka = curr % pocet_x != 0
        elif i == pos[1] or i == pos[6]:
            podminka = True
        elif i == pos[2] or i == pos[4] or i == pos[7]:
            podminka = (curr+1) % pocet_x != 0

        if curr-i >= 0 and curr-i <= (pocet_x*pocet_y -1) and pole[curr-i] >= 0 and podminka and rekurze[curr-i] == None:
            if pole[curr-i] == 0:
                pygame.draw.rect((screen),(255,255,255),(miny_index[curr-i][0]-40,miny_index[curr-i][1]-40,40,40))
                queue.append(curr-i)
                rekurze[curr-i] = True
            elif pole[curr-i] == 1:
                screen.blit((jednicka),(miny_index[curr-i][0]-40,miny_index[curr-i][1]-40))
                rekurze[curr-i] = True
            elif pole[curr-i] == 2:
                screen.blit((dvojka),(miny_index[curr-i][0]-40,miny_index[curr-i][1]-40))
                rekurze[curr-i] = True
            elif pole[curr-i] == 3:
                screen.blit((trojka),(miny_index[curr-i][0]-40,miny_index[curr-i][1]-40))
                rekurze[curr-i] = True
            elif pole[curr-i] == 4:
                screen.blit((ctyrka),(miny_index[curr-i][0]-40,miny_index[curr-i][1]-40))
                rekurze[curr-i] = True
            elif pole[curr-i] == 5:
                screen.blit((petka),(miny_index[curr-i][0]-40,miny_index[curr-i][1]-40))
                rekurze[curr-i] = True
            elif pole[curr-i] == 6:
                screen.blit((sestka),(miny_index[curr-i][0]-40,miny_index[curr-i][1]-40))
                rekurze[curr-i] = True
            elif pole[curr-i] == 7:
                screen.blit((sedmicka),(miny_index[curr-i][0]-40,miny_index[curr-i][1]-40))
                rekurze[curr-i] = True
            elif pole[curr-i] == 8:
                screen.blit((osmicka),(miny_index[curr-i][0]-40,miny_index[curr-i][1]-40))
                rekurze[curr-i] = True
    while queue != []:
        curr = queue[0]
        del queue[0]
        for j in pos:
            obsluha_rekurze(j)
# Pole a screen
pozice = []
pole = []
velikost_x = 40
velikost_y = 40
screen_parametry = (pocet_x*40,pocet_y*40)
pos = []


screen = pygame.display.set_mode((screen_parametry))
#lines
def Vyroblajny():
    x = velikost_x
    y = velikost_y
    for lines in range(pocet_x):
        pygame.draw.line((screen),(255,255,255),(x,0),(x,screen_parametry[1]))
        x += velikost_x
    for lines in range(pocet_y):
        pygame.draw.line((screen),(255,255,255),(0,y),(screen_parametry[0],y))
        y += velikost_y
#Obrázky
zivot = pygame.image.load("zivot.png")
smrt1 = pygame.image.load("smrt.png")
jednicka = pygame.image.load("1.png")
dvojka = pygame.image.load("2.png")
trojka = pygame.image.load("3.png")
ctyrka = pygame.image.load("4.png")
petka = pygame.image.load("5.png")
sestka = pygame.image.load("6.png")
sedmicka = pygame.image.load("7.png")
osmicka = pygame.image.load("8.png")
vlajka = pygame.image.load("flag.png")
mina = pygame.image.load("mine.png")
tryagain = pygame.image.load("tryagain.png")
zivot = pygame.transform.scale((zivot),screen_parametry)
smrt1 = pygame.transform.scale((smrt1),screen_parametry)
mina = pygame.transform.scale((mina),(velikost_x,velikost_y))
vlajka = pygame.transform.scale((vlajka),(velikost_x,velikost_y))
jednicka = pygame.transform.scale((jednicka),(velikost_x,velikost_y))
dvojka = pygame.transform.scale((dvojka),(velikost_x,velikost_y))
trojka = pygame.transform.scale((trojka),(velikost_x,velikost_y))
ctyrka = pygame.transform.scale((ctyrka),(velikost_x,velikost_y))
petka = pygame.transform.scale((petka),(velikost_x,velikost_y))
sestka = pygame.transform.scale((sestka),(velikost_x,velikost_y))
sedmicka = pygame.transform.scale((sedmicka),(velikost_x,velikost_y))
osmicka = pygame.transform.scale((osmicka),(velikost_x,velikost_y))
tryagain = pygame.transform.scale((tryagain),(screen_parametry[0]//6,screen_parametry[1]//10))
# Music and sounds
pygame.mixer.music.load("soundtrack.mp3")
smrt = pygame.mixer.Sound("death.wav")
life = pygame.mixer.Sound("win.wav")
select = pygame.mixer.Sound("select.wav")
flag_s = pygame.mixer.Sound("flag.wav")

#miny
miny = {key: value for key, value in zip(pozice,pole)} #Dictionary - keys = pozice - (x,y), values = počet min v pozici
indexy = [i for i in range(len(pozice))]
miny_index = {key: value for key, value in zip(indexy,pozice)} #Dictionary - keys = index pozice, values = pozice (x,y)
boolean = [None for i in range(len(pozice))]
rekurze = {key: value for key, value in zip(indexy,boolean)} #Dictionary - keys = index pozice, values = Boolean
#nějaké proměnné

# Title
pygame.display.set_caption("Minesweeper")
# Game loop
def game_loop():
    time = pygame.time.get_ticks()
    win = None
    cas = True
    music = True
    running = True
    first_click = True
    death = None
    game = True
    pygame.draw.rect((screen),(0,0,0),(0,0,screen_parametry[0],screen_parametry[1]))
    Vyroblajny()
    global miny,indexy,miny_index,boolean,rekurze,ind,pozice
    def Vyrobpole(x,y,pocetm):
        global pozice,pole,pos
        pos = [x+1,x,x-1,1,-1,-(x-1),-x,-(x+1)]
        cord_x = velikost_x
        cord_y = velikost_y
        x_inc = cord_x
        y_inc = 0
        for i in range(y):
            y_inc += cord_y
            for j in range(x):
                pozice.append((x_inc,y_inc))
                x_inc += cord_x
            x_inc = cord_x
        pole = [0 for i in range(x*y)]
        index = pozice.index((a,b))
        while pole.count(-1) != pocetm:
            pole[index] = 0
            n = random.randint(0,x*y-1)
            nenimina = [index]
            if index-(x+1) >=0 and index % x != 0:
                nenimina.append(index-(x+1))
            if index-x >=0:
                nenimina.append(index-x)
            if index-(x-1) >=0 and index+1 % x != 0:
                nenimina.append(index-(x-1))
            if index-1 >=0 and index % x != 0:
                nenimina.append(index-1)
            if index < (x*y-1) and index+1 % x != 0:
                nenimina.append(index+1)
            if index+(x-1) < (x*y-1) and index % x != 0:
                nenimina.append(index+(x-1))
            if index+x <= (x*y-1):
                nenimina.append(index+x)
            if index+(x+1) <= (x*y-1) and index+1 % x != 0:
                nenimina.append(index+(x+1))
            if n not in nenimina:
                pole[n] = -1
        for i in range(x*y):
            if pole[i] != -1:
                if i-(x+1) >= 0 and pole[i-(x+1)] == -1 and i % x != 0:
                    pole[i] += 1
                if i-x >= 0 and pole[i-x] == -1:
                    pole[i] += 1
                if i-(x-1) >= 0 and pole[i-(x-1)] == -1 and (i+1) % x != 0:
                    pole[i] += 1
                if i-1>=0 and pole[i-1] == -1 and i % x != 0:
                    pole[i] += 1
                if i < (x*y-1) and pole[i+1] == -1 and (i+1) % x != 0:
                    pole[i] += 1
                if i+(x-1) < (x*y -1) and pole[i+(x-1)] == -1 and i % x != 0:
                    pole[i] += 1
                if i+x <= (x*y -1) and pole[i+x] == -1:
                    pole[i] += 1
                if i+(x+1) <= (x*y -1) and pole[i+(x+1)] == -1 and (i+1) % x != 0:
                    pole[i] += 1
    
    while running:
        #mouse
        a,b = pygame.mouse.get_pos()
        pygame.display.update()
        j = 0
        if music == True:
            pygame.mixer.music.play(-1)
            music = False

        if death == True:
            game = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and ((screen_parametry[0]*4//10)<a<((screen_parametry[0]*4//10)+(screen_parametry[0]//6))) and ((screen_parametry[1]*6//10)<b<((screen_parametry[1]*6//10)+screen_parametry[1]//10)):
                    running = False
                    death = False
                    game_loop()
        if win == True:
            policka = [i for i in rekurze.values()]
            if policka.count(None) + policka.count(False) == pocetmin:
                if cas == True:
                    time = pygame.time.get_ticks() - time
                    print("Your time was: " + str(time/1000) +" seconds")
                    cas = False
                pygame.mixer.Sound.play(life)
                pygame.mixer.music.stop()
                game = False
                screen.blit((zivot),(0,0))
                screen.blit((tryagain),(screen_parametry[0]*4//10,screen_parametry[1]*6//10)) #screen_parametry[0]//6,screen_parametry[1]//10)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and ((screen_parametry[0]*4//10)<a<((screen_parametry[0]*4//10)+(screen_parametry[0]//6))) and ((screen_parametry[1]*6//10)<b<((screen_parametry[1]*6//10)+screen_parametry[1]//10)):
                        running = False
                        win = False
                        game_loop()
                    elif event.type == pygame.QUIT:
                        running = False
                pygame.display.update()
        
        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game == True:
                if (event.type == pygame.MOUSEBUTTONDOWN) and event.button == 3:
                    pygame.mixer.Sound.play(flag_s)
                    while a%40 != 0:
                        a += 1
                    while b%40 != 0:
                        b += 1
                    ind = list(miny.keys()).index((a,b))
                    if rekurze[ind] == None:
                        screen.blit((vlajka),(a-40,b-40))
                        rekurze[ind] = False
                    elif rekurze[ind] == False:
                        pygame.draw.rect((screen),(0,0,0),(a-40,b-40,40,40))
                        rekurze[ind] = None
                if (event.type == pygame.MOUSEBUTTONDOWN) and event.button == 1 and first_click == True:
                    pozice = []
                    while a%40 != 0:
                        a+=1
                    while b%40 != 0:
                        b+=1
                    Vyrobpole(pocet_x,pocet_y,pocetmin)
                    miny = {key: value for key, value in zip(pozice,pole)} #Dictionary - keys = pozice - (x,y), values = počet min v pozici
                    indexy = [i for i in range(len(pozice))]
                    miny_index = {key: value for key, value in zip(indexy,pozice)} #Dictionary - keys = index pozice, values = pozice (x,y)
                    boolean = [None for i in range(len(pozice))]
                    rekurze = {key: value for key, value in zip(indexy,boolean)} #Dictionary - keys = index pozice, values = Boolean
                    ind = pozice.index((a,b))
                    rekurze[ind] = True
                    win = True
                    pygame.draw.rect((screen),(255,255,255),(a-40,b-40,40,40))
                    pygame.mixer.Sound.play(select)
                    hledej()
                    first_click = False
                elif (event.type == pygame.MOUSEBUTTONDOWN) and event.button == 1:
                    while a%40 != 0:
                        a += 1
                    while b%40 != 0:
                        b += 1
                    if miny[(a,b)] == -1:
                        for i in miny.values():
                            if i == -1:
                                jj = miny_index[j]
                                jj = (jj[0]-40,jj[1]-40)
                                screen.blit((mina),(jj))
                            j+=1
                        screen.blit((smrt1),(0,0))
                        screen.blit((tryagain),(screen_parametry[0]*4//10,screen_parametry[1]*6//10)) #screen_parametry[0]//6,screen_parametry[1]//10)
                        pygame.display.update()
                        pygame.mixer.Sound.play(smrt)
                        pygame.mixer.music.stop()
                        death = True
                        
                        
                    elif miny[(a,b)] != -1 and miny[(a,b)] == 1:
                        pygame.mixer.Sound.play(select)
                        screen.blit((jednicka),(a-40,b-40))
                        ind = list(miny.keys()).index((a,b))
                        rekurze[ind] = True
                    elif miny[(a,b)] != -1 and miny[(a,b)] == 2:
                        pygame.mixer.Sound.play(select)
                        screen.blit((dvojka),(a-40,b-40))
                        ind = list(miny.keys()).index((a,b))
                        rekurze[ind] = True
                    elif miny[(a,b)] != -1 and miny[(a,b)] == 3:              
                        screen.blit((trojka),(a-40,b-40))
                        pygame.mixer.Sound.play(select)
                        ind = list(miny.keys()).index((a,b))
                        rekurze[ind] = True
                    elif miny[(a,b)] != -1 and miny[(a,b)] == 4:                
                        screen.blit((ctyrka),(a-40,b-40))
                        pygame.mixer.Sound.play(select)
                        ind = list(miny.keys()).index((a,b))
                        rekurze[ind] = True
                    elif miny[(a,b)] != -1 and miny[(a,b)] == 5:               
                        screen.blit((petka),(a-40,b-40))
                        pygame.mixer.Sound.play(select)
                        ind = list(miny.keys()).index((a,b))
                        rekurze[ind] = True
                    elif miny[(a,b)] != -1 and miny[(a,b)] == 6:                
                        screen.blit((sestka),(a-40,b-40))
                        pygame.mixer.Sound.play(select)
                        ind = list(miny.keys()).index((a,b))
                        rekurze[ind] = True
                    elif miny[(a,b)] != -1 and miny[(a,b)] == 7:           
                        screen.blit((sedmicka),(a-40,b-40))
                        pygame.mixer.Sound.play(select)
                        ind = list(miny.keys()).index((a,b))
                        rekurze[ind] = True
                    elif miny[(a,b)] != -1 and miny[(a,b)] == 8:           
                        screen.blit((osmicka),(a-40,b-40))
                        pygame.mixer.Sound.play(select)
                        ind = list(miny.keys()).index((a,b))
                        rekurze[ind] = True
                    else:
                        ind = list(miny.keys()).index((a,b))
                        pygame.mixer.Sound.play(select)
                        pygame.draw.rect((screen),(255,255,255),(a-40,b-40,40,40))
                        rekurze[ind] = True
                        hledej()
game_loop()
