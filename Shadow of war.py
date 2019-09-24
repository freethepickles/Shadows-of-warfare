import pygame, time, random, mods, json
import logging
from sys import*

pygame.init()

#DEBUG#
print("Creating DEBUG.txt file")
text_file = open ("Log.txt", "w")
logging.basicConfig(filename='logfile.txt',level=logging.DEBUG)
#Mods import#
mods = 0
#Game cursor#


#sounds#
explostion_sound = pygame.mixer.Sound("explostion_sound.wav")
fire_sound = pygame.mixer.Sound("fire_sound.wav")
critical_sound = pygame.mixer.Sound("critical_sound.wav")
direct_sound = pygame.mixer.Sound("direct_sound.wav")
button_click_sound = pygame.mixer.Sound("button_click.wav")

text_file.write("Build 1.20\n")
text_file.write("begin log....\n")
text_file.write("-------------\n")
text_file.write("sounds loaded...\n")
text_file.write("Looking for Mod attributes...\n")
text_file.write("Number of attributes 0...\n")
text_file.write("we tried to add the asset file but it failed...\n")
print("Number of attributes",mods)
print("The game is now sentient RUN!!!!")

score = 0
##achievements = 0

#Color#
white = (255,255,255)
off_white = (180,183,79)
turtle_green = (90,130,0)
shade_of_tan  = (121,83,89)
black = (0,0,0)
gray = (192,192,192)
dark_gray = (127,127,127)   
dark_red = (128,0,0)
red = (200,0,0)
light_red = (255,0,0)
yellow = (200,200,0)
light_yellow = (255,255,0)
dark_blue = (0,64,128)
blue = ( 63,72,204)
light_blue =  (44,108,180)
sky_blue = (128,255,255)
navy_blue = (0,0,54)
aqua = (0,255,255)
cyan = (64,128,128)
green = (34,177,76)
light_green = (0,255,0)
dark_green = (0,128,64)
yellow_green = (128,255,0)
lime = (0,255,0)
orange = (255,128,0)
light_orange = (255,128,64)
brown = (128,64,0)
dark_brown = (62,31,0)
light_purple = (128,0,255)
dark_purple = (64,0,128)
pink = (255,0,28)
light_pink = (255,128,255)
gold = (185,185,0)
med_blue = (0,128,192)
muroon =(128, 0,64)
menu_button = (56,224,224)
menu_slect = (15,96,96)
text_file.write("Colors loaded.../n")

#Game Data#
X = 34
display_width = 900
display_height = 700
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Galatic War Build 1.20')
clock = pygame.time.Clock()
tankWidth = 40
tankHeight = 20
turretWidth = 5
wheelWidth = 5
ground_height = 45
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 70)
largefont = pygame.font.SysFont("comicsansms", 95)

print("Galatic war 1.20.1 Loaded")
print("---------------------------")
print("Whats new in 1.20.1")
print("---------------------------")
print("+Added story line")
print("+Added 1 new boss")
print("+Redesighned Win and loss screens")
print("+Redesighned Level Slect")
print("+Team slect")
print("+Rewrote Mod API (1.2.0)")
print("*The Game has been renamed")
print("*Improved pause menu")
print("*The game now loggs information useing a built in python script")
print("*Orgnized code to make updateing the game slimpler")
print("*Changed file structure")
print("*Updated Debug screen")
print(" A more detailed list is in the change log")


#defined variables#
def text_objects(text, color,size = "small"):
		
    if size == "small":    
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()
    
def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)

