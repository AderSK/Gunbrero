# Ovládanie
# Výstrel = SPACE
# Ovládanie Guľky = MOUSE
# Posunutie dohora = W
# Posunutie doľava = A
# Posunutie dodola = S
# Posunutie doprava = D
# Ukončenie Hry = ESCAPE

import pygame
import sys
from random import*
import time
from math import *

pygame.init()
pygame.font.init()

win = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
# Malo by fungovať aj pre menšie rozlíšenia

##### Nefunguje dobre ak je obrazovka priblížená #####

pygame.display.set_icon(pygame.image.load('klob.png'))
pygame.display.set_caption('Gunbrero')

myfont = pygame.font.SysFont('Modern No. 20', 35)
myfont2 = pygame.font.SysFont('Modern No. 20', 400)

klob = pygame.image.load('klob.png')
sombrero = [pygame.image.load('som1.png'), pygame.image.load('som2.png'), pygame.image.load('som3.png'), pygame.image.load('som4.png'), pygame.image.load('som5.png')]

shot = pygame.mixer.Sound('shot.wav')
scream = [pygame.mixer.Sound('scream1.wav'), pygame.mixer.Sound('scream2.wav'), pygame.mixer.Sound('scream3.wav')]
track = pygame.mixer.music.load('track.wav')

pygame.mixer.Sound.set_volume(shot, 0)
pygame.mixer.Sound.set_volume(scream[0], 0)
pygame.mixer.Sound.set_volume(scream[1], 0)
pygame.mixer.Sound.set_volume(scream[2], 0)

pygame.mixer.music.set_volume(0.05)
# Nastavenie hlasitosti hudby

pygame.mouse.set_cursor(*pygame.cursors.broken_x)

class player(object):
    def __init__(self, xsur, ysur, speed):
        self.xsur = xsur
        self.ysur = ysur
        self.speed = speed

    def hit(self):
        global run
        run = False
        a = choice((0, 1, 2))
        scream[a].play()

class gulka(object):
    def __init__(self, xbullet, ybullet, speed, size):
        self.xbullet = xbullet
        self.ybullet = ybullet
        self.speed = speed
        self.size = size
        self.bullet = False
        self.bullet_time = 0
        self.xmys = 0
        self.ymys = 0

class enemy(object):
    def __init__(self, xe, ye, hat, speed, spawn_time, shot_time, bullet_size, bullet_speed, cislo, spawn_pos):
        self.xe = xe
        self.ye = ye
        self.hat = hat
        self.speed = speed
        self.spawn_time = spawn_time
        self.shot_time = shot_time
        self.bullet_size = bullet_size
        self.bullet_speed = bullet_speed
        self.cislo = cislo
        self.spawn_pos = spawn_pos
        self.etime = 0
        self.stime = 0
        self.zije = False
        self.xciel = 0
        self.yciel = 0
        self.jenapoz = False
        
class enemy_bullet(object):
    def __init__(self, xeb, yeb, bullet_size, speed, cielx, ciely):
        self.xeb = xeb
        self.yeb = yeb
        self.bullet_size = bullet_size
        self.speed = speed
        self.cielx = cielx
        self.ciely = ciely
        self.span = 0
        self.lifespan = 180

    def draw(self, win):
        pygame.draw.circle(win, (105,105,105), (self.xeb, self.yeb), self.bullet_size)
        
me = player(900, 400, 7)
gul = gulka(-100, -100, 10, 10)

e1 = enemy(-100, 0, 0, 7, 60, 60, 10, 5, 5, 1)
e2 = enemy(-100, 0, 1, 3, 200, 30, 5, 7, 7, 2)
e3 = enemy(-100, 0, 2, 6, 100, 100, 30, 3, 4, 3)
e4 = enemy(-100, 0, 3, 7, 250, 50, 12, 4, 5, 4)
e5 = enemy(-100, 0, 4, 6, 300, 90, 25, 4, 4, 4)

enem = [e1, e2, e2, e4, e5]

e1b = []
e2b = []
e3b = []
e4b = []
e5b = []

enemb = [e1b, e2b, e3b, e4b, e5b]

score = 0

start = pygame.Rect(1000, 300, 300, 100)
musictoggle = pygame.Rect(1000, 500, 300, 100)
soundtoggle = pygame.Rect(1000, 700, 300, 100)
cont = pygame.Rect(600, 400, 300, 300)
quitB = pygame.Rect(790, 700, 300, 100)

