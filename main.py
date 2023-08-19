import pygame, math, time, os, random
from math import sqrt
import numpy as np
import pyaudio
from pydub import AudioSegment
from note import noteList as nl
pygame.display.set_caption("asdf")
pygame.init()
pygame.mixer.init()
start_screen = True

w =1600
h= 900
VIS_AREA_WIDTH = 300
VIS_AREA_HEIGHT = 500
BARS = 30
BAR_WIDTH = VIS_AREA_WIDTH // BARS
Cpath = os.path.dirname(__file__)
Fpath = os.path.join("font")

screen = pygame.display.set_mode((w,h))
background = pygame.image.load(r"C:\Users\User\Documents\dev\이찬우\rhythm_game\pic\background.jpg")
bg2 = pygame.image.load(r"C:\Users\User\Documents\dev\이찬우\rhythm_game\pic\bg.png")
start_bg = pygame.image.load(r"C:\Users\User\Documents\dev\이찬우\rhythm_game\pic\start.jpg")
clock = pygame.time.Clock()
music_path = r"C:\Users\User\Documents\dev\이찬우\rhythm_game\Newjeans.mp3"  
pygame.mixer.music.load(music_path)  
pygame.mixer.music.play(0)
start_font = pygame.font.Font(os.path.join(Fpath,"I AM A PLAYER.ttf"), int(w/23))
start_text = start_font.render("START", False, (255,255,255))

main = True
ingame = True

keys = [0, 0, 0, 0]
keyset = [0, 0, 0, 0]

maxframe = 120
fps = 0
note_counter = 0

def check_start_button(mouse_position):
    button_rect = start_text.get_rect(center=(w/2, (h/12)*8))
    if button_rect.collidepoint(mouse_position):
        return True
    return False
while start_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if check_start_button(mouse_pos):
                start_screen = False
    screen.blit(start_bg, (0, 0))
    screen.blit(start_text, (w/2 - start_text.get_width() /2, (h/12)*8 - start_text.get_height() / 2))
    pygame.display.flip()
    clock.tick(maxframe)

if not start_screen:
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.quit()
    main = True
    ingame = True
    pygame.mixer.init()
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(0)
    current_note_idx = 0
    gst = time.time()
    Time = time.time() - gst
    t1 = []
    t2 = []
    t3 = []
    t4 = []
ty = 0
tst = Time
t1=[]
t2=[]
t3=[]
t4=[]

rate = ""
ingame_font_rate = pygame.font.Font(os.path.join(Fpath,"I AM A PLAYER.ttf"), int(w/23))
rate_text = ingame_font_rate.render(str(rate), False, (255,255,255))

def sum_note(n):
    if n == 1:
        ty = 0
        tst = Time + 2
        t1.append([ty,tst])
    if n == 2:
        ty = 0
        tst = Time + 2
        t2.append([ty,tst])
    if n == 3:
        ty = 0
        tst = Time + 2
        t3.append([ty,tst])
    if n == 4:
        ty = 0
        tst = Time + 2
        t4.append([ty,tst])

speed = 0.8
        
notesumt = 0

a=0
aa=0

spin = 0
combo = 0
combo_effect = 0
combo_effect2 = 0
miss_anim = 0
last_combo = 0

combo_time = Time + 1
rate_data = [0,0,0,0]