def message_to_screen(msg,color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (int(display_width / 2), int(display_height / 2)+y_displace)
    gameDisplay.blit(textSurf, textRect)
    
def message_to_game(msg,color, x, y, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    gameDisplay.blit(textSurf, textRect)


def tank(x,y,turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x-27, y-2),
                       (x-26, y-5),
                       (x-25, y-8),
                       (x-23, y-12),
                       (x-20, y-14),
                       (x-18, y-15),
                       (x-15, y-17),
					   (x-13, y-19),
                       (x-11, y-21)
                       ]

    pygame.draw.circle(gameDisplay, dark_gray, (x,y), int(tankHeight/2))
    pygame.draw.rect(gameDisplay, dark_gray, (x-tankHeight, y, tankWidth, tankHeight))
	
    pygame.draw.line(gameDisplay, dark_gray, (x,y), possibleTurrets[turPos], turretWidth)

    pygame.draw.circle(gameDisplay, dark_gray, (x-15, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, dark_gray, (x-10, y+20), wheelWidth)

    pygame.draw.circle(gameDisplay, dark_gray, (x-15, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, dark_gray, (x-10, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, dark_gray, (x-5, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, dark_gray, (x, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, dark_gray, (x+5, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, dark_gray, (x+10, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, dark_gray, (x+15, y+20), wheelWidth)

    return possibleTurrets[turPos]
    print(turPos)

def enemy_tank(x,y,turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x+27, y-2),
                       (x+26, y-5),
                       (x+25, y-8),
                       (x+23, y-12),
                       (x+20, y-14),
                       (x+18, y-15),
                       (x+15, y-17),
                       (x+13, y-19),
                       (x+11, y-21)
                       ]

    pygame.draw.circle(gameDisplay, dark_red, (x,y), int(tankHeight/2))
    pygame.draw.rect(gameDisplay, dark_red, (x-tankHeight, y, tankWidth, tankHeight))

    pygame.draw.line(gameDisplay, dark_red, (x,y), possibleTurrets[turPos], turretWidth)

    pygame.draw.circle(gameDisplay, dark_red, (x-15, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, dark_red, (x-10, y+20), wheelWidth)

    pygame.draw.circle(gameDisplay, dark_red, (x-15, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, dark_red, (x-10, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, dark_red, (x-5, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, dark_red, (x, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, dark_red, (x+5, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, dark_red, (x+10, y+20), wheelWidth)
    pygame.draw.circle(gameDisplay, dark_red, (x+15, y+20), wheelWidth)

    return possibleTurrets[turPos]
    
text_file.write("Variables loaded...\n")

def game_controls():

    gcont = True
    
    while gcont:
        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        gameDisplay.fill(black)
        message_to_screen("Controls",menu_slect,-200,size="large")
        message_to_screen("Fire: Space bar",menu_slect,-60)
        message_to_screen("Move Turret: Up and Down arrows",menu_slect,-30)
        message_to_screen("Move Tank: Left and Right arrows",menu_slect,0)
        message_to_screen("Increase power: D, Decrease power: A",menu_slect,30)
        message_to_screen("To pause the game: P",menu_slect,60)
        message_to_screen("Top Green bar is the health bar",menu_slect,90)
        message_to_screen("There will be an upgrade system in the next update ",menu_slect,120)
        message_to_screen("For Info about that Click the Upgrade info button",menu_slect,150)
        
        button("play", 50,550,150,50, menu_button, menu_slect, action="play")
        button("Back", 350,550,150,50, menu_button, menu_slect, action="main")
        button("Self destruct", 650,650,150,50,menu_button,menu_slect,action="self_destruct")
        button("Upgrade info", 50,650,150,50,menu_button,menu_slect,action="upgrade") 
        button("quit", 650,550,150,50, menu_button, menu_slect, action ="quit")
   
        pygame.display.update()
        clock.tick(15)
        
def duck():
     load = True
     while load:
         for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()


         gameDisplay.fill(black)
         message_to_screen("Level Select - Space ducks",menu_slect,-250,size="small")

         button("Level 1", 100,200,100,50, menu_button, menu_slect, action= "Level 1")
         button("Level 2", 100,260,100,50, menu_button, menu_slect, action= "Level 2")
         button("Level 3", 100,320,100,50, menu_button, menu_slect, action= "Level 3")
         button("Level 4", 100,380,100,50, menu_button, menu_slect, action= "Level 4")
         button("Level 5", 100,440,100,50, menu_button, menu_slect, action= "Level 5")

         button("Level 6", 250,200,100,50, menu_button, menu_slect, action= "Level 6")
         button("Level 7", 250,260,100,50, menu_button, menu_slect, action= "Level 7")
         button("Level 8", 250,320,100,50, menu_button, menu_slect, action= "Level 8")
         button("Level 9", 250,380,100,50, menu_button, menu_slect, action= "Level 9")
         button("Level 10", 250,440,100,50, menu_button, menu_slect, action= "Level 10")

         button("Level 11", 400,200,100,50, menu_button, menu_slect, action= "Level 11")
         button("Level 12", 400,260,100,50, menu_button, menu_slect, action= "Level 12")
         button("Level 13", 400,320,100,50, menu_button, menu_slect, action= "Level 13")
         button("Boss 1", 400,380,120,50, menu_button, menu_slect, action= "Level 14")
         button("Boss 2", 400,440,120,50, menu_button, menu_slect, action= "Level 15")
         button("Boss 3", 550,200,120,50, menu_button, menu_slect, action= "Level 15")
         
         button("Back", 450,500,100,50, menu_button, menu_slect, action ="main")


         pygame.display.update()

         clock.tick(15)
def load():
     load = True
     while load:
         for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()


         gameDisplay.fill(black)
         message_to_screen("Level Select - Central Command",menu_slect,-250,size="small")

         button("Level 1", 100,200,100,50, menu_button, menu_slect, action= "Level 1")
         button("Level 2", 100,260,100,50, menu_button, menu_slect, action= "Level 2")
         button("Level 3", 100,320,100,50, menu_button, menu_slect, action= "Level 3")
         button("Level 4", 100,380,100,50, menu_button, menu_slect, action= "Level 4")
         button("Level 5", 100,440,100,50, menu_button, menu_slect, action= "Level 5")

         button("Level 6", 250,200,100,50, menu_button, menu_slect, action= "Level 6")
         button("Level 7", 250,260,100,50, menu_button, menu_slect, action= "Level 7")
         button("Level 8", 250,320,100,50, menu_button, menu_slect, action= "Level 8")
         button("Level 9", 250,380,100,50, menu_button, menu_slect, action= "Level 9")
         button("Level 10", 250,440,100,50, menu_button, menu_slect, action= "Level 10")

         button("Level 11", 400,200,100,50, menu_button, menu_slect, action= "Level 11")
         button("Level 12", 400,260,100,50, menu_button, menu_slect, action= "Level 12")
         button("Level 13", 400,320,100,50, menu_button, menu_slect, action= "Level 13")
         button("Space Duck", 400,380,190,50, menu_button, menu_slect, action= "Level 14")
         button("Space Cow", 400,440,190,50, menu_button, menu_slect, action= "Level 15")
         button("Ban hammer", 550,200,190,50, menu_button, menu_slect, action= "Level 15")
         
         button("Back", 450,500,100,50, menu_button, menu_slect, action ="main")


         pygame.display.update()

         clock.tick(15)



        
def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.mixer.Sound.play(button_click_sound)
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        achievements = 0
        
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "controls":
                game_controls()
                print("loading Controls")

            if action == "upgrade":
                upgrade()

            if action == "main":
                print("Loading Menu")
                game_intro()
                

            if action == "load":
                achievements += 1
                print("Added one to Achievements")
                print("Displaying Levels")
                print("Player selected Central Command")
                load()
                

            if action == "Level 1":
                print("Displaying Level 1")
                chapter()
                

               
            if action == "Level 2":
                print("Displaying Level 2")

                level2()
                
            if action == "Level 3":
                print("Displaying Level 3")
                level()
                

            if action == "Level 4":
                print("Displaying Level  4")
                next()
                

            if action == "Level 5":
                print("Displaying Level  5")
                time()
                

            if action == "Level 6":
                print("Displaying Level  6")
                bob()
                

            if action == "Level 7":
                print("Displaying Level  7")
                joe()
                

            if action == "Level 8":
              print("Displaying Level  8")
              ted()
              

            if action == "Level 9":
              print("Displaying Level  9")
              jon()
              

            if action == "Level 10":
              print("Displaying Level  10")
              jack()
              

            if action == "Level 11":
              print("Displaying Level  11")
              jeb()
              

            if action == "Level 12":
              print("Displaying Level  12")
              sal()
              

            if action == "Level 13":
              print("Displaying Level  13")
              tim()
              

            if action == "Level 14":
              print("Displaying Level  14")
              pal()
              

            if action == "Level 15":
              print("Displaying Level  15")
              foe()
              

            if action == "mods":
                mods()
                
            if action == "info":
                info()
            
            if action == "ver":
                ver()    
                
            if action =="self_destruct":
                self_destruct()
                
            if action =="upgrade":
                upgrade()

            if action =="Stl":
                Stl()
                
            if action =="Tea":
                Tea()   
                
            if action =="duck":
                print("Player selected space ducks")
                duck() 
                
            if action =="csl":
                csl()
                

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))

    text_to_button(text,black,x,y,width,height)




def pause():

    paused = True
    message_to_screen("Paused",dark_red,-100,size="large")
    message_to_screen("Press C to continue playing, M for Main Menu or Q to Quit",black,25)

    pygame.display.update()
    while paused:
        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False

                    if event.key == pygame.K_m:
                      game_intro()

                    elif event.key == pygame.K_q:
                      pygame.quit()
                      quit()




        clock.tick(30)


   
   
def explosion(x, y, size=20):



    explode = True

    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startPoint = x,y
        colorChoices = [red, black, yellow, dark_gray, dark_red, gold, gray]

        magnitude = 3

        while magnitude < size:

            exploding_bit_x = x +random.randrange(-1*magnitude,magnitude)
            exploding_bit_y = y +random.randrange(-1*magnitude,magnitude)
   
            pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0,7)], (exploding_bit_x,exploding_bit_y),random.randrange(1,5))
            magnitude += 1
            

            pygame.display.update()
            clock.tick(60)

        explode = False
        
def partical_supper(x, y, size=50):



    partical_supper = True

    while partical_supper:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startPoint = x,y

        colorChoices = [cyan, orange, gold]

        magnitude = 5

        while magnitude < size:

            exploding_bit_x = x +random.randrange(-1*magnitude,magnitude)
            exploding_bit_y = y +random.randrange(-1*magnitude,magnitude)           
            pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0,3)], (exploding_bit_x,exploding_bit_y),random.randrange(1,3))
            magnitude += 1

            pygame.display.update()
            clock.tick(60)

        partical_supper = False 


        
def partical_critical(x, y, size=50):



    partical_critical = True

    while partical_critical:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startPoint = x,y

        colorChoices = [dark_purple, dark_blue, dark_green]

        magnitude = 5

        while magnitude < size:

            exploding_bit_x = x +random.randrange(-1*magnitude,magnitude)
            exploding_bit_y = y +random.randrange(-1*magnitude,magnitude)

            pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0,3)], (exploding_bit_x,exploding_bit_y),random.randrange(1,3))
            magnitude += 1

            pygame.display.update()
            clock.tick(60)

        partical_critical = False 
        print("Game says: Improved the AI yea right!")

def partical_direct(x, y, size=50):



    partical_direct = True

    while partical_direct:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startPoint = x,y

        colorChoices = [pink, med_blue, muroon]

        magnitude = 3

        while magnitude < size:

            exploding_bit_x = x +random.randrange(-1*magnitude,magnitude)
            exploding_bit_y = y +random.randrange(-1*magnitude,magnitude)

            pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0,3)], (exploding_bit_x,exploding_bit_y),random.randrange(1,3))
            magnitude += 1

            pygame.display.update()
            clock.tick(60)

        partical_direct = False 
        
def partical_hard(x, y, size=50):



    partical_hard = True

    while partical_hard:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startPoint = x,y

        colorChoices = [pink, white, red]

        magnitude = 3

        while magnitude < size:

            exploding_bit_x = x +random.randrange(-1*magnitude,magnitude)
            exploding_bit_y = y +random.randrange(-1*magnitude,magnitude)

            pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0,3)], (exploding_bit_x,exploding_bit_y),random.randrange(1,3))
            magnitude += 1

            pygame.display.update()
            clock.tick(60)

        partical_hard = False 
        
def partical_medium(x, y, size=50):



    partical_medium = True

    while partical_medium:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startPoint = x,y

        colorChoices = [navy_blue, light_green, light_orange]

        magnitude = 3

        while magnitude < size:

            exploding_bit_x = x +random.randrange(-1*magnitude,magnitude)
            exploding_bit_y = y +random.randrange(-1*magnitude,magnitude)

            pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0,3)], (exploding_bit_x,exploding_bit_y),random.randrange(1,3))
            magnitude += 1

            pygame.display.update()
            clock.tick(60)

        partical_medium = False 
        
def partical_light(x, y, size=50):



    partical_light = True

    while partical_light:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startPoint = x,y

        colorChoices = [green, dark_green, aqua]

        magnitude = 3

        while magnitude < size:

            exploding_bit_x = x +random.randrange(-1*magnitude,magnitude)
            exploding_bit_y = y +random.randrange(-1*magnitude,magnitude)

            pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0,3)], (exploding_bit_x,exploding_bit_y),random.randrange(1,3))
            magnitude += 1

            pygame.display.update()
            clock.tick(60)

        partical_light = False  
        
        
        