start2 = pygame.Rect(1010, 310, 280, 80)
musictoggle2 = pygame.Rect(1010, 510, 280, 80)
soundtoggle2 = pygame.Rect(1010, 710, 280, 80)
cont2 = pygame.Rect(610, 410, 280, 280)
quitB2 = pygame.Rect(800, 710, 280, 80)

def musicf():
    global music
    music = not music
    if not music:
        pygame.mixer.music.stop()
    if music:
        pygame.mixer.music.play(-1)

def soundf():
    global sound
    sound = not sound
    if not sound:
        pygame.mixer.Sound.set_volume(shot, 0)
        pygame.mixer.Sound.set_volume(scream[0], 0)
        pygame.mixer.Sound.set_volume(scream[1], 0)
        pygame.mixer.Sound.set_volume(scream[2], 0)
    if sound:
        pygame.mixer.Sound.set_volume(shot, 0.1)
        pygame.mixer.Sound.set_volume(scream[0], 0.1)
        pygame.mixer.Sound.set_volume(scream[1], 0.1)
        pygame.mixer.Sound.set_volume(scream[2], 0.1)
        # Nastavenie hlasitosti zvukových efektov

music = False
sound = False
# Začiatočné nastavenie hudby a zvuku

menu = True
while menu:
    pygame.time.delay(15)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            menu = False
            run = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            menu = False
            run = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = e.pos
            if start.collidepoint(mouse_pos):
                menu = False
            if musictoggle.collidepoint(mouse_pos):
                musicf()
            if soundtoggle.collidepoint(mouse_pos):
                soundf()
                
    win.fill((255, 185, 48))
    
    pygame.draw.rect(win, [0, 0, 255], start)
    pygame.draw.rect(win, [255, 185, 48], start2)
    textsurface2 = myfont.render('Start', False, (0, 0, 0))
    win.blit(textsurface2,(1030,330))
    
    pygame.draw.rect(win, [0, 0, 255], musictoggle)
    pygame.draw.rect(win, [255, 185, 48], musictoggle2)
    textsurface3 = myfont.render('Music', False, (0, 0, 0))
    win.blit(textsurface3,(1030,530))
    
    pygame.draw.rect(win, [0, 0, 255], soundtoggle)
    pygame.draw.rect(win, [255, 185, 48], soundtoggle2)
    textsurface4 = myfont.render('Sound', False, (0, 0, 0))
    win.blit(textsurface4,(1030,730))
    
    pygame.draw.rect(win, [0, 0, 255], cont)
    pygame.draw.rect(win, [255, 185, 48], cont2)
    textsurface5 = myfont.render('Shoot = SPACE', False, (0, 0, 0))
    win.blit(textsurface5,(630,430))
    
    textsurface6 = myfont.render('Bullet = MOUSE', False, (0, 0, 0))
    win.blit(textsurface6,(630,530))
    
    textsurface7 = myfont.render('Move = W A S D', False, (0, 0, 0))
    win.blit(textsurface7,(630,630))
    
    if music:
        pygame.draw.circle(win, (0,255,0), (1225, 550), 30)
        
    if not music:
        pygame.draw.circle(win, (255,0,0), (1225, 550), 30)
        
    if sound:
        pygame.draw.circle(win, (0,255,0), (1225, 750), 30)
        
    if not sound:
        pygame.draw.circle(win, (255,0,0), (1225, 750), 30)
        
    pygame.display.update()

