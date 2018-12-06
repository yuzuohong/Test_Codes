import pygame
import time

pygame.init()

display_width = 900
display_height = 800

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 235
car_height = 236

gameDisplay = pygame.display.set_mode((display_width,display_height),0,32)
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

filename = 'D:\Python\Test_Codes\images\\1.png'
filename2 = 'D:\Python\Test_Codes\images\\fish2.png'

carImg = pygame.image.load(filename)
fishImg = pygame.image.load(filename2)


def car(x,y):
    gameDisplay.blit(carImg,(x,y))
    gameDisplay.blit(fishImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text,True,red)
    return textSurface,textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',90)
    TextSurf,TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)

# function for message display and restarting the game
def crash():
    message_display('Crashed!! Try again!')
    game_loop()

def game_loop():

    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                
    x = (display_width * 0.5)
    y = (display_height * 0.6)

    x_change = 0
    y_change = 0

    # initialize 
    gameDisplay = pygame.display.set_mode((display_width,display_height),0,32)
    FullScreen = False

    gameExit = False

    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # activies at key pressings
            if event.type == pygame.KEYDOWN:

                # press 'f' key to toggle between full screen and normal screen
                if event.key == pygame.K_f:
                    FullScreen = not FullScreen
                    gameDisplay = pygame.display.set_mode((display_width,display_height),FullScreen,32)
                    pygame.display.update()

                # define motions for direction keys
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            # do nothing at a key release
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT\
                    or event.key == pygame.K_RIGHT\
                    or event.key == pygame.K_UP\
                    or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0
                
            print(event)
            
        x += x_change
        y += y_change

        # at a mouse click, the car moves to the mouse position
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()

        gameDisplay.fill(white)    
        car(x,y)

        # define boundaries
        if x > display_width - car_width + 20\
            or x < 0\
            or y > display_height - car_height + 20\
            or y < 0:
            
            crash()

        pygame.display.update()

        clock.tick(60)
        
# main loop of the game
game_loop()

# exit
pygame.quit()
quit()
    