def firebullet(xy,tankx,tanky,turPos,gun2_power,xlocation,randomHeight,enemyTankX, enemyTankY):
    firebullet= True
    damage = 0

    startingShell = list(xy)
    pygame.mixer.Sound.play(fire_sound)
    
    print("FIRE!",xy)

    while firebullet:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        
        print(startingShell[0],startingShell[1])
        pygame.draw.circle(gameDisplay, green, (startingShell[0],startingShell[1]),5)


        startingShell[0] -= (12 - turPos)*2

        # y = x**2
        startingShell[1] += int((((startingShell[0]-xy[0])*0.015/(gun_power/50))**2) - (turPos+turPos/(12-turPos)))

        if startingShell[1] > display_height-ground_height:
            #print("Last shell:",startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]*display_height-ground_height)/startingShell[1])
            hit_y = int(display_height-ground_height)
            #print("Impact:", hit_x,hit_y)
            
                
            if enemyTankX + 10 > hit_x > enemyTankX - 10:
                print("Direct! bullet")
                damage = 12
                partical_direct(hit_x,hit_y)
                pygame.mixer.Sound.play(direct_sound)
                
                

            elif enemyTankX + 25 > hit_x > enemyTankX - 25:
                print("hard!")
                damage = 10
                partical_hard(hit_x,hit_y)
                pygame.mixer.Sound.play(explostion_sound)
              
            elif enemyTankX + 30 > hit_x > enemyTankX - 30:
                print("medium! bullet")
                damage = 8
                partical_medium(hit_x,hit_y)
                pygame.mixer.Sound.play(explostion_sound)

                

            elif enemyTankX + 35 > hit_x > enemyTankX - 35:
                print("light bullet!")
                damage = 6
                partical_light(hit_x,hit_y)
                pygame.mixer.Sound.play(explostion_sound)
 
                




            explosion(hit_x,hit_y)
            firebullet = False

        check_x_1 = startingShell[0] <= xlocation
        check_x_2 = startingShell[0] >= xlocation

        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            #print("Last shell:",startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])
            #print("Impact:", hit_x,hit_y)
            explosion(hit_x,hit_y)
            firebullet = False


        pygame.display.update()
        
        clock.tick(60)
    return damage
    
def fireShell(xy,tankx,tanky,turPos,gun_power,xlocation,randomHeight,enemyTankX, enemyTankY):
    fire = True
    damage = 0
    damage_a = 0
    



    startingShell = list(xy)
    pygame.mixer.Sound.play(fire_sound)

    #print("FIRE!",xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        
        #print(startingShell[0],startingShell[1])
        pygame.draw.circle(gameDisplay, dark_blue, (startingShell[0],startingShell[1]),5)


        startingShell[0] -= (12 - turPos)*2

        # y = x**2
        startingShell[1] += int((((startingShell[0]-xy[0])*0.015/(gun_power/50))**2) - (turPos+turPos/(12-turPos)))

        if startingShell[1] > display_height-ground_height:
            #print("Last shell:",startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]*display_height-ground_height)/startingShell[1])
            hit_y = int(display_height-ground_height)
            #print("Impact:", hit_x,hit_y)
            
            
            
            if enemyTankX + 2 > hit_x > enemyTankX - 2:
                print("player - Super Attack")
                damage = 55             
                damage_a = 33
                partical_supper(hit_x,hit_y)
                pygame.mixer.Sound.play(explostion_sound)

            if enemyTankX + 5 > hit_x > enemyTankX - 5:
                print("player - critical!")
                damage = 22
                damage_a = 11
                partical_critical(hit_x,hit_y)
                pygame.mixer.Sound.play(critical_sound)
                
            elif enemyTankX + 10 > hit_x > enemyTankX - 10:
                print("player - Direct!")
                damage = 19
                damage_a = 9
                partical_direct(hit_x,hit_y)
                pygame.mixer.Sound.play(direct_sound)
                
                

            elif enemyTankX + 25 > hit_x > enemyTankX - 25:
                print("player - hard!")
                damage = 16
                damage_a = 8
                partical_hard(hit_x,hit_y)
                pygame.mixer.Sound.play(explostion_sound)
              
            elif enemyTankX + 30 > hit_x > enemyTankX - 30:
                print("player - medium!")
                damage = 12
                damage_a = 6
                partical_medium(hit_x,hit_y)
                pygame.mixer.Sound.play(explostion_sound)

                

            elif enemyTankX + 35 > hit_x > enemyTankX - 35:
                print("player - light!")
                damage = 10
                damage_a = 5
                partical_light(hit_x,hit_y)
                pygame.mixer.Sound.play(explostion_sound)
                
            else:
                print("player - missed")
                        




            explosion(hit_x,hit_y)
            fire = False

        check_x_1 = startingShell[0] <= xlocation
        check_x_2 = startingShell[0] >= xlocation

        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            #print("Last shell:",startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])
            #print("Impact:", hit_x,hit_y)
            explosion(hit_x,hit_y)
            fire = False


        pygame.display.update()
        
        clock.tick(60)
    return damage
    return damage_a



def e_fireShell(xy,tankx,tanky,turPos,gun_power,xlocation,randomHeight,ptankx,ptanky):

    damage = 0
    damage_a = 0
    currentPower = 1
    power_found = False
    points = 0

    while not power_found:
        currentPower += 1
        if currentPower > 100:
            power_found = True
        

        fire = True
        startingShell = list(xy)
        pygame.mixer.Sound.play(fire_sound)

        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                        
            
            startingShell[0] += (12 - turPos)*2

            gun_power  = random.randrange(int(currentPower*0.60), int(currentPower*1.99))
            startingShell[1] += int((((startingShell[0]-xy[0])*0.015/(gun_power/50))**2) - (turPos+turPos/(12-turPos)))

            if startingShell[1] > display_height-ground_height:
                hit_x = int((startingShell[0]*display_height-ground_height)/startingShell[1])
                hit_y = int(display_height-ground_height)
                #explosion(hit_x,hit_y)
                if ptankx+15 > hit_x > ptankx - 15:
                    #print("target acquired!")
                    power_found = True
                fire = False

            check_x_1 = startingShell[0] <= xlocation
            check_x_2 = startingShell[0] >= xlocation

            check_y_1 = startingShell[1] <= display_height
            check_y_2 = startingShell[1] >= display_height - ground_height

            if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                hit_x = int((startingShell[0]))
                hit_y = int(startingShell[1])
                #explosion(hit_x,hit_y)
                fire = False



    fire = True
    startingShell = list(xy)
    #print("FIRE!",xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #print(startingShell[0],startingShell[1])
        pygame.draw.circle(gameDisplay, dark_red, (startingShell[0],startingShell[1]),5)
        startingShell[0] += (12 - turPos)*2
        # y = x**2
        startingShell[1] += int((((startingShell[0]-xy[0])*0.015/(currentPower/50))**2) - (turPos+turPos/(12-turPos)))
        if startingShell[1] > display_height-ground_height:
            #print("last shell:",startingShell[0],startingShell[1])
            hit_x = int((startingShell[0]*display_height-ground_height)/startingShell[1])
            hit_y = int(display_height-ground_height)
            #print("Impact:",hit_x,hit_y)
            
            if ptankx + 1> hit_x > ptankx - 1:
                print("Enemy - debuff2!")    
                damage_a = 40
                damage = 80
                partical_critical(hit_x,hit_y)
                pygame.mixer.Sound.play(explostion_sound)
                
            elif ptankx + 2 > hit_x > ptankx - 2:
                print("enemy - debuff!")  
                damage_a = 25
                damage = 50
                partical_critical(hit_x,hit_y)
                pygame.mixer.Sound.play(explostion_sound)
                
            elif ptankx + 5 > hit_x > ptankx - 5:
                print("enemy - critical!")  
                damage_a = 22
                damage = 45
                partical_critical(hit_x,hit_y)
                pygame.mixer.Sound.play(explostion_sound)
                
            elif ptankx + 10 > hit_x > ptankx - 10:
                print(" enemy - Direct!")
                damage_a = 20
                damage = 40
                partical_direct(hit_x,hit_y)
                pygame.mixer.Sound.play(explostion_sound)
                
            elif ptankx + 15 > hit_x > ptankx - 15:
                print("enemy - hard!")
                damage_a =  16
                damage = 32
                partical_hard(hit_x,hit_y)
                pygame.mixer.Sound.play(explostion_sound)

            elif ptankx + 20 > hit_x > ptankx - 20:
                print("enemy - medium!")
                damage_a = 11
                damage = 22
                partical_medium(hit_x,hit_y)
                pygame.mixer.Sound.play(explostion_sound)

            elif ptankx + 25 > hit_x > ptankx - 25:
                print("enemy - light!")
                damage_a = 4  
                damage = 8
                
                partical_light(hit_x,hit_y)
                pygame.mixer.Sound.play(explostion_sound)
                
            else:
                print("enemy - missed")
            explosion(hit_x,hit_y)
            fire = False

        check_x_1 = startingShell[0] <= xlocation
        check_x_2 = startingShell[0] >= xlocation
        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            #print("Last shell:",startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])
            #print("Impact:", hit_x,hit_y)
            explosion(hit_x,hit_y)
            fire = False

        pygame.display.update()
        clock.tick(60)
    return damage
    return damage_a
    