run = True
while run:
    pygame.time.delay(15)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
         if me.xsur >= 1:
             me.xsur -= me.speed       
    if keys[pygame.K_d]:
        if me.xsur <= 1819:
            me.xsur += me.speed         
    if keys[pygame.K_s]:
         if me.ysur <= 979:
             me.ysur += me.speed            
    if keys[pygame.K_w]:
        if me.ysur >= 1:
            me.ysur -= me.speed
            
    gul.xmys, gul.ymys = pygame.mouse.get_pos()
    
    if keys[pygame.K_SPACE] and not gul.bullet:
        gul.bullet = True
        gul.xbullet = me.xsur+50
        gul.ybullet = me.ysur+50
        shot.play()
        
    if gul.bullet:
        if gul.xmys > gul.xbullet:
            gul.xbullet += gul.speed
        if gul.xmys < gul.xbullet:
            gul.xbullet -= gul.speed
        if gul.ymys > gul.ybullet:
            gul.ybullet += gul.speed
        if gul.ymys < gul.ybullet:
            gul.ybullet -= gul.speed
        gul.bullet_time += 1
        
    win.fill((255, 185, 48))
    
    if gul.bullet:
        pygame.draw.circle(win, (105,105,105), (gul.xbullet, gul.ybullet), gul.size)

    if gul.bullet and gul.bullet_time >= 20:
        if gul.xbullet >= me.xsur+10 and gul.xbullet <= me.xsur+90:
            if gul.ybullet >= me.ysur+10 and gul.ybullet <= me.ysur+90:
                run = False
                a = choice((0, 1, 2))
                scream[a].play()
                
    egul = -1
    for e in enem:
        egul += 1
        if not e.zije:
            e.etime += 1
            if e.etime == e.spawn_time:
                e.zije = True
                e.time = 0
                if e.spawn_pos == 1:
                    e.xe = -100
                    e.ye = randrange(200, 880)
                    e.xciel = randrange(100, 500)
                    e.yciel = e.ye+randrange(-200, 200)
                if e.spawn_pos == 2:
                    e.xe = randrange(200, 1720)
                    e.ye = -100
                    e.xciel = e.xe+randrange(-200, 200)
                    e.yciel = randrange(100, 600)
                if e.spawn_pos == 3:
                    e.xe = 2020
                    e.ye = randrange(200, 880)
                    e.xciel = randrange(1320, 1820)
                    e.yciel = e.ye+randrange(-200, 200)
                if e.spawn_pos == 4:
                    e.xe = randrange(200, 1720)
                    e.ye = 1180
                    e.xciel = e.xe+randrange(-200, 200)
                    e.yciel = randrange(480, 980)
                    
        if e.zije and not e.jenapoz:
            if e.xciel > e.xe:
                e.xe += e.speed
            if e.xciel < e.xe:
                e.xe -= e.speed
            if e.yciel > e.ye:
                e.ye += e.speed
            if e.yciel < e.ye:
                e.ye -= e.speed
            if abs(e.xciel-e.xe) <= 8 and abs(e.yciel-e.ye) <= 8:
                e.jenapoz = True
                
        if e.jenapoz:
            e.stime += 1
            if e.stime == e.shot_time:
                e.stime = 0
                cielx = me.xsur
                ciely = me.ysur
                px, py = ((cielx - e.xe+50)//(10*e.cislo), (ciely - e.ye+50)//(10*e.cislo))
                enemb[egul].append(enemy_bullet(e.xe+50, e.ye+50, e.bullet_size, e.bullet_speed, px, py))
                shot.play()
                
        if gul.bullet:
            if gul.xbullet >= e.xe+10 and gul.xbullet <= e.xe+90:
                if gul.ybullet >= e.ye+10 and gul.ybullet <= e.ye+90:
                    score += 1
                    e.zije = False
                    e.jenapoz = False
                    e.xe = -100
                    e.ye = 0
                    e.etime = 0
                    e.stime = 0
                    #enemb[egul] = []
                    #Guľky po smrti nepriteľa zmiznú
                    a = choice((0, 1, 2))
                    scream[a].play()
                    
        for bul in enemb[egul]:
            bul.xeb += bul.cielx
            bul.yeb += bul.ciely
            bul.span += 1
            if bul.span == bul.lifespan:
                bul.span = 0
                enemb[egul].pop(enemb[egul].index(bul))
            if bul.xeb >= me.xsur+10 and bul.xeb <= me.xsur+90:
                if bul.yeb >= me.ysur+10 and bul.yeb <= me.ysur+90:
                    me.hit()
            bul.draw(win)
            
        if e.zije:
            win.blit(sombrero[e.hat], (e.xe, e.ye))
            if e.xe >= me.xsur+10 and e.xe <= me.xsur+90:
                if e.ye >= me.ysur+10 and e.ye <= me.ysur+90:
                    me.hit()
                    
    win.blit(klob, (me.xsur, me.ysur))
    
    textsurface1 = myfont.render('Score: '+str(score), False, (0, 0, 0))
    win.blit(textsurface1,(900,50))
    
    pygame.display.update()

koniec = True
while koniec:
    pygame.time.delay(15)
    
    win.fill((255, 0, 0))
    
    textsurface2 = myfont2.render('Game Over', False, (0, 0, 0))
    textsurface3 = myfont.render('Score: '+str(score), False, (0, 0, 0))
    
    win.blit(textsurface2,(75,100))
    win.blit(textsurface3,(900,600))
    
    pygame.draw.rect(win, [0, 0, 255], quitB)
    pygame.draw.rect(win, [255, 0, 0], quitB2)
    textsurface8 = myfont.render('Quit', False, (0, 0, 0))
    win.blit(textsurface8,(900,730))
    
    pygame.display.update()
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            menu = False
            run = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            menu = False
            run = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = e.pos
            if quitB.collidepoint(mouse_pos):
                koniec = False
                pygame.quit()
                sys.exit()