def rating(n):
    global combo, miss_anim, last_combo, combo_effect, combo_effect2, combo_time, rate
    if abs((h/12) * 9 - rate_data[n - 1] < 950 * speed * (h/900) and (h/12) * 9 - rate_data[n - 1] >= 200*speed*(h/900)):
        last_combo = combo
        miss_anim = 1
        combo = 0
        combo_effect = 0.2
        combo_time = Time + 1
        combo_effect2 = 1.3
        rate = "WORST"
    if abs((h/12) * 9 - rate_data[n - 1] < 200 * speed * (h/900) and (h/12) * 9 - rate_data[n - 1] >= 100*speed*(h/900)):
        last_combo = combo
        miss_anim = 1
        combo = 0
        combo_effect = 0.2
        combo_time = Time + 1
        combo_effect2 = 1.3
        rate = "BAD"
    if abs((h/12) * 9 - rate_data[n - 1] < 100 * speed * (h/900) and (h/12) * 9 - rate_data[n - 1] >= 70*speed*(h/900)):
        combo += 1
        combo_effect = 0.2
        combo_time = Time + 1
        combo_effect2 = 1.3
        rate = "GOOD"
    if abs((h/12) * 9 - rate_data[n - 1] < 70 * speed * (h/900) and (h/12) * 9 - rate_data[n - 1] >= 45*speed*(h/900)):
        combo += 1
        combo_effect = 0.2
        combo_time = Time + 1
        combo_effect2 = 1.3
        rate = "GREAT"
    if abs((h/12) * 9 - rate_data[n - 1] < 45 * speed * (h/900) and (h/12) * 9 - rate_data[n - 1] >= 0*speed*(h/900)):
        combo += 2
        combo_effect = 0.2
        combo_time = Time + 1
        combo_effect2 = 1.3
        rate = "ACCURATE!"
        
