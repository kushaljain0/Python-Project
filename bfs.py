
"""Breadth First Search"""

# Importing Libraries
import pygame, sys, random
from collections import deque
from tkinter import messagebox, Tk

#Setting the width and height of the screen
size = (width, height) = 1280, 960
pygame.init()

#Creating a window of size given above
win = pygame.display.set_mode(size)
pygame.display.set_caption('Breadth First Search')
clock = pygame.time.Clock()

#Defining Number and columns and rows 
cols, rows = 64, 48

# Defining pixels width and height in which the whole screen will be divided
w = width//cols
h = height//rows

# Defining lists for storing the parts of the maze and their property
# Defining queue for performing BFS
grid = []
queue, visited = deque(), []
path = []

# Defining Class which keeps all the data related to individual part of our grid
class Spot:
    
    # Function that defines properties of individual part of grid
    def __init__(self, i, j):
        self.x, self.y = i, j
        self.f, self.g, self.h = 0, 0, 0
        self.neighbors = []
        self.prev = None
        self.wall = False
        self.visited = False
    
    # Function for coloring individual part of the grid
    def show(self, win, col, shape= 1):
        if self.wall == True: # Checks whether its a wall or not and changes value of color accordingly
            col = (0, 0, 0)
        if shape == 1:
            pygame.draw.rect(win, col, (self.x*w, self.y*h, w-1, h-1))
        else:
            pygame.draw.circle(win, col, (self.x*w+w//2, self.y*h+h//2), w//3)
    
    # Function for storing neghbouring individual grid so that they can be accesed afterwards
    def add_neighbors(self, grid):
        if self.x < cols - 1:
            self.neighbors.append(grid[self.x+1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x-1][self.y])
        if self.y < rows - 1:
            self.neighbors.append(grid[self.x][self.y+1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y-1]) # Checking for different conditions when the grid is out of bounds
        #Add Diagonals
        # if self.x < cols - 1 and self.y < rows - 1:
        #     self.neighbors.append(grid[self.x+1][self.y+1])
        # if self.x < cols - 1 and self.y > 0:
        #     self.neighbors.append(grid[self.x+1][self.y-1])
        # if self.x > 0 and self.y < rows - 1:
        #     self.neighbors.append(grid[self.x-1][self.y+1])
        # if self.x > 0 and self.y > 0:
        #     self.neighbors.append(grid[self.x-1][self.y-1])


# Function for storing data related to the walls of the maze
def clickWall(pos, state):
    i = pos[0] // w
    j = pos[1] // h
    grid[i][j].wall = state

# Loop to store coordinates of each individual grid in form of pairs
for i in range(cols):
    arr = []
    for j in range(rows):
        arr.append(Spot(i, j))
    grid.append(arr)

# Loop to add neighbours near individual grids
for i in range(cols):
    for j in range(rows):
        grid[i][j].add_neighbors(grid)

    
def main():
    randomflag=0
    winflag=False
    flag = False
    noflag = True
    startflag = False
    makewall=False
    pause=True

    startpoint=False
    endpoint=False
    starttext=pygame.font.SysFont('Corbel',25,bold=True)
    text1=starttext.render('SAMPLE MAZE',True,(0,0,0))
    text2=starttext.render('CREATE NEW MAZE',True,(0,0,0))

    while True:
        if startpoint:
            start.wall=False
        if endpoint:
            end.wall=False
        if startflag==False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button in (1, 3):

                        if event.button == 1:
                            if startpoint and endpoint==False and winflag:
                                end=grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h]
                                endpoint=True

                        if event.button == 1:  
                            if startpoint==False and winflag:
                                start=grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h]
                                startpoint=True
                                queue.append(start)
                                start.visited= True

                        if event.button == 3:
                            if startpoint and endpoint==False and grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h]==start:
                                startpoint=False
                                queue.pop()
                                start.visited= False
                            if endpoint and grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h]==end:
                                endpoint=False
                                
                        if 200<=pygame.mouse.get_pos()[0]<=400  and height/2<=pygame.mouse.get_pos()[1]<=height/2 + 50 and randomflag==0 and event.button==1:
                            winflag=True
                            randomflag=1


                        if 740<=pygame.mouse.get_pos()[0]<=1000  and height/2<=pygame.mouse.get_pos()[1]<=height/2 + 50 event.button==1:
                            winflag=True
                            randomflag=3
                            
                        if winflag and randomflag==3 and startpoint and endpoint:
                            clickWall(pygame.mouse.get_pos(), event.button==1)
                            
                elif event.type == pygame.MOUSEMOTION and randomflag==3 and startpoint and endpoint :
                    if event.buttons[0] or event.buttons[2]:
                        clickWall(pygame.mouse.get_pos(),event.buttons[0])
                if event.type == pygame.KEYDOWN and startpoint and endpoint:
                    if event.key == pygame.K_RETURN:
                        startflag = True

                        