def power(level):

    text = smallfont.render("Tank power: "+str(level)+"%",True, dark_red)
    gameDisplay.blit(text, [display_width/8,0])
    


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        intro = False
                    elif event.key == pygame.K_q:

                        pygame.quit()
                        quit()
                        

            
        gameDisplay.fill(black)
        message_to_screen("Welcome to Galtic war!  ",menu_slect,-250,size="medium")
    
        button("Play", 100,300,120,50, menu_button, menu_slect, action="Level 1")
        button("Controls", 100,360,120,50, menu_button, menu_slect, action="controls")
        button("Mods", 100, 420, 120, 50, menu_button, menu_slect, action="mods")
        button("Teams", 350, 300, 120, 50, menu_button, menu_slect, action="Tea")
        button("Story line", 350, 360, 120, 50, menu_button, menu_slect, action="Stl")
        button("Info", 350, 420, 120, 50, menu_button, menu_slect, action="info")
        button("Version", 600, 300, 120, 50, menu_button, menu_slect, action="ver")
        button("Level select", 600,360,150,50, menu_button, menu_slect, action="load")
        button("Quit", 600,420,120,50, menu_button, menu_slect, action ="quit")
        
        message_to_screen("Update 1.20",menu_slect,260,size="small")
        message_to_screen("Mod API 1.2.0_A",menu_slect,300,size="small")
        
        pygame.display.update()
        clock.tick(15)
        #game_intro()
        
        
def Tea():

    Tea = True

    while upgrade:
        for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        intro = False
                    elif event.key == pygame.K_q:

                        pygame.quit()
                        quit()
                        
       
        gameDisplay.fill(black)
        message_to_screen("Choose a side",menu_slect,-250,size="medium")
        button("Space ducks", 150,550,190,50, menu_button, menu_slect, action ="duck")
        button("Central Command", 350,550,195,50, menu_button, menu_slect, action ="load")
        button("Back", 650,550,120,50, menu_button, menu_slect, action ="main")
        
        pygame.display.update()
        clock.tick(15)       
        
def csl():

    csl = True

    while upgrade:
        for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        intro = False
                    elif event.key == pygame.K_q:

                        pygame.quit()
                        quit()
                        
       
        gameDisplay.fill(black)
        message_to_screen("Story Line - Space ducks",menu_slect,-250,size="small")
        message_to_screen("The Galaxy has been Split in two one side Commanded by a gay will an attitude.",menu_slect,-160,size="small")
        message_to_screen("The other The Space Ducks ,",menu_slect,-130,size="small")
        message_to_screen("if you choose The space ducks your mission is to...,",menu_slect,-100,size="small")
        message_to_screen("So go and destroy the guy will an attitude and his army!!!",menu_slect,-70,size="small")
        message_to_screen("You must face Him, His second in command, and is head of operations!!!",menu_slect,-40,size="small")
        message_to_screen("Once you do this his control over the galaxy will be disbanded!!!",menu_slect,-10,size="small")
        
        
        button("Central command", 100,550,120,50, menu_button, menu_slect, action ="Stl")
        button("Back", 500,550,120,50, menu_button, menu_slect, action ="main")
        
        pygame.display.update()
        clock.tick(15)              
def Stl():

    Stl = True

    while upgrade:
        for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        intro = False
                    elif event.key == pygame.K_q:

                        pygame.quit()
                        quit()
                        
       
        gameDisplay.fill(black)
        message_to_screen("Story Line - Command Central",menu_slect,-250,size="small")
        message_to_screen("The Galaxy has been Split in two one side Commanded by a space duck.",menu_slect,-160,size="small")
        message_to_screen("The other Central command,",menu_slect,-130,size="small")
        message_to_screen("if you choose Central command your mission is to...,",menu_slect,-100,size="small")
        message_to_screen("So go and destroy the space duck and his army!!!",menu_slect,-70,size="small")
        message_to_screen("You must face Him, His second in command, and is head of operations!!!",menu_slect,-40,size="small")
        message_to_screen("Once you do this his control over the galaxy will be disbanded!!!",menu_slect,-10,size="small")
        
        
        button("Space Ducks", 100,550,120,50, menu_button, menu_slect, action ="csl")
        button("Back", 450,550,120,50, menu_button, menu_slect, action ="main")
        
        pygame.display.update()
        clock.tick(15)             

def upgrade():

    upgrade = True

    while upgrade:
        for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        intro = False
                    elif event.key == pygame.K_q:

                        pygame.quit()
                        quit()
                        
       
        gameDisplay.fill(black)
        message_to_screen("Upgrade Info",menu_slect,-250,size="medium")
        message_to_screen("Upgrade has not been added yet when it is the information will be show here",menu_slect,-160,size="small")

        button("Back", 450,550,120,50, menu_button, menu_slect, action ="main")
        
        pygame.display.update()
        clock.tick(15)             
def ver():

    ver = True

    while ver:
        for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        intro = False
                    elif event.key == pygame.K_q:

                        pygame.quit()
                        quit()
                        
       
        gameDisplay.fill(black)
        message_to_screen("Version 1.20 Change log",menu_slect,-250,size="medium")       
        message_to_screen("Log can be founed in Change log folder", menu_slect, -160, size="small")
        button("Back", 450,550,120,50, menu_button, menu_slect, action ="main")
        
        pygame.display.update()
        clock.tick(15)     
        
def info():

    info = True

    while info:
        for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        intro = False
                    elif event.key == pygame.K_q:

                        pygame.quit()
                        quit()
                        
       
        gameDisplay.fill(black)
        message_to_screen("Information",menu_slect,-250,size="large")
        message_to_screen("This Game was originality intended to be a joke.",menu_slect,-160,size="small")
        message_to_screen("However with the help of Austin, Addison, DJ, Jon, and Jared", menu_slect, -100, size="small")
        message_to_screen("We decided to take this game as far as we could.", menu_slect, -5, size="small")
        message_to_screen("So were we are two years later.", menu_slect, 45, size="small")
        message_to_screen("The only two people that will ever read this will probably be ", menu_slect, 90, size="small")
        message_to_screen("Me and Addison so i dont know why i still do this, probably because I can", menu_slect, 130, size="small")
        button("Back", 450,550,120,50, menu_button, menu_slect, action ="main")
        
        pygame.display.update()
        clock.tick(15)  
        
def mods():

    mods = True

    while mods:
        for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        intro = False
                    elif event.key == pygame.K_q:

                        pygame.quit()
                        quit()
                        
       
        gameDisplay.fill(black)
        message_to_screen("Mods",menu_slect,-250,size="large")
        message_to_screen("The mod maker should have registered the mod with the game ",menu_slect,-160,size="small")
        message_to_screen("All registered mods will be shown on this screen", menu_slect, -100, size="small")
        message_to_screen("Attributes: 0 of 0 ", menu_slect, -5, size="small")
        message_to_screen("Compatible with: Developmental version 100117", menu_slect, 45, size="small")
        message_to_screen("Mod API version: 1.1.0_A", menu_slect, 90, size="small")
        message_to_screen("Currently testing Mod API version: ----", menu_slect, 130, size="small")
        button("Back", 450,550,120,50, menu_button, menu_slect, action ="main")
        
        pygame.display.update()
        clock.tick(15)

def game_over():
     game_over = True
     while game_over:
         for event in pygame.event.get():

                if event.type == pygame.QUIT: 
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()

         gameDisplay.fill(black)
         message_to_screen("Game over",menu_slect,-250,size="large")
         message_to_screen("You loose",menu_slect,-250,size="small")         
         button("Back", 450,500,100,50, menu_button, menu_slect, action ="load")

         pygame.display.update()

         clock.tick(120)
def you_win():
     you_win = True
     while you_win:
         for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()

                gameDisplay.fill(black)
                message_to_screen("Victory!",menu_slect,-250,size="large")
                message_to_screen("You have won",menu_slect,-550,size="small")               
                button("Back", 450,500,100,50, menu_button, menu_slect, action ="load")

                pygame.display.update()

                clock.tick(60)

