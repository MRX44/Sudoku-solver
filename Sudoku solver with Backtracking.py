import pygame

Width = 550
back_ground_color = (0,0,0)

def main():
  pygame.init()
  win = pygame.display.set_mode((Width,Width))
  pygame.display.set_caption("Sudoku")

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        
        return
    
main()
