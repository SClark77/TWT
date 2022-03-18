# Pygame in 90 minutes
# from Tech With Tim youtube lesson

# make sure pygame module is installed [pip install pygame] from command line.

# import module
import pygame

# set display dimentions
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# give window a name
pygame.display.set_caption("TWT Game")

# set color variable
WHITE = (255, 255, 255)

# create a draw window function
def draw_window():
	# draw stuff on the screen

# fill screen with color
		win.fill(WHITE) # color values are R G B set in the WHITE Variable
# update Display
		pygame.display.update()



# create event loop
def main():
	
	run = True
	while run:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()




# check to only run main function if file was ran directly
if __name__ == "__main__":
	main() 