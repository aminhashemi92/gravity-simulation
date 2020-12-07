import pygame
import numpy as np

def dis(x1,y1,x2,y2):
  return(np.sqrt((x1-x2)**2+(y1-y2)**2))

pygame.init()
background_colour = (255,255,255)
(width, height) = (600, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)


xz = 100
yz = 200
xk = 300
yk = 200

vxz = 0
vyz = 10
vxk = 0
vyk = 0

m = 1e3
M = 1e9
G = 6.67e-5

dt= 0.01

while 1:
  #pygame.draw.circle(screen, (255,255,255), (int(xz),int(yz)), 2, 1)
  #pygame.draw.circle(screen, (255,255,255), (int(xk),int(yk)), 2, 1)
  #pygame.draw.lines(screen, (255,255,255), False, [(int(rx1),int(ry1)),(int(rx2),int(ry2))], 1)
  #pygame.draw.lines(screen, (255,255,255), False, [(int(rx2),int(ry2)),(int(rx3+100),int(ry3+100))], 1)
  #pygame.display.flip()

	
  r = dis(xz,yz,xk,yk)
  f = G*m*M / (r**2.2)
  fxz = f * (xk-xz)/r
  fyz = f * (yk-yz)/r
  fxk = f * (xz-xk)/r
  fyk = f * (yz-yk)/r

  axz = fxz / m
  ayz = fyz / m
  axk = fxk / M
  ayk = fyk / M

  vxz = vxz + axz *dt
  vyz = vyz + ayz *dt
  vxk = vxk + axk *dt
  vyk = vyk + ayk *dt

  xz = xz + vxz *dt
  yz = yz + vyz *dt
  xk = xk + vxk *dt
  yk = yk + vyk *dt

  pygame.draw.circle(screen, (0,0,0), (int(xz),int(yz)), 2, 1)
  pygame.draw.circle(screen, (0,0,0), (int(xk),int(yk)), 2, 1)
  #pygame.draw.lines(screen, (0,0,0), False, [(int(rx1),int(ry1)),(int(rx2),int(ry2))], 1)
  #pygame.draw.lines(screen, (0,0,0), False, [(int(rx2),int(ry2)),(int(rx3+100),int(ry3+100))], 1)
  pygame.display.flip()
  pygame.time.delay(5)

  #print(xz,yz,xk,yk)