current_note_idx = 0
if not start_screen:
    while main:
        while ingame:

            if len(t1) > 0:
                rate_data[0] = t1[0][0]
            if len(t2) > 0:
                rate_data[1] = t2[0][0]
            if len(t3) > 0:
                rate_data[2] = t3[0][0]
            if len(t4) > 0:
                rate_data[3] = t4[0][0]
            Time = pygame.time.get_ticks() / 1000
            print(Time)
            # if current_note_idx < len(nl) and Time >= nl[current_note_idx]['timeTick']:
            #     current_note = nl[current_note_idx]
            #     sum_note(current_note['pos'])
            #     current_note_idx += 1
            #     print("good")
            
            # for next_idx in range(current_note_idx, len(nl)):
            #     next_note = nl[next_idx]
            #     if Time >= next_note['timeTick']:
            #         sum_note(next_note['pos'])
            #         current_note_idx += 1
            #     else:
            #         break
    ####################################################################################################
            # Time = pygame.time.get_ticks() / 1000
            
            while current_note_idx < len(nl) and Time >= nl[current_note_idx]['timeTick']:
                current_note = nl[current_note_idx]
                sum_note(current_note['pos'])  
                current_note_idx += 1 
    #####################################################################################################
            Time = time.time() - gst

            fps = clock.get_fps()
        
            ingame_font_combo = pygame.font.Font(os.path.join(Fpath, "I AM A PLAYER.ttf"), int((w/38)* combo_effect2))
            combo_text = ingame_font_combo.render(str(combo),False, (255,255,255))
            rate_text = ingame_font_rate.render(str(rate),False , (255,255,255))
            rate_text = pygame.transform.scale(rate_text, (int(w/110*len(rate) * combo_effect2), int((w/58 * combo_effect * combo_effect2))))
            
            ingame_font_miss = pygame.font.Font(os.path.join(Fpath, "I AM A PLAYER.ttf"), int(w/38 * miss_anim))
            miss_text = ingame_font_miss.render(str(last_combo), False, (255,0,0))

            if fps == 0:
                fps = maxframe
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        keyset[0] = 1
                        if len(t1) > 0:
                            if t1[0][0] > h /3:
                                rating(1)
                                del t1[0]
                    if event.key == pygame.K_s:
                        keyset[1] = 1
                        if len(t2) > 0:
                            if t2[0][0] > h /3:
                                rating(2)
                                del t2[0]
                    if event.key == pygame.K_d:
                        keyset[2] = 1
                        if len(t3) > 0:
                            if t3[0][0] > h /3:
                                rating(3)
                                del t3[0]
                    if event.key == pygame.K_f:
                        keyset[3] = 1
                        if len(t4) > 0:
                            if t4[0][0] > h /3:
                                rating(4)
                                del t4[0]
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        keyset[0] = 0
                    if event.key == pygame.K_s:
                        keyset[1] = 0
                    if event.key == pygame.K_d:
                        keyset[2] = 0
                    if event.key == pygame.K_f:
                        keyset[3] = 0
        
            screen.blit(background, (0, 0))
            screen.blit(bg2, (w / 2 - w / 8, -int(w/100), w / 4, h+ int(w /50)))

            #######################################################################################################
            keys[1] += (keyset[1]-keys[1])/ (2 * (maxframe / fps))      
            keys[2] += (keyset[2]-keys[2])/ (2 * (maxframe / fps))
            keys[0] += (keyset[0]-keys[0])/ (2 * (maxframe / fps))
            keys[3] += (keyset[3]-keys[3])/ (2 * (maxframe / fps)) 
            #######################################################################################################
            if Time > combo_time:
                combo_effect += (0-combo_effect) / (7*(maxframe/fps))
            if Time < combo_time:
                combo_effect += (1-combo_effect) / (7*(maxframe/fps))
            
            combo_effect2 += (2-combo_effect2) / (7*(maxframe/fps))

            miss_anim +=(4- miss_anim) / (14*(maxframe / fps))
            c = pygame.Color(10, 10, 10, a=255)

            for i in range(7):
                i+=1
                pygame.draw.rect(screen, (200-((200/7)*i),200 - ((200/7)*i),200-((200/7)*i)), (w/2 - w/8 + w/32 - (w/32)*keys[0], (h/12)*9 - (h/30)*keys[0]*i, w/16*keys[0], (h/35)/i))
            for i in range(7):
                i+=1
                pygame.draw.rect(screen, (200-((200/7)*i),200 - ((200/7)*i),200-((200/7)*i)), (w/2 - w/16 + w/32 - (w/32)*keys[1], (h/12)*9 - (h/30)*keys[1]*i, w/16*keys[1], (h/35)/i))
            for i in range(7):
                i+=1
                pygame.draw.rect(screen, (200-((200/7)*i),200 - ((200/7)*i),200-((200/7)*i)), (w/2 + w/32 - (w/32)*keys[2], (h/12)*9 - (h/30)*keys[2]*i, w/16*keys[2], (h/35)/i))
            for i in range(7):
                i+=1
                pygame.draw.rect(screen, (200-((200/7)*i),200 - ((200/7)*i),200-((200/7)*i)), (w/2 + w/16 + w/32 - (w/32)*keys[3], (h/12)*9 - (h/30)*keys[3]*i, w/16*keys[3], (h/35)/i))

            pygame.draw.rect(screen, (0,255,255), (w / 2 - w / 8, -int(w/100), w / 4, h+ int(w /50)), int(w / 100))

            for tile_data in t1:
                tile_data[0] = (h/12) * 9 + (Time - tile_data[1]) * 350 * speed * (h/900)
                pygame.draw.rect(screen, (0,255,255), (w/2 - w/8, tile_data[0] - h/100, w/16, h/50))
                if tile_data[0] > h - (h/9):
                    last_combo = combo
                    miss_anim = 1
                    combo = 0
                    combo_effect = 0.2
                    combo_time = Time + 1
                    combo_effect2 = 1.3
                    rate = "MISS"
                    t1.remove(tile_data)
            for tile_data in t2:
                tile_data[0] = (h/12) * 9 + (Time - tile_data[1]) * 350 * speed * (h/900)
                pygame.draw.rect(screen,(0,255,255),(w/2 - w/16, tile_data[0]- h/100,w/16,h/50))
                if tile_data[0] > h - (h/9):
                    last_combo = combo
                    miss_anim = 1
                    combo = 0
                    combo_effect = 0.2
                    combo_time = Time + 1
                    combo_effect2 = 1.3
                    rate = "MISS"
                    t2.remove(tile_data)
            for tile_data in t3:
                tile_data[0] = (h/12) * 9 + (Time - tile_data[1]) * 350 * speed * (h/900)
                pygame.draw.rect(screen,(0,255,255),(w/2, tile_data[0]- h/100,w/16,h/50))
                if tile_data[0] > h - (h/9):
                    last_combo = combo
                    miss_anim = 1
                    combo = 0
                    combo_effect = 0.2
                    combo_time = Time + 1
                    combo_effect2 = 1.3
                    rate = "MISS"
                    t3.remove(tile_data)
            for tile_data in t4:
                tile_data[0] = (h/12) * 9 + (Time - tile_data[1]) * 350 * speed * (h/900)
                pygame.draw.rect(screen,(0,255,255),(w/2 + w/16, tile_data[0]- h/100,w/16,h/50))
                if tile_data[0] > h - (h/9):
                    last_combo = combo
                    miss_anim = 1
                    combo = 0
                    combo_effect = 0.2
                    combo_time = Time + 1
                    combo_effect2 = 1.3
                    rate = "MISS"
                    t4.remove(tile_data)
            
            pygame.draw.rect(screen, (0,0,0), (w/2-w/8, (h/12)*9,w/4,h/2))
            pygame.draw.rect(screen, (255,255,128), (w/2-w/8, (h/12)*9,w/4,h/2), int(h/100))
            
            pygame.draw.rect(screen, (255 - 100 * keys[0],255 - 100 * keys[0], 255 - 100 * keys[0]), (w / 2 - w / 9, (h / 24) * 19 + (h / 48) * keys[0], w / 27, h / 8), int(h / 150))
            pygame.draw.rect(screen, (255 - 100 * keys[3],255 - 100 * keys[3], 255 - 100 * keys[3]), (w / 2 + w / 13.5, (h / 24) * 19 + (h / 48) * keys[3], w / 27, h / 8), int(h / 150))

            pygame.draw.circle(screen, (150, 150, 150), (w / 2, (h / 24) * 21), (w / 20), int(h / 200))
            pygame.draw.line(screen, (150, 150, 150), (w / 2 - math.sin(spin) * 25 * (w / 1600), (h / 24) * 21 - math.cos(spin) * 25 * (w / 1600)), (w / 2 + math.sin(spin) * 25 * (w / 1600), (h / 24) * 21 + math.cos(spin) * 25 * (w / 1600)), int(w / 400))
            spin += (speed / 10 * (maxframe / fps))


            pygame.draw.rect(screen, (255 - 100 * keys[1], 255 - 100 * keys[1], 255 - 100 * keys[1]), (w / 2 - w / 18, (h / 48) * 39 + (h / 48) * keys[1], w / 27, h / 8))
            pygame.draw.rect(screen, (0,0, 0), (w / 2 - w / 18, (h / 48) * 43 + (h / 48) * (keys[1] * 1.2), w / 27, h / 64), int(h / 150))
            pygame.draw.rect(screen, (50,50, 50), (w / 2 - w / 18, (h / 48) * 39 + (h / 48) * keys[1], w / 27, h / 8), int(h / 150))

            pygame.draw.rect(screen, (255 - 100 * keys[2], 255 - 100 * keys[2], 255 - 100 * keys[2]), (w / 2 + w / 58, (h / 48) * 39 + (h / 48) * keys[2], w / 27, h / 8))
            pygame.draw.rect(screen, (0,0,0), (w / 2 + w / 58, (h / 48) * 43 + (h / 48) * (keys[2] * 1.2), w / 27, h / 64), int(h / 150))
            pygame.draw.rect(screen, (50,50, 50), (w / 2 + w / 58, (h / 48) * 39 + (h / 48) * keys[2], w / 27, h / 8), int(h / 150))
            miss_text.set_alpha(255 - (255/4)* miss_anim)

            screen.blit(combo_text, (w/2 - combo_text.get_width() /2, (h/12)*4 - combo_text.get_height() / 2))
            screen.blit(rate_text, (w/2 - rate_text.get_width() /2, (h/12)*8 - rate_text.get_height() / 2))
            screen.blit(miss_text, (w/2 - miss_text.get_width() /2, (h/12)*4 - miss_text.get_height() / 2))
            pygame.display.flip()
            clock.tick(maxframe)

