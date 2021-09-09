import pygame
import requests

#window parameters
Width = 550
buffer = 6
solved = 0
#levels = [easy,medium,hard]

#calling API
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = response.json()['board']
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))] #creating a shallow copy

#colors
back_ground_color = (255,255,255)
black = (0,0,0)
blue= (52,31,155)

def isEmpty(num):
    if num == 0:
        return True
    return False
    

def isvalid(position,num):
    # the 3 constrains are col , row and box
    
    for i in range(0,len(grid[0])):                      #Row Check
        if grid[position[0]][i] == num :
            return False
        
    for i in range(0,len(grid[0])):                      #Column check
        if (grid[i][position[1]]) == num:
            return False

    #Box cordinates
    x = position[0]//3 *3
    y = position[1]//3 *3

    for i in range(0,3):                                 #Box check
        for j in range(0,3):
            if grid[x+i][y+j] == num:
                return False
    return True 

def sudoku_solver(win):
    myfont = pygame.font.SysFont("Comic Sans MS",35)
    for i in range(len(grid[0])):
        for j in range(len(grid[0])):
            if isEmpty(grid[i][j]):
                for k in range(1,10):
                    if isvalid((i,j),k):
                        grid[i][j] = k
                        pygame.draw.rect(win, back_ground_color, ((j+1)*50 + buffer, (i+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                        value = myfont.render(str(k),True,black)
                        win.blit(value, ((j+1)*50 +15,(i+1)*50))
                        pygame.display.update()
                        pygame.time.delay(50)

                        sudoku_solver(win)

                        #Exit condition
                        global solved
                        if solved == 1:
                            return
                        
                        #if sudoku_solver returns, there's a mismatch
                        grid[i][j]=0
                        pygame.draw.rect(win, back_ground_color, ((j+1)*50 + buffer, (i+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                        pygame.display.update()
                return
    solved = 1
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

  sudoku_solver(win)
  while True:
    for event in pygame.event.get():    
      if event.type == pygame.QUIT:
          pygame.quit()
          return    
main()
