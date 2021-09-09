import pygame
import requests

#window parameters
Width = 550
buffer = 6
#levels = [easy,medium,hard]

#calling API
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = response.json()['board']
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))] #creating a shallow copy

#colors
back_ground_color = (255,255,255)
black = (0,0,0)
blue= (52,31,155)

def insert(win,position):
    i,j = position[1],position[0]
    myfont = pygame.font.SysFont("Comic Sans MS",35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if (grid_original[i-1][j-1] !=0) : #checking if the block is empty or not 
                    return
                if event.key== 48 : #0 is mapped to 48
                    #earse condition
                    grid[i-1][j-1] = event.key -48
                    pygame.draw.rect(win,back_ground_color,(position[0]*50+buffer,position[1]*50+buffer,50-2*buffer,50-2*buffer))
                    pygame.display.update()
                    
                if  (0 < event.key-48 < 10): #checking for valid inputs
                    pygame.draw.rect(win,back_ground_color,(position[0]*50+buffer,position[1]*50+buffer,50-2*buffer,50-2*buffer))
                    value = myfont.render(str(event.key-48),True,black)
                    win.blit(value,(position[0]*50+15,position[1]*50))
                    grid[i-1][j-1] = event.key -48
                    pygame.display.update()
                    return
                return



def main():
  pygame.init()
  win = pygame.display.set_mode((Width,Width))
  pygame.display.set_caption("Sudoku")
  win.fill(back_ground_color)
  myfont = pygame.font.SysFont("Comic Sans MS",35)
  
  #adding grid
  for i in range(0,10):
      if i%3 == 0:
          pygame.draw.line(win,black,(50+50*i,50),(50+50*i,500),4) #Bold lines
          pygame.draw.line(win,black,(50,50+50*i),(500,50+50*i),4)
          
      pygame.draw.line(win,black,(50+50*i,50),(50+50*i,500),2)
      pygame.draw.line(win,black,(50,50+50*i),(500,50+50*i),2)
  pygame.display.update()
  
  for i in range(0,len(grid[0])):
      for j in range(0,len(grid[0])):
          if  0<grid[i][j]<10 :
              value = myfont.render(str(grid[i][j]),True,blue)
              win.blit(value,((j+1)*50+20,(1+i)*50))    
  pygame.display.update()  


  while True:
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONUP and event.button ==1  :
          pos = pygame.mouse.get_pos()
          insert(win,(pos[0]//50,pos[1]//50)) # getting the grid number (index)
      if event.type == pygame.QUIT:
          pygame.quit()
          return    
main()
