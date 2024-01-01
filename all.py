import pygame
pygame
import random
import math


class trail:
    def __init__(self, firstset,trailsize):
        self.trailcoords = firstset
        self.trailsize = trailsize
        self.allsize = []
        #define sizes. size gets smaller from n to 1
        for a in range(trailsize,0 ,-1):
            self.allsize.append(a)
        #create trailpoints from class points
        self.trailpoints = []
        for n,a in enumerate(self.trailcoords):
            self.trailpoints.append(point(a[0],a[1],(r.randint(0,255),r.randint(0,255),r.randint(0,255)),self.allsize[n]))
            
    def updatetrail(self,newpos):
        
        #update coordslist
        self.trailcoords.pop()
        self.trailcoords.insert(0,newpos)
        
        #now updating visual points list
        for n,a in enumerate(self.trailcoords):
            self.trailpoints[n].update_coords(a)
        
        
    def drawtrail(self, screen):
       for n, a in reversed(list(enumerate(self.trailpoints))):
            a.dynamic_color_draw(screen, (0, (200 - (20 * n)), (200 - (20 * n))))

    
    def erasetrail(self,screen,bg):
        for a in self.trailpoints:
            a.dynamic_color_draw(screen,bg)

def circle(xy, radius,theta):
    x_center = xy[0]
    y_center = xy[1]
    
    x = x_center + radius * math.cos(theta)
    y = y_center + radius * math.sin(theta)

    return x, y
class particle:#(self,xy,clr,size)
    def __init__(self,xy,clr,size):
        self.x = xy[0]
        self.y = xy[1]
        self.color = clr
        self.size = size
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.size)
        
    def updatepos(self,coords):
        self.x = coords[0]
        self.y = coords[1]
        
class trail2:
    def __init__(self,size,color,dist):
        self.color = color 
        self.size = size
        self.dist = dist
        self.theta = []
        self.particles = []
        for a in range(0,size):
            self.theta.append(random.uniform(0, 2 * math.pi))
            
        for a in range (0,size-1):
            self.particles.append(particle(circle(pygame.mouse.get_pos(),self.dist,self.theta[a]),self.color,(self.size+random.randint(0,4))))
        
    def drawtrail(self,screen):
        for a in self.particles:
            a.draw(screen)
    def newangle(self):
        for n,_ in enumerate(self.theta):
            self.theta[n] = random.uniform(0, 2 * math.pi)
        for n,a in enumerate(self.particles):
            a.updatepos(circle(pygame.mouse.get_pos(),self.dist,self.theta[n]))
    
        