def bann_win():
    bann_win = True
    while bann_win:
         for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()

                gameDisplay.fill(black)
                message_to_screen("You have beaten the Ban hammer",menu_slect,-250,size="small")
                button("Back", 450,500,100,50, menu_button, menu_slect, action ="load")

                pygame.display.update()

                clock.tick(60)

def space_win():
     space_win = True
     while space_win:
         for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()

                gameDisplay.fill(black)
                message_to_screen("You have beaten the Space duck",menu_slect,-250,size="small")
                button("Back", 650,500,100,50, menu_button, menu_slect, action ="load")

                pygame.display.update()

                clock.tick(60)

def tie():
     tie = True
     while tie:
         for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()

                gameDisplay.fill(black)
                message_to_screen("You have tied",menu_slect,-250,size="medium")
                message_to_screen("Apparently that's a thing now!",menu_slect,-250,size="medium")
                button("Back", 650,500,100,50, menu_button, menu_slect, action ="load")

                pygame.display.update()

                clock.tick(60)
#health
def health_bars(player_health, enemy_health):

    if player_health > 100:
        player_health_color = green
        
    elif player_health > 75:
        player_health_color = yellow
        
    elif player_health > 50:
        player_health_color = orange
        
    elif player_health > 25:
        player_health_color = red
        
    else:
        player_health_color = dark_red
        if player_health < 0:
            player_health = 0
            print("player health",player_health)
    
            
     

    if enemy_health > 100:
        enemy_health_color = green
        
    elif enemy_health > 75:
        enemy_health_color = yellow

    elif enemy_health > 50:
        enemy_health_color = orange
        
    elif enemy_health > 25:
        enemy_health_color = red
    else:
        enemy_health_color = dark_red
        if enemy_health < 0:
            enemy_health = 0
            print("Enemy health",enemy_health)

    pygame.draw.rect(gameDisplay, player_health_color, (680, 25, player_health, 25))
    pygame.draw.rect(gameDisplay, enemy_health_color, (20, 25, enemy_health, 25))
    
   

    

# main Gameloop


