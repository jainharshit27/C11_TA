import pygame, pymunk
import pymunk.pygame_util

pygame.init()

height = 600
width = 690
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#pymunk space
gravity = 1000
wind = 200
space = pymunk.Space()
space.gravity = wind, gravity
draw_options = pymunk.pygame_util.DrawOptions(screen)

vs_rect = [(1, -80), (1, 80), (-1, 80), (-1, -80)]    #These are vertices for target
#Create target_body and assign pymunk.Body(body_type=pymunk.Body.KINEMATIC) to create KINEMATIC body for target.
#Create target_shape and assign pymunk.Poly(target_body, vs_rect) to give polygon shape to target.
#Create target_body.position and assign 600,400 for its position.
#Add target_body and target_shape using space.add(target_body, target_shape).

#Create bow_body and assign pymunk.Body(body_type=pymunk.Body.KINEMATIC) to create KINEMATIC body for bow.
#Create bow_shape and assign pymunk.Circle(bow_body, 25) to give circular shape to bow.
#Add a bow_shape.sensor as True
#Add bow_shape.color as (255, 50, 50, 255)
#Add bow_body.position and assign 100, 140 for its position.
#Add bow_body and bow_shape to space using space.add()

vs = [(-80, 0), (0, 2), (10, 0), (0, -2)]
#Create arrow_body and assign pymunk.Body() with KINEMATIC body type.
#Create arrow_shape and assign pymunk.Poly() with arrow_body, vs as body and vertices.
#Add density of 0.1 to shape using arrow_shape.density.
#Assign arrow_body.position the same position as bow_body.position.
#Add arrow_body and arrow_shape to space using space.add()

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Check if event.type == pygame.MOUSEBUTTONUP and event.button == 1, if yes do the following
            #Change arrow_body.body_type to pymunk.Body.DYNAMIC
            
    space.debug_draw(draw_options)
    pygame.display.update()
    
    clock.tick(60)