# Exiting and pause function for path finder
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and winflag:
                if event.key == pygame.K_SPACE and pause==True:
                    pause = False
                elif event.key == pygame.K_SPACE and pause==False:
                    pause = True


        if 200<=pygame.mouse.get_pos()[0]<=400 and height/2<=pygame.mouse.get_pos()[1]<=height/2 + 50:
            pygame.draw.rect(win,(255,0,255),[200,height/2,200,50])
        else:
            pygame.draw.rect(win,(0,255,255),[200,height/2,200,50])


        if 740<=pygame.mouse.get_pos()[0]<=1000 and height/2<=pygame.mouse.get_pos()[1]<=height/2 + 50:
            pygame.draw.rect(win,(255,0,255),[740,height/2,260,50])
        else:
            pygame.draw.rect(win,(0,255,255),[740,height/2,260,50])


        win.blit(text1,(220,height/2+12))


        win.blit(text2,(760,height/2+12))

        

        if randomflag==1:
            for i in range(cols):
                for j in range(rows):
                    if random.randint(0,100) < 20:
                        grid[i][j].wall=True
                randomflag=2

        if startflag and pause:
            if len(queue) > 0:
                current = queue.popleft()
                if current == end:
                    temp = current
                    while temp.prev:
                        path.append(temp.prev)
                        temp = temp.prev 
                    if not flag:
                        flag = True
                        print("Done")
                    elif flag:
                        continue
                if flag == False:
                    for i in current.neighbors:
                        if not i.visited and not i.wall:
                            i.visited = True
                            i.prev = current
                            queue.append(i)
            else:
                if noflag and not flag:
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution", "There was no solution" )
                    noflag = False
                else:
                    continue


        
        if winflag:
            win.fill((0, 0, 0))
            for i in range(cols):
                for j in range(rows):
                    spot = grid[i][j]
                    spot.show(win, (255, 255, 255))
                    if spot in path:
                        spot.show(win, (25, 120, 250))
                        spot.show(win, (255,0,0),0)
                    elif spot.visited:
                        spot.show(win, (255, 0, 0))
                    if spot in queue and flag==False:
                        spot.show(win, (0, 255, 0))
                    if startpoint:
                        if spot == start:
                            spot.show(win,(0,10,100))
                            spot.show(win, (255,0,0),0)
                    if endpoint:
                        if spot == end:
                            spot.show(win, (255, 120, 255))
                            spot.show(win, (255,0,0),0)
            if startpoint==False:
                grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h].show(win,(0,10,100))
                grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h].show(win, (255,0,0),0)
            if startpoint and endpoint==False:
                if grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h]!=start:
                    grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h].show(win,(255,120,255))
                    grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h].show(win, (255,0,0),0)   
            if startpoint and endpoint and startflag==False and randomflag==3:
                if grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h]!=start and grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h]!=end:
                    grid[pygame.mouse.get_pos()[0]//w][pygame.mouse.get_pos()[1]//h].show(win,(0,0,0))     
                
        pygame.display.flip()

main()


