import pygame
import random
import math
import time
def drawcircles(arr):
    for (x,y) in arr:
        pygame.draw.circle(display,(0,0,0),(x,y),4)
def selectCentroid(arr):
    if count==0:
        i1 = random.randrange(len(arr))
        t1 = arr[i1]
        i2 = random.randrange(len(arr))
        t2 = arr[i2]
        pygame.draw.circle(display,(255,0,0),t1,4)
        pygame.draw.circle(display,(0,0,255),t2,4)
    else:
        sum_x_blue = 0
        sum_y_blue =0
        sum_x_red = 0
        sum_y_red = 0
        for (x,y) in bluearr:
            sum_x_blue+=x
            sum_y_blue+=y
        for (x,y) in redarr:
            sum_x_red+=x
            sum_y_red+=y
        t1 = (sum_x_blue/len(bluearr),sum_y_blue/len(bluearr))
        t2 = (sum_x_red/(len(redarr)),sum_y_red/len(redarr))
    return t1,t2
def assignPoints(t1,t2,arr):
    bluearr = []
    redarr = []
    for (x,y) in arr:
        result = calculateShortestDistance(x,y,t1,t2)
        if result==1:
            bluearr.append((x,y))
            pygame.draw.circle(display,(0,0,255),(x,y),4)
        else:
            redarr.append((x,y))
            pygame.draw.circle(display,(255,0,0),(x,y),4)

def calculateShortestDistance(x,y,t1,t2):
    x1,y1 = t1
    x2,y2 = t2
    dist1 = math.sqrt((x-x1)**2+(y-y1)**2)
    dist2 = math.sqrt((x-x2)**2+(y-y2)**2)
    if dist1<dist2:
        return 1
    return 0
pygame.init()
clock = pygame.time.Clock()
width = 800
height = 600
display = pygame.display.set_mode((width,height))
exit = False
arr = []
global count,bluearr,redarr
count = 0
bluearr = []
redarr = []
display.fill((255, 255, 255))
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type==pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            arr.append((x,y))
            pygame.draw.circle(display,(0,0,0),(x,y),4)
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                t1,t2=selectCentroid(arr)
                count+=1
                assignPoints(t1,t2,arr)
    pygame.display.update()
    clock.tick(30)
pygame.display.quit()
pygame.quit()
quit()