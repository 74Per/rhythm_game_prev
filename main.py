import pygame, math, time, os, random

pygame.init()

w =1600
h= w*(9/16)

screen = pygame.display.set_mode((w,h))

clock = pygame.time.Clock()

main = True
ingame = True

keys = [0, 0, 0, 0]
keyset = [0, 0, 0, 0]

maxframe = 60
fps = 0

gst = time.time()
Time = time.time() - gst

ty = 0
tst = Time

t1=[]
t2=[]
t3=[]
t4=[]

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

speed = 3
        
notesumt = 0

a=0
aa=0

spin = 0
while main:
    while ingame:
        if Time > 0.2 * notesumt:
            notesumt +=1   
            while a == aa:
                a = random.randint(1,4)
            sum_note(a)
            aa=a     
        Time = time.time() - gst

        fps = clock.get_fps()
        
        if fps == 0:
            fps = maxframe
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    keyset[0] = 1
                    if len(t1) > 0:
                        if t1[0][0] > h /2:
                            del t1[0]
                if event.key == pygame.K_f:
                    keyset[1] = 1
                    if len(t2) > 0:
                        if t2[0][0] > h /2:
                            del t2[0]
                if event.key == pygame.K_j:
                    keyset[2] = 1
                    if len(t3) > 0:
                        if t3[0][0] > h /2:
                            del t3[0]
                if event.key == pygame.K_k:
                    keyset[3] = 1
                    if len(t4) > 0:
                        if t4[0][0] > h /2:
                            del t4[0]
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    keyset[0] = 0
                if event.key == pygame.K_f:
                    keyset[1] = 0
                if event.key == pygame.K_j:
                    keyset[2] = 0
                if event.key == pygame.K_k:
                    keyset[3] = 0

        screen.fill((0,0,0))


        keys[0] += (keyset[0]-keys[0])/ (4 * (maxframe / fps))
        keys[1] += (keyset[1]-keys[1])/ (4 * (maxframe / fps))
        keys[2] += (keyset[2]-keys[2])/ (4 * (maxframe / fps))
        keys[3] += (keyset[3]-keys[3])/ (4 * (maxframe / fps)) 
        pygame.draw.rect(screen, (0,0,0), (w / 2 - w / 8, -int(w/100), w / 4, h+ int(w /50)))
        
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

        pygame.draw.rect(screen, (176,255,176), (w / 2 - w / 8, -int(w/100), w / 4, h+ int(w /50)), int(w / 100))

        for tile_data in t1:
            tile_data[0] = (h/12) * 9 + (Time - tile_data[1]) * 350 * speed * (h/900)
            pygame.draw.rect(screen, (255,255,176), (w/2 - w/8, tile_data[0] - h/100, w/16, h/50))
            if tile_data[0] > h - (h/9):
                t1.remove(tile_data)
        for tile_data in t2:
            tile_data[0] = (h/12) * 9 + (Time - tile_data[1]) * 350 * speed * (h/900)
            pygame.draw.rect(screen,(255,255,176),(w/2 - w/16, tile_data[0]- h/100,w/16,h/50))
            if tile_data[0] > h - (h/9):
                t2.remove(tile_data)
        for tile_data in t3:
            tile_data[0] = (h/12) * 9 + (Time - tile_data[1]) * 350 * speed * (h/900)
            pygame.draw.rect(screen,(255,255,176),(w/2, tile_data[0]- h/100,w/16,h/50))
            if tile_data[0] > h - (h/9):
                t3.remove(tile_data)
        for tile_data in t4:
            tile_data[0] = (h/12) * 9 + (Time - tile_data[1]) * 350 * speed * (h/900)
            pygame.draw.rect(screen,(255,255,176),(w/2 + w/16, tile_data[0]- h/100,w/16,h/50))
            if tile_data[0] > h - (h/9):
                t4.remove(tile_data)

        pygame.draw.rect(screen, (0,0,0), (w/2-w/8, (h/12)*9,w/4,h/2))
        pygame.draw.rect(screen, (176,255,176), (w/2-w/8, (h/12)*9,w/4,h/2), int(h/100))
        
        pygame.draw.rect(screen, (255 - 100 * keys[0],255 - 100 * keys[0], 255 - 100 * keys[0]), (w / 2 - w / 9, (h / 24) * 19 + (h / 48) * keys[0], w / 27, h / 8), int(h / 150))
        pygame.draw.rect(screen, (255 - 100 * keys[3],255 - 100 * keys[3], 255 - 100 * keys[3]), (w / 2 + w / 13.5, (h / 24) * 19 + (h / 48) * keys[3], w / 27, h / 8), int(h / 150))

        pygame.draw.circle(screen, (150, 150, 150), (w / 2, (h / 24) * 21), (w / 20), int(h / 200))
        pygame.draw.line(screen, (150, 150, 150), (w / 2 - math.sin(spin) * 25 * (w / 1600), (h / 24) * 21 - math.cos(spin) * 25 * (w / 1600)), (w / 2 + math.sin(spin) * 25 * (w / 1600), (h / 24) * 21 + math.cos(spin) * 25 * (w / 1600)), int(w / 400))
        spin += (speed / 20 * (maxframe / fps))


        pygame.draw.rect(screen, (255 - 100 * keys[1], 255 - 100 * keys[1], 255 - 100 * keys[1]), (w / 2 - w / 18, (h / 48) * 39 + (h / 48) * keys[1], w / 27, h / 8))
        pygame.draw.rect(screen, (0,0, 0), (w / 2 - w / 18, (h / 48) * 43 + (h / 48) * (keys[1] * 1.2), w / 27, h / 64), int(h / 150))
        pygame.draw.rect(screen, (50,50, 50), (w / 2 - w / 18, (h / 48) * 39 + (h / 48) * keys[1], w / 27, h / 8), int(h / 150))

        pygame.draw.rect(screen, (255 - 100 * keys[2], 255 - 100 * keys[2], 255 - 100 * keys[2]), (w / 2 + w / 58, (h / 48) * 39 + (h / 48) * keys[2], w / 27, h / 8))
        pygame.draw.rect(screen, (0,0, 0), (w / 2 + w / 58, (h / 48) * 43 + (h / 48) * (keys[2] * 1.2), w / 27, h / 64), int(h / 150))
        pygame.draw.rect(screen, (50,50, 50), (w / 2 + w / 58, (h / 48) * 39 + (h / 48) * keys[2], w / 27, h / 8), int(h / 150))


        pygame.display.flip()
        clock.tick(maxframe)

