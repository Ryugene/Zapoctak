import pygame
import random
pygame.init()
queue = []
indexy = [i for i in range(100)]
boolean = [None for i in range(100)]
rekurze = {key: value for key, value in zip(indexy,boolean)}
pos = [11,10,9,1,-1,-9,-10,-11]
# Screen
screen = pygame.display.set_mode((600,600))
running = True
#Icon
icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)
#Obrázky
zivot = pygame.image.load("zivot.png")
smrt = pygame.image.load("smrt.png")
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
zivot = pygame.transform.scale((zivot),(600,600))
smrt = pygame.transform.scale((smrt),(600,600))
mina = pygame.transform.scale((mina),(60,60))
vlajka = pygame.transform.scale((vlajka),(60,60))
jednicka = pygame.transform.scale((jednicka),(60,60))
dvojka = pygame.transform.scale((dvojka),(60,60))
trojka = pygame.transform.scale((trojka),(60,60))
ctyrka = pygame.transform.scale((ctyrka),(60,60))
petka = pygame.transform.scale((petka),(60,60))
sestka = pygame.transform.scale((sestka),(60,60))
sedmicka = pygame.transform.scale((sedmicka),(60,60))
osmicka = pygame.transform.scale((osmicka),(60,60))
# Background
bg = pygame.image.load("background.jpg")
bg = pygame.transform.scale((bg),(600,600))
screen.blit((bg),(0,0))
#lines
x = 60
y = 60
for lines in range(9):
        pygame.draw.line((screen),(255,255,255),(x,0),(x,600))
        pygame.draw.line((screen),(255,255,255),(0,y),(600,y))
        y += 60
        x += 60
