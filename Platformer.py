# Pygame template



# initialize pygame and create window


all_sprites = pygame.sprite.Group()
# Game loop
running = True
while running:
	# keep loop running at the right speed
	clock.tick(FPS)
	# Process input (events)
	for event in pygame.event.get():
		# check for closing window
		if event.type == pygame.QUIT:
			running = False
	
	# Update

	# Draw / render
	wn.fill(BLACK)
	all_sprites.draw(wn)
	# *after* drawing everything, flip the display
	pygame.display.flip()

pygame.quit()