def foe():
    gameExit = False
    gameOver = False
    FPS = 60

    player_health = 120
    enemy_health = 190
    

    barrier_width = 0

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9

    fire_power = 60
    points = 0
    
    power_change = 0
    
    xlocation = (display_width/2) + random.randint(-0.2*display_width, 0.2*display_width)
    randomHeight = random.randrange(display_height*0.1,display_height*0.6)

    while not gameExit:


        if gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",red,-50,size="large")
            message_to_screen("Press C to play again or Q to exit",black,50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5




                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_z:        
                  pygame.image.save(gameDisplay, "bin/assets/screenshots/screenshot.png")



                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_ESCAPE:
                    pause()




                elif event.key == pygame.K_SPACE:
                    damage = fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,randomHeight,enemyTankX,enemyTankY)
                    enemy_health -= damage
                    enemyTankX += 3
                    points +=1 
                    
                    

                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange (0,2)

                    for x in range(random.randrange(0,10)):
                        if display_width *0.3 > enemyTankX >display_width *0.03:
                            if possibleMovement [moveIndex] == "f":
                                enemyTankX += 5
                            elif possibleMovement [moveIndex] == "r":
                                enemyTankX -= 5

                            gameDisplay.fill(white)
                            health_bars(player_health,enemy_health)
                            gun = tank(mainTankX,mainTankY,currentTurPos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                            fire_power += power_change
                            
                            if fire_power > 100:
                                fire_power = 100
                            elif fire_power < 1:
                                fire_power = 1
                                



                            clock.tick(FPS)


                    damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,randomHeight,mainTankX,mainTankY)
                    player_health -= damage

                    
                elif event.key == pygame.K_n:
                    damage = firebullet(gun2,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,randomHeight,enemyTankX,enemyTankY)
                    enemy_health -= damage
                    
                    

                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange (0,2)

                    for x in range(random.randrange(0,10)):
                        if display_width *0.3 > enemyTankX >display_width *0.03:
                            if possibleMovement [moveIndex] == "f":
                                enemyTankX += 5
                            elif possibleMovement [moveIndex] == "r":
                                enemyTankX -= 5

                            gameDisplay.fill(white)
                            health_bars(player_health,enemy_health)

                            gun2 = tank(mainTankX,mainTankY,currentTurPos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                            fire_power += power_change
                            
                            if fire_power > 100:
                                fire_power = 100
                            elif fire_power < 1:
                                fire_power = 1
                                



                            clock.tick(FPS)


                    damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,randomHeight,mainTankX,mainTankY)
                    player_health -= damage
                    

                    
                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0





        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0


        if mainTankX - (tankWidth/2) < xlocation:
            mainTankX += 5


        gameDisplay.fill(light_blue)
        health_bars(player_health,enemy_health)
        gun = tank(mainTankX,mainTankY,currentTurPos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        fire_power += power_change

        power(fire_power)
        if player_health < 65:
            fire_power = 35           
          
            




        gameDisplay.fill(light_yellow, rect=[0, display_height-ground_height, display_width, ground_height])
        pygame.display.update()

        if player_health < 1 :
            game_over()
        if enemy_health < 1 :
            bann_win()
        elif player_health < 1:
            tie()



        clock.tick(FPS)
    pygame.quit()
    quit()

def pal():
    gameExit = False
    gameOver = False
    FPS = 60

    player_health = 120
    enemy_health = 190




    barrier_width = 0

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9




    fire_power = 60
    points = 0
    
    power_change = 0



    xlocation = (display_width/2) + random.randint(-0.2*display_width, 0.2*display_width)
    randomHeight = random.randrange(display_height*0.1,display_height*0.6)





    while not gameExit:


        if gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",red,-50,size="large")
            message_to_screen("Press C to play again or Q to exit",black,50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5




                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_z:
                  pygame.image.save(gameDisplay, "bin/assets/screenshots/screenshot.png")



                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_ESCAPE:
                    pause()

                elif event.key == pygame.K_SPACE:
                    damage = fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,randomHeight,enemyTankX,enemyTankY)
                    enemy_health -= damage
                    points +=1

                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange (0,2)

                    for x in range(random.randrange(0,10)):
                        if display_width *0.3 > enemyTankX >display_width *0.03:
                            if possibleMovement [moveIndex] == "f":
                                enemyTankX += 5
                            elif possibleMovement [moveIndex] == "r":
                                enemyTankX -= 5

                            gameDisplay.fill(white)
                            health_bars(player_health,enemy_health)                           
                            gun = tank(mainTankX,mainTankY,currentTurPos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                            fire_power += power_change



                            clock.tick(FPS)


                    damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,randomHeight,mainTankX,mainTankY)
                    player_health -= damage

                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0





        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0


        if mainTankX - (tankWidth/2) < xlocation:
            mainTankX += 5


        gameDisplay.fill(light_blue)
        health_bars(player_health,enemy_health)        
        gun = tank(mainTankX,mainTankY,currentTurPos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        fire_power += power_change

        power(fire_power)
        if player_health < 60:
            fire_power = 40           
        




        gameDisplay.fill(black, rect=[0, display_height-ground_height, display_width, ground_height])
        pygame.display.update()
        ##print("The game says: Finding ways to corrupt data")

        if player_health < 1:
            game_over()
        if enemy_health < 1:
            space_win()



        clock.tick(FPS)
    pygame.quit()
    quit()

def tim():
    gameExit = False
    gameOver = False
    FPS = 60

    player_health = 120
    enemy_health = 190


    barrier_width = 0

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9




    fire_power = 60
    points = 0
    
    power_change = 0
    if player_health < 58:
        fire_power = 59   


    xlocation = (display_width/2) + random.randint(-0.2*display_width, 0.2*display_width)
    randomHeight = random.randrange(display_height*0.1,display_height*0.6)

    while not gameExit:


        if gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",red,-50,size="large")
            message_to_screen("Press C to play again or Q to exit",black,50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5

                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_z:
                  pygame.image.save(gameDisplay, "bin/assets/screenshots/screenshot.png")



                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_ESCAPE:
                    pause()

                elif event.key == pygame.K_SPACE:
                    damage = fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,randomHeight,enemyTankX,enemyTankY)
                    enemy_health -= damage
                    points +=1

                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange (0,2)

                    for x in range(random.randrange(0,10)):
                        if display_width *0.3 > enemyTankX >display_width *0.03:
                            if possibleMovement [moveIndex] == "f":
                                enemyTankX += 5
                            elif possibleMovement [moveIndex] == "r":
                                enemyTankX -= 5

                            gameDisplay.fill(white)
                            health_bars(player_health,enemy_health)
                            gun = tank(mainTankX,mainTankY,currentTurPos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                            fire_power += power_change



                            clock.tick(FPS)


                    damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,randomHeight,mainTankX,mainTankY)
                    player_health -= damage

                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0





        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0


        if mainTankX - (tankWidth/2) < xlocation:
            mainTankX += 5


        gameDisplay.fill(light_blue)
        health_bars(player_health,enemy_health)
        gun = tank(mainTankX,mainTankY,currentTurPos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        fire_power += power_change

        power(fire_power)
        if player_health < 50:
            fire_power = 45           




        gameDisplay.fill(orange, rect=[0, display_height-ground_height, display_width, ground_height])
        pygame.display.update()

        if player_health < 1:
            game_over()
        if enemy_health < 1:
            you_win()



        clock.tick(FPS)
    pygame.quit()
    quit()

def sal():
    gameExit = False
    gameOver = False
    FPS = 60

    player_health = 120
    enemy_health = 190


    barrier_width = 0

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9




    fire_power = 60
    points = 0
    
    power_change = 0



    xlocation = (display_width/2) + random.randint(-0.2*display_width, 0.2*display_width)
    randomHeight = random.randrange(display_height*0.1,display_height*0.6)





    while not gameExit:


        if gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",red,-50,size="large")
            message_to_screen("Press C to play again or Q to exit",black,50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5




                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_z:
                  pygame.image.save(gameDisplay, "bin/assets/screenshots/screenshot.png")



                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_ESCAPE:
                    pause()

                elif event.key == pygame.K_SPACE:
                    damage = fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,randomHeight,enemyTankX,enemyTankY)
                    enemy_health -= damage
                    points +=1

                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange (0,2)

                    for x in range(random.randrange(0,10)):
                        if display_width *0.3 > enemyTankX >display_width *0.03:
                            if possibleMovement [moveIndex] == "f":
                                enemyTankX += 5
                            elif possibleMovement [moveIndex] == "r":
                                enemyTankX -= 5

                            gameDisplay.fill(white)
                            health_bars(player_health,enemy_health)
                            gun = tank(mainTankX,mainTankY,currentTurPos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                            fire_power += power_change



                            clock.tick(FPS)


                    damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,randomHeight,mainTankX,mainTankY)
                    player_health -= damage

                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0





        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0


        if mainTankX - (tankWidth/2) < xlocation:
            mainTankX += 5


        gameDisplay.fill(light_blue)
        health_bars(player_health,enemy_health)
        gun = tank(mainTankX,mainTankY,currentTurPos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        fire_power += power_change

        power(fire_power)
        if player_health < 50:
            fire_power = 51   
        




        gameDisplay.fill(gray, rect=[0, display_height-ground_height, display_width, ground_height])
        pygame.display.update()

        if player_health < 1:
            game_over()
        if enemy_health < 1:
            you_win()



        clock.tick(FPS)
    pygame.quit()
    quit()

def jeb():
    gameExit = False
    gameOver = False
    FPS = 60

    player_health = 120
    enemy_health = 110


    barrier_width = 0

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9




    fire_power = 60
    points = 0
    
    power_change = 0



    xlocation = (display_width/2) + random.randint(-0.2*display_width, 0.2*display_width)
    randomHeight = random.randrange(display_height*0.1,display_height*0.6)





    while not gameExit:


        if gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",red,-50,size="large")
            message_to_screen("Press C to play again or Q to exit",black,50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5




                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_z:
                  pygame.image.save(gameDisplay, "bin/assets/screenshots/screenshot.png")



                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_ESCAPE:
                    pause()

                elif event.key == pygame.K_SPACE:
                    damage = fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,randomHeight,enemyTankX,enemyTankY)
                    enemy_health -= damage
                    points +=1

                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange (0,2)

                    for x in range(random.randrange(0,10)):
                        if display_width *0.3 > enemyTankX >display_width *0.03:
                            if possibleMovement [moveIndex] == "f":
                                enemyTankX += 5
                            elif possibleMovement [moveIndex] == "r":
                                enemyTankX -= 5

                            gameDisplay.fill(white)
                            health_bars(player_health,enemy_health)
                            gun = tank(mainTankX,mainTankY,currentTurPos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                            fire_power += power_change



                            clock.tick(FPS)


                    damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,randomHeight,mainTankX,mainTankY)
                    player_health -= damage

                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0





        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0


        if mainTankX - (tankWidth/2) < xlocation:
            mainTankX += 5


        gameDisplay.fill(light_blue)
        health_bars(player_health,enemy_health)
        gun = tank(mainTankX,mainTankY,currentTurPos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        fire_power += power_change

        power(fire_power)
        if player_health < 56:
            fire_power = 54   
        




        gameDisplay.fill(red, rect=[0, display_height-ground_height, display_width, ground_height])
        pygame.display.update()

        if player_health < 1:
            game_over()
        if enemy_health < 1:
            you_win()



        clock.tick(FPS)
    pygame.quit()
    quit()

def jack():
    gameExit = False
    gameOver = False
    FPS = 60

    player_health = 120
    enemy_health = 110


    barrier_width = 0

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9




    fire_power = 60
    points = 0
    
    power_change = 0
    if player_health < 50:
        fire_power = 53   


    xlocation = (display_width/2) + random.randint(-0.2*display_width, 0.2*display_width)
    randomHeight = random.randrange(display_height*0.1,display_height*0.6)





    while not gameExit:


        if gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",red,-50,size="large")
            message_to_screen("Press C to play again or Q to exit",black,50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5




                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_z:
                  pygame.image.save(gameDisplay, "bin/assets/screenshots/screenshot.png")



                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_ESCAPE:
                    pause()

                elif event.key == pygame.K_SPACE:
                    damage = fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,randomHeight,enemyTankX,enemyTankY)
                    enemy_health -= damage
                    points +=1

                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange (0,2)

                    for x in range(random.randrange(0,10)):
                        if display_width *0.3 > enemyTankX >display_width *0.03:
                            if possibleMovement [moveIndex] == "f":
                                enemyTankX += 5
                            elif possibleMovement [moveIndex] == "r":
                                enemyTankX -= 5

                            gameDisplay.fill(white)
                            health_bars(player_health,enemy_health)
                            gun = tank(mainTankX,mainTankY,currentTurPos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                            fire_power += power_change



                            clock.tick(FPS)


                    damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,randomHeight,mainTankX,mainTankY)
                    player_health -= damage

                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0





        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0


        if mainTankX - (tankWidth/2) < xlocation:
            mainTankX += 5


        gameDisplay.fill(light_blue)
        health_bars(player_health,enemy_health)
        gun = tank(mainTankX,mainTankY,currentTurPos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        fire_power += power_change

        power(fire_power)
        if player_health < 58:
            fire_power = 59   
        




        gameDisplay.fill(gold, rect=[0, display_height-ground_height, display_width, ground_height])
        pygame.display.update()

        if player_health < 1:
            game_over()
        if enemy_health < 1:
            you_win()



        clock.tick(FPS)
    pygame.quit()
    quit()

def jon():
    gameExit = False
    gameOver = False
    FPS = 60

    player_health = 120
    enemy_health = 110


    barrier_width = 0

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9




    fire_power = 60
    points = 0
    
    power_change = 0



    xlocation = (display_width/2) + random.randint(-0.2*display_width, 0.2*display_width)
    randomHeight = random.randrange(display_height*0.1,display_height*0.6)





    while not gameExit:


        if gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",red,-50,size="large")
            message_to_screen("Press C to play again or Q to exit",black,50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5




                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_z:
                  pygame.image.save(gameDisplay, "bin/assets/screenshots/screenshot.png")



                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_ESCAPE:
                    pause()

                elif event.key == pygame.K_SPACE:
                    damage = fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,randomHeight,enemyTankX,enemyTankY)
                    enemy_health -= damage
                    points +=1

                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange (0,2)

                    for x in range(random.randrange(0,10)):
                        if display_width *0.3 > enemyTankX >display_width *0.03:
                            if possibleMovement [moveIndex] == "f":
                                enemyTankX += 5
                            elif possibleMovement [moveIndex] == "r":
                                enemyTankX -= 5

                            gameDisplay.fill(white)
                            health_bars(player_health,enemy_health)
                            gun = tank(mainTankX,mainTankY,currentTurPos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                            fire_power += power_change



                            clock.tick(FPS)


                    damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,randomHeight,mainTankX,mainTankY)
                    player_health -= damage

                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0





        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0


        if mainTankX - (tankWidth/2) < xlocation:
            mainTankX += 5


        gameDisplay.fill(light_blue)
        health_bars(player_health,enemy_health)
        gun = tank(mainTankX,mainTankY,currentTurPos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        fire_power += power_change

        power(fire_power)
        if player_health < 56:
            fire_power = 55   
        




        gameDisplay.fill(brown, rect=[0, display_height-ground_height, display_width, ground_height])
        pygame.display.update()

        if player_health < 1:
            game_over()
        if enemy_health < 1:
            you_win()



        clock.tick(FPS)
    pygame.quit()
    quit()

def ted():
    gameExit = False
    gameOver = False
    FPS = 60

    player_health = 120
    enemy_health = 110


    barrier_width = 0

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9




    fire_power = 60
    points = 0
    
    power_change = 0



    xlocation = (display_width/2) + random.randint(-0.2*display_width, 0.2*display_width)
    randomHeight = random.randrange(display_height*0.1,display_height*0.6)





    while not gameExit:


        if gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",red,-50,size="large")
            message_to_screen("Press C to play again or Q to exit",black,50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5




                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_z:
                  pygame.image.save(gameDisplay, "bin/assets/screenshots/screenshot.png")



                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_ESCAPE:
                    pause()

                elif event.key == pygame.K_SPACE:
                    damage = fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,randomHeight,enemyTankX,enemyTankY)
                    enemy_health -= damage
                    points +=1

                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange (0,2)

                    for x in range(random.randrange(0,10)):
                        if display_width *0.3 > enemyTankX >display_width *0.03:
                            if possibleMovement [moveIndex] == "f":
                                enemyTankX += 5
                            elif possibleMovement [moveIndex] == "r":
                                enemyTankX -= 5

                            gameDisplay.fill(white)
                            health_bars(player_health,enemy_health)
                            gun = tank(mainTankX,mainTankY,currentTurPos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                            fire_power += power_change



                            clock.tick(FPS)


                    damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,randomHeight,mainTankX,mainTankY)
                    player_health -= damage

                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0





        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0


        if mainTankX - (tankWidth/2) < xlocation:
            mainTankX += 5


        gameDisplay.fill(light_blue)
        health_bars(player_health,enemy_health)
        gun = tank(mainTankX,mainTankY,currentTurPos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        fire_power += power_change

        power(fire_power)
        if player_health < 58:
            fire_power = 56           

        




        gameDisplay.fill(brown, rect=[0, display_height-ground_height, display_width, ground_height])
        pygame.display.update()

        if player_health < 1:
            game_over()
        if enemy_health < 1:
            you_win()



        clock.tick(FPS)
    pygame.quit()
    quit()


def joe():
    gameExit = False
    gameOver = False
    FPS = 60

    player_health = 120
    enemy_health = 110


    barrier_width = 0

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9




    fire_power = 60
    points = 0
    
    power_change = 0



    xlocation = (display_width/2) + random.randint(-0.2*display_width, 0.2*display_width)
    randomHeight = random.randrange(display_height*0.1,display_height*0.6)





    while not gameExit:


        if gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",red,-50,size="large")
            message_to_screen("Press C to play again or Q to exit",black,50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5




                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_z:
                  pygame.image.save(gameDisplay, "bin/assets/screenshots/screenshot.png")



                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_ESCAPE:
                    pause()

                elif event.key == pygame.K_SPACE:
                    damage = fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,randomHeight,enemyTankX,enemyTankY)
                    enemy_health -= damage
                    points +=1

                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange (0,2)


                    for x in range(random.randrange(0,10)):
                        if display_width *0.3 > enemyTankX >display_width *0.03:
                            if possibleMovement [moveIndex] == "f":
                                enemyTankX += 5
                            elif possibleMovement [moveIndex] == "r":
                                enemyTankX -= 5

                            gameDisplay.fill(white)
                            health_bars(player_health,enemy_health)
                            gun = tank(mainTankX,mainTankY,currentTurPos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                            fire_power += power_change



                            clock.tick(FPS)


                    damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,randomHeight,mainTankX,mainTankY)
                    player_health -= damage

                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0





        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0


        if mainTankX - (tankWidth/2) < xlocation:
            mainTankX += 5


        gameDisplay.fill(light_blue)
        health_bars(player_health,enemy_health)
        gun = tank(mainTankX,mainTankY,currentTurPos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        fire_power += power_change

        power(fire_power)
        if player_health < 58:
            fire_power = 57   

        




        gameDisplay.fill(gold, rect=[0, display_height-ground_height, display_width, ground_height])
        pygame.display.update()

        if player_health < 1:
            game_over()
        if enemy_health < 1:
            you_win()



        clock.tick(FPS)
    pygame.quit()
    quit()

def bob():
    gameExit = False
    gameOver = False
    FPS = 60

    player_health = 120
    enemy_health = 110


    barrier_width = 0

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9




    fire_power = 60
    points = 0
    
    power_change = 0



    xlocation = (display_width/2) + random.randint(-0.2*display_width, 0.2*display_width)
    randomHeight = random.randrange(display_height*0.1,display_height*0.6)





    while not gameExit:


        if gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",red,-50,size="large")
            message_to_screen("Press C to play again or Q to exit",black,50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5




                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_z:
                  pygame.image.save(gameDisplay, "bin/assets/screenshots/screenshot.png")



                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_ESCAPE:
                    pause()

                elif event.key == pygame.K_SPACE:
                    damage = fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,randomHeight,enemyTankX,enemyTankY)
                    enemy_health -= damage
                    points +=1

                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange (0,2)

                    for x in range(random.randrange(0,10)):
                        if display_width *0.3 > enemyTankX >display_width *0.03:
                            if possibleMovement [moveIndex] == "f":
                                enemyTankX += 5
                            elif possibleMovement [moveIndex] == "r":
                                enemyTankX -= 5

                            gameDisplay.fill(white)
                            health_bars(player_health,enemy_health)
                            gun = tank(mainTankX,mainTankY,currentTurPos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                            fire_power += power_change



                            clock.tick(FPS)


                    damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,randomHeight,mainTankX,mainTankY)
                    player_health -= damage

                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0





        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0


        if mainTankX - (tankWidth/2) < xlocation:
            mainTankX += 5


        gameDisplay.fill(light_blue)
        health_bars(player_health,enemy_health)
        gun = tank(mainTankX,mainTankY,currentTurPos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        fire_power += power_change

        power(fire_power)
        if player_health < 58:
            fire_power = 59   
        




        gameDisplay.fill(light_green, rect=[0, display_height-ground_height, display_width, ground_height])
        pygame.display.update()

        if player_health < 1:
            game_over()
        if enemy_health < 1:
            you_win()



        clock.tick(FPS)
    pygame.quit()
    quit()

def time():
    gameExit = False
    gameOver = False
    FPS = 60

    player_health = 120
    enemy_health = 110


    barrier_width = 0

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9




    fire_power = 60
    points = 0
    
    power_change = 0



    xlocation = (display_width/2) + random.randint(-0.2*display_width, 0.2*display_width)
    randomHeight = random.randrange(display_height*0.1,display_height*0.6)





    while not gameExit:


        if gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",red,-50,size="large")
            message_to_screen("Press C to play again or Q to exit",black,50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5




                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_z:
                  pygame.image.save(gameDisplay, "bin/assets/screenshots/screenshot.png")



                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_ESCAPE:
                    pause()

                elif event.key == pygame.K_SPACE:
                    damage = fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,randomHeight,enemyTankX,enemyTankY)
                    enemy_health -= damage
                    points +=1

                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange (0,2)

                    for x in range(random.randrange(0,10)):
                        if display_width *0.3 > enemyTankX >display_width *0.03:
                            if possibleMovement [moveIndex] == "f":
                                enemyTankX += 5
                            elif possibleMovement [moveIndex] == "r":
                                enemyTankX -= 5

                            gameDisplay.fill(white)
                            health_bars(player_health,enemy_health)
                            gun = tank(mainTankX,mainTankY,currentTurPos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                            fire_power += power_change



                            clock.tick(FPS)


                    damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,randomHeight,mainTankX,mainTankY)
                    player_health -= damage

                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0





        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0


        if mainTankX - (tankWidth/2) < xlocation:
            mainTankX += 5


        gameDisplay.fill(light_blue)
        health_bars(player_health,enemy_health)
        gun = tank(mainTankX,mainTankY,currentTurPos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        fire_power += power_change

        power(fire_power)
        
        if player_health < 65:
            fire_power = 60  
        




        gameDisplay.fill(light_green, rect=[0, display_height-ground_height, display_width, ground_height])
        pygame.display.update()

        if player_health < 1:
            game_over()
        if enemy_health < 1:
            you_win()



        clock.tick(FPS)
    pygame.quit()
    quit()

def next():
    gameExit = False
    gameOver = False
    FPS = 60

    player_health = 120
    enemy_health = 110


    barrier_width = 0

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9




    fire_power = 60
    points = 0
    
    power_change = 0



    xlocation = (display_width/2) + random.randint(-0.2*display_width, 0.2*display_width)
    randomHeight = random.randrange(display_height*0.1,display_height*0.6)





    while not gameExit:


        if gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",red,-50,size="large")
            message_to_screen("Press C to play again or Q to exit",black,50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5




                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_z:
                  pygame.image.save(gameDisplay, "bin/assets/screenshots/screenshot.png")



                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_ESCAPE:
                    pause()

                elif event.key == pygame.K_SPACE:
                    damage = fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,randomHeight,enemyTankX,enemyTankY)
                    enemy_health -= damage
                    points +=1

                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange (0,2)

                    for x in range(random.randrange(0,10)):
                        if display_width *0.3 > enemyTankX >display_width *0.03:
                            if possibleMovement [moveIndex] == "f":
                                enemyTankX += 5
                            elif possibleMovement [moveIndex] == "r":
                                enemyTankX -= 5

                            gameDisplay.fill(white)
                            health_bars(player_health,enemy_health)
                            gun = tank(mainTankX,mainTankY,currentTurPos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                            fire_power += power_change



                            clock.tick(FPS)


                    damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,randomHeight,mainTankX,mainTankY)
                    player_health -= damage

                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0





        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0


        if mainTankX - (tankWidth/2) < xlocation:
            mainTankX += 5


        gameDisplay.fill(light_blue)
        health_bars(player_health,enemy_health)
        gun = tank(mainTankX,mainTankY,currentTurPos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        fire_power += power_change

        power(fire_power)
   
        if player_health < 68:
            fire_power = 62          




        gameDisplay.fill(dark_gray, rect=[0, display_height-ground_height, display_width, ground_height])
        pygame.display.update()

        if player_health < 1:
            game_over()
        if enemy_health < 1:
            you_win()



        clock.tick(FPS)
    pygame.quit()
    quit()

def level():
    gameExit = False
    gameOver = False
    FPS = 60

    player_health = 120
    enemy_health = 110


    barrier_width = 0

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9




    fire_power = 60
    points = 0
    
    power_change = 0



    xlocation = (display_width/2) + random.randint(-0.2*display_width, 0.2*display_width)
    randomHeight = random.randrange(display_height*0.1,display_height*0.6)





    while not gameExit:


        if gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",red,-50,size="large")
            message_to_screen("Press C to play again or Q to exit",black,50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5




                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_z:
                  pygame.image.save(gameDisplay, "bin/assets/screenshots/screenshot.png")



                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_ESCAPE:
                    pause()

                elif event.key == pygame.K_SPACE:
                    damage = fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,randomHeight,enemyTankX,enemyTankY)
                    enemy_health -= damage
                    points +=1

                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange (0,2)

                    for x in range(random.randrange(0,10)):
                        if display_width *0.3 > enemyTankX >display_width *0.03:
                            if possibleMovement [moveIndex] == "f":
                                enemyTankX += 5
                            elif possibleMovement [moveIndex] == "r":
                                enemyTankX -= 5

                            gameDisplay.fill(white)
                            health_bars(player_health,enemy_health)
                            gun = tank(mainTankX,mainTankY,currentTurPos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                            fire_power += power_change



                            clock.tick(FPS)


                    damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,randomHeight,mainTankX,mainTankY)
                    player_health -= damage

                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0





        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0


        if mainTankX - (tankWidth/2) < xlocation:
            mainTankX += 5


        gameDisplay.fill(light_blue)
        health_bars(player_health,enemy_health)
        gun = tank(mainTankX,mainTankY,currentTurPos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        fire_power += power_change

        power(fire_power)
        
        if player_health < 70:
            fire_power = 64       




        gameDisplay.fill(dark_green, rect=[0, display_height-ground_height, display_width, ground_height])
        pygame.display.update()

        if player_health < 1:
            game_over()
        if enemy_health < 1:
            you_win()



        clock.tick(FPS)
    pygame.quit()
    quit()



def level2():
    gameExit = False
    gameOver = False
    FPS = 60

    player_health = 120
    enemy_health = 110


    barrier_width = 0

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9




    fire_power = 60
    points = 0
    
    power_change = 0



    xlocation = (display_width/2) + random.randint(-0.2*display_width, 0.2*display_width)
    randomHeight = random.randrange(display_height*0.1,display_height*0.6)





    while not gameExit:


        if gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",red,-50,size="large")
            message_to_screen("Press C to play again or Q to exit",black,50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5




                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_z:
                  pygame.image.save(gameDisplay, "bin/assets/screenshots/screenshot.png")



                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_ESCAPE:
                    pause()

                elif event.key == pygame.K_SPACE:
                    damage = fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,randomHeight,enemyTankX,enemyTankY)
                    enemy_health -= damage
                    

                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange (0,2)

                    for x in range(random.randrange(0,10)):
                        if display_width *0.3 > enemyTankX >display_width *0.03:
                            if possibleMovement [moveIndex] == "f":
                                enemyTankX += 5
                            elif possibleMovement [moveIndex] == "r":
                                enemyTankX -= 5

                            gameDisplay.fill(white)
                            health_bars(player_health,enemy_health)
                            gun = tank(mainTankX,mainTankY,currentTurPos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                            fire_power += power_change



                            clock.tick(FPS)


                    damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,randomHeight,mainTankX,mainTankY)
                    player_health -= damage

                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0





        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0


        if mainTankX - (tankWidth/2) < xlocation:
            mainTankX += 5
            
        gameDisplay.fill(light_blue)
        health_bars(player_health,enemy_health)
        gun = tank(mainTankX,mainTankY,currentTurPos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        fire_power += power_change

        power(fire_power)
        
        if player_health < 70:
            fire_power = 65
        

        gameDisplay.fill(gray, rect=[0, display_height-ground_height, display_width, ground_height])
        pygame.display.update()

        if player_health < 1:
            game_over()
        if enemy_health < 1:
            you_win()



        clock.tick(FPS)
    pygame.quit()
    quit()

def chapter():
    gameExit = False
    gameOver = False
    FPS = 60

    player_health = 120
    enemy_health = 110


    barrier_width = 0

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9




    fire_power = 60
    points = 0
    
    power_change = 0
    


    xlocation = (display_width/2) + random.randint(-0.2*display_width, 0.2*display_width)
    randomHeight = random.randrange(display_height*0.1,display_height*0.6)





    while not gameExit:


        if gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over",red,-50,size="large")
            message_to_screen("Press C to play again or Q to exit",black,50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5




                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_z:
                  pygame.image.save(gameDisplay, "bin/assets/screenshots/screenshot.png")



                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_ESCAPE:
                    pause()

                elif event.key == pygame.K_SPACE:
                    damage = fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,randomHeight,enemyTankX,enemyTankY)
                    enemy_health -= damage
                    points +=1

                    possibleMovement = ['f', 'r']
                    moveIndex = random.randrange (0,2)

                    for x in range(random.randrange(0,10)):
                        if display_width *0.3 > enemyTankX >display_width *0.03:
                            if possibleMovement [moveIndex] == "f":
                                enemyTankX += 5
                            elif possibleMovement [moveIndex] == "r":
                                enemyTankX -= 5

                            gameDisplay.fill(white)
                            health_bars(player_health,enemy_health)
                            gun = tank(mainTankX,mainTankY,currentTurPos)
                            enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
                            fire_power += power_change



                            clock.tick(FPS)


                    damage = e_fireShell(enemy_gun,enemyTankX,enemyTankY,8,50,xlocation,randomHeight,mainTankX,mainTankY)
                    player_health -= damage

                elif event.key == pygame.K_a:
                    power_change = -1
                elif event.key == pygame.K_d:
                    power_change = 1



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0





        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0
        
        
        if mainTankX - (tankWidth/2) < xlocation:
            mainTankX += 5
        

            
        gameDisplay.fill(light_blue)
        health_bars(player_health,enemy_health)
        gun = tank(mainTankX,mainTankY,currentTurPos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        fire_power += power_change

        power(fire_power)
        
        if player_health < 76:
            fire_power = 70
            

         

        gameDisplay.fill(dark_green, rect=[0, display_height-ground_height, display_width, ground_height])
        pygame.display.update()

        if player_health < 1:
            game_over()
        if enemy_health < 1:
            you_win()
        clock.tick(FPS)
text_file.write("1 Bug found...asset file missing!!!\n")
text_file.write("asset file is being ignored\n")
text_file.write("Shadows of war Developers build 1.19.0(DEV 1.20.0)...\n")

text_file.write("All jokes aside that's a bug\n")
text_file.write("line count: 4139\n")
text_file.write("End log...\n")
text_file.close()   
game_intro()
chapter() 
pygame.quit()
quit()
