import pygame, sys , random , time 
pygame.init()
WIDTH, HEIGHT = 900, 700 
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Binary Search")

class btn:
	def __init__(self):
		self.x, self.y = 0, 0 
		self.width = 100
		self.height = 50 
		self.clicked = False 
		self.font = pygame.font.Font('freesansbold.ttf', 30).render('START', True, (255,255,255))

	def draw(self):
		if ((self.width + self.x > pygame.mouse.get_pos()[0] > self.x) and (self.height + self.y > pygame.mouse.get_pos()[1] > self.y)) : 
			self.color = (0,255,0)
			if True in pygame.mouse.get_pressed():
				self.clicked = True 
		else:
			self.color = (0,128,0) 

		pygame.draw.rect(SCREEN,self.color,pygame.Rect(self.x,self.y,self.width,self.height))
		SCREEN.blit(self.font,(0,0))

def sort(list_):
	for i in range(len(list_)):
		for j in range(i+1,len(list_)):
			if list_[i] > list_[j]:
				temp = list_[i]
				list_[i] = list_[j]
				list_[j] = temp

	return list_


if __name__ == '__main__': 

	# defining some animation variables
	list_ = []
	for i in range(60):
		list_.append(random.randrange(25,HEIGHT-25))

	list_ = sort(list_) 
	target_index = random.randrange(0,len(list_))
	target = list_[target_index]

	left, right = 0, len(list_)-1
	width = (WIDTH-(len(list_)*5)) // len(list_)
	found = False
	start = False
	initial_time = None
	end_time = None 

	start_btn = btn()
	mid = -1

	# game loop
	while True:
 		for event in pygame.event.get():
 			if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
 				pygame.quit()

 				sys.exit()

 		# background color and fonts
 		SCREEN.fill((255,255,255))
 		target_font = pygame.font.Font('freesansbold.ttf', 32).render(f'Target : {target_index}', True, (0,0,0))
 		SCREEN.blit(target_font, (WIDTH//2,0))

 		# start btn
 		start_btn.draw()
 		if start_btn.clicked:
 			start = True 
 			if initial_time == None: 
 				initial_time = time.time()

 		#animation stuff
 		x = 5 
 		for i in range(len(list_)):
 			if i == left or i == right:
 				color = (255,255,0)
 			if i == mid:
 				color = (255,0,0)
 				if list_[mid] == target:
 					color = (0,255,0)
 			if i!=left and i!=right and i!=mid :
 				color = (0,0,0)

 			y = HEIGHT - list_[i]

 			pygame.draw.rect(SCREEN,color,pygame.Rect(x,y,width,list_[i]))
 			x += (width+5) 

 		# binary search 
 		if start and not found: 
	 		if mid!=-1:
	 			if list_[mid] == target:
	 				found = True 
	 				end_time = time.time()
	 			elif list_[mid] < target:
	 				left = mid+1
	 			else:
	 				right = mid-1

	 		mid = (left+right)//2

	 	if found:
	 		time_taken_font = pygame.font.Font('freesansbold.ttf', 15).render(f'Time Taken : {(end_time - initial_time)}', True, (0,0,0))
	 		SCREEN.blit(time_taken_font, (0,50))


	 	pygame.time.Clock().tick(5)
	 	pygame.display.update()