def hledej():
    global queue,rekurze,ind
    queue.append(ind)
    while queue != []:
        curr = queue[0]
        del queue[0]
        for i in pos:
            if i == 11:
                if curr-i >= 0 and curr-i <= 99 and pole[curr-i] >= 0 and (curr-11) %10 != 9 and rekurze[curr-i] == None:
                    if pole[curr-i] == 0:
                        g = pygame.draw.rect((screen),(255,255,255),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60,60,60))
                        g
                        queue.append(curr-i)
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 1:
                        screen.blit((jednicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 2:
                        screen.blit((dvojka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 3:
                        screen.blit((trojka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 4:
                        screen.blit((ctyrka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 5:
                        screen.blit((petka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 6:
                        screen.blit((sestka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 7:
                        screen.blit((sedmicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 8:
                        screen.blit((osmicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
            elif i == 10:
                if curr-i >= 0 and curr-i <= 99 and pole[curr-i] >= 0 and rekurze[curr-i] == None:
                    if pole[curr-i] == 0:
                        g = pygame.draw.rect((screen),(255,255,255),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60,60,60))
                        g
                        queue.append(curr-i)
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 1:
                        screen.blit((jednicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 2:
                        screen.blit((dvojka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 3:
                        screen.blit((trojka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 4:
                        screen.blit((ctyrka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 5:
                        screen.blit((petka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 6:
                        screen.blit((sestka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 7:
                        screen.blit((sedmicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 8:
                        screen.blit((osmicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
            elif i == 9:
                if curr-i >= 0 and curr-i <= 99 and pole[curr-i] >= 0 and (curr-9) %10 != 0 and rekurze[curr-i] == None:
                    if pole[curr-i] == 0:
                        g = pygame.draw.rect((screen),(255,255,255),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60,60,60))
                        g
                        queue.append(curr-i)
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 1:
                        screen.blit((jednicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 2:
                        screen.blit((dvojka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 3:
                        screen.blit((trojka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 4:
                        screen.blit((ctyrka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 5:
                        screen.blit((petka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 6:
                        screen.blit((sestka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 7:
                        screen.blit((sedmicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 8:
                        screen.blit((osmicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
            elif i == 1:
                if curr-i >= 0 and curr-i <= 99 and pole[curr-i] >= 0 and (curr-1) %10 != 9 and rekurze[curr-i] == None:
                    if pole[curr-i] == 0:
                        g = pygame.draw.rect((screen),(255,255,255),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60,60,60))
                        g
                        queue.append(curr-i)
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 1:
                        screen.blit((jednicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 2:
                        screen.blit((dvojka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 3:
                        screen.blit((trojka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 4:
                        screen.blit((ctyrka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 5:
                        screen.blit((petka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 6:
                        screen.blit((sestka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 7:
                        screen.blit((sedmicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 8:
                        screen.blit((osmicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
            elif i == -1:
                if curr-i >= 0 and curr-i <= 99 and pole[curr-i] >= 0 and (curr+1) %10 != 0 and rekurze[curr-i] == None:
                    if pole[curr-i] == 0:
                        g = pygame.draw.rect((screen),(255,255,255),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60,60,60))
                        g
                        queue.append(curr-i)
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 1:
                        screen.blit((jednicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 2:
                        screen.blit((dvojka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 3:
                        screen.blit((trojka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 4:
                        screen.blit((ctyrka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 5:
                        screen.blit((petka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 6:
                        screen.blit((sestka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 7:
                        screen.blit((sedmicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 8:
                        screen.blit((osmicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
            elif i == -9:
                if curr-i >= 0 and curr-i <= 99 and pole[curr-i] >= 0 and (curr+9) %10 != 9 and rekurze[curr-i] == None:
                    if pole[curr-i] == 0:
                        g = pygame.draw.rect((screen),(255,255,255),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60,60,60))
                        g
                        queue.append(curr-i)
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 1:
                        screen.blit((jednicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 2:
                        screen.blit((dvojka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 3:
                        screen.blit((trojka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 4:
                        screen.blit((ctyrka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 5:
                        screen.blit((petka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 6:
                        screen.blit((sestka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 7:
                        screen.blit((sedmicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 8:
                        screen.blit((osmicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
            elif i == -10:
                if curr-i >= 0 and curr-i <= 99 and pole[curr-i] >= 0 and rekurze[curr-i] == None:
                    if pole[curr-i] == 0:
                        g = pygame.draw.rect((screen),(255,255,255),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60,60,60))
                        g
                        queue.append(curr-i)
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 1:
                        screen.blit((jednicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 2:
                        screen.blit((dvojka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 3:
                        screen.blit((trojka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 4:
                        screen.blit((ctyrka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 5:
                        screen.blit((petka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 6:
                        screen.blit((sestka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 7:
                        screen.blit((sedmicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 8:
                        screen.blit((osmicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
            elif i == -11:
                if curr-i >= 0 and curr-i <= 99 and pole[curr-i] >= 0 and (curr+11) %10 != 0 and rekurze[curr-i] == None:
                    if pole[curr-i] == 0:
                        g = pygame.draw.rect((screen),(255,255,255),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60,60,60))
                        g
                        queue.append(curr-i)
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 1:
                        screen.blit((jednicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 2:
                        screen.blit((dvojka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 3:
                        screen.blit((trojka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 4:
                        screen.blit((ctyrka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 5:
                        screen.blit((petka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 6:
                        screen.blit((sestka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 7:
                        screen.blit((sedmicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
                    elif pole[curr-i] == 8:
                        screen.blit((osmicka),(miny_index[curr-i][0]-60,miny_index[curr-i][1]-60))
                        rekurze[curr-i] = True
# Pole
x = 60
y = 0
pozice = []
for i in range(10):
    y +=60
    for j in range(10):
        pozice.append((x,y))
        x += 60
    x = 60
pole = [0 for i in range(100)]
while pole.count(-1) != 17:
    pole[random.randint(0,99)] = -1
for i in range(100):
    if pole[i] != -1:
        if i-11 >= 0 and pole[i-11] == -1 and (i-11) % 10 != 9:
            pole[i] += 1
        if i-10 >= 0 and pole[i-10] == -1:
            pole[i] += 1
        if i-9 >= 0 and pole[i-9] == -1 and (i-9) % 10 != 0:
            pole[i] += 1
        if i-1>=0 and pole[i-1] == -1 and (i-1) % 10 != 9:
            pole[i] += 1
        if i < 99 and pole[i+1] == -1 and (i+1) % 10 != 0:
            pole[i] += 1
        if i+9 < 99 and pole[i+9] == -1 and (i+9) % 10 != 9:
            pole[i] += 1
        if i+10 <= 99 and pole[i+10] == -1:
            pole[i] += 1
        if i+11 <= 99 and pole[i+11] == -1 and (i+11) % 10 != 0:
            pole[i] += 1
# Music and sounds
pygame.mixer.music.load("soundtrack.mp3")
death = pygame.mixer.Sound("death.wav")
life = pygame.mixer.Sound("win.wav")
select = pygame.mixer.Sound("select.wav")
flag_s = pygame.mixer.Sound("flag.wav")

music = True
#miny
miny = {key: value for key, value in zip(pozice,pole)}
miny_index = {key: value for key, value in zip(indexy,pozice)}
curr = None
win = True
game = True
# Title
pygame.display.set_caption("Minesweeper")
# Game loop
while running:
    if type(curr) == int and curr+5000 < pygame.time.get_ticks():
        running = False
    j = 0
    if music == True:
        pygame.mixer.music.play(-1)
        music = False

    policka = [i for i in rekurze.values()]
    if policka.count(None) + policka.count(False) == 17:
        pygame.mixer.Sound.play(life)
        pygame.mixer.music.stop()
        screen.blit((zivot),(0,0))
        pygame.display.update()
        if win == True:
            curr = pygame.time.get_ticks()
            win = False
        game = False
    #mouse
    a,b = pygame.mouse.get_pos()
    #events
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    if game == True:
            if (event.type == pygame.MOUSEBUTTONDOWN) and event.button == 3:
                pygame.mixer.Sound.play(flag_s)
                while a%60 != 0:
                    a += 1
                while b%60 != 0:
                    b += 1
                ind = list(miny.keys()).index((a,b))
                if rekurze[ind] == None:
                    screen.blit((vlajka),(a-60,b-60))
                    rekurze[ind] = False
                elif rekurze[ind] == False:
                    pygame.draw.rect((screen),(0,0,0),(a-60,b-60,60,60))
                    rekurze[ind] = None
            if (event.type == pygame.MOUSEBUTTONDOWN) and event.button == 1:
                while a%60 != 0:
                    a += 1
                while b%60 != 0:
                    b += 1
                if miny[(a,b)] == -1:
                    for i in miny.values():
                        if i == -1:
                            jj = miny_index[j]
                            jj = (jj[0]-60,jj[1]-60)
                            screen.blit((mina),(jj))
                        j+=1
                    screen.blit((smrt),(0,0))
                    pygame.display.update()
                    pygame.mixer.Sound.play(death)
                    pygame.mixer.music.stop()
                    curr = pygame.time.get_ticks()
                    game = False
                elif miny[(a,b)] != -1 and miny[(a,b)] == 1:
                    pygame.mixer.Sound.play(select)
                    screen.blit((jednicka),(a-60,b-60))
                    ind = list(miny.keys()).index((a,b))
                    rekurze[ind] = True
                elif miny[(a,b)] != -1 and miny[(a,b)] == 2:
                    pygame.mixer.Sound.play(select)
                    screen.blit((dvojka),(a-60,b-60))
                    ind = list(miny.keys()).index((a,b))
                    rekurze[ind] = True
                elif miny[(a,b)] != -1 and miny[(a,b)] == 3:              
                    screen.blit((trojka),(a-60,b-60))
                    pygame.mixer.Sound.play(select)
                    ind = list(miny.keys()).index((a,b))
                    rekurze[ind] = True
                elif miny[(a,b)] != -1 and miny[(a,b)] == 4:                
                    screen.blit((ctyrka),(a-60,b-60))
                    pygame.mixer.Sound.play(select)
                    ind = list(miny.keys()).index((a,b))
                    rekurze[ind] = True
                elif miny[(a,b)] != -1 and miny[(a,b)] == 5:               
                    screen.blit((petka),(a-60,b-60))
                    pygame.mixer.Sound.play(select)
                    ind = list(miny.keys()).index((a,b))
                    rekurze[ind] = True
                elif miny[(a,b)] != -1 and miny[(a,b)] == 6:                
                    screen.blit((sestka),(a-60,b-60))
                    pygame.mixer.Sound.play(select)
                    ind = list(miny.keys()).index((a,b))
                    rekurze[ind] = True
                elif miny[(a,b)] != -1 and miny[(a,b)] == 7:           
                    screen.blit((sedmicka),(a-60,b-60))
                    pygame.mixer.Sound.play(select)
                    ind = list(miny.keys()).index((a,b))
                    rekurze[ind] = True
                elif miny[(a,b)] != -1 and miny[(a,b)] == 8:           
                    screen.blit((osmicka),(a-60,b-60))
                    pygame.mixer.Sound.play(select)
                    ind = list(miny.keys()).index((a,b))
                    rekurze[ind] = True
                else:
                    ind = list(miny.keys()).index((a,b))
                    pygame.mixer.Sound.play(select)
                    pygame.draw.rect((screen),(255,255,255),(a-60,b-60,60,60))
                    rekurze[ind] = True
                    hledej()
    #display update
    pygame.display.update()
