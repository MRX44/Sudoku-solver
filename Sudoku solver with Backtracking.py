import pygame

#window parameters
Width = 550

#colors
back_ground_color = (255,255,255)
black = (0,0,0)

def main():
  pygame.init()
  win = pygame.display.set_mode((Width,Width))
  pygame.display.set_caption("Sudoku")
  win.fill(back_ground_color)

  #adding grid
  for i in range(0,10):
      if i%3 == 0:
          pygame.draw.line(win,black,(50+50*i,50),(50+50*i,500),4) #Bold lines
          pygame.draw.line(win,black,(50,50+50*i),(500,50+50*i),4)
          
      pygame.draw.line(win,black,(50+50*i,50),(50+50*i,500),2)
      pygame.draw.line(win,black,(50,50+50*i),(500,50+50*i),2)

  pygame.display.update()  


  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        
        return
    
main()
