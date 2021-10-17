import pygame
pygame.init()
pygame.font.init()

#Setting Up Window
WIDTH, HEIGHT = 800, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Library Dash")
background = pygame.transform.scale(pygame.image.load('dcatbackground.png'), (WIDTH,HEIGHT))

#Font Stuff
font = pygame.font.SysFont('Courier New', 20)
WHITE = (255,255,255)
BLACK = (0,0,0)

#Miscellaneous Stuff
FPS = 120
VELOCITY = 15

#Width and Height of characters
BS_WIDTH, BS_HEIGHT = 80,80

###############################
#LEVEL ONE

#Miscellaneous
POS_X, POS_Y = 45, 400
PEN_VELOCITY = 50
P_WIDTH, P_HEIGHT =  20, 10
PEN_X, PEN_Y = 85, 430
pens = []

#Miscellaneous pt2
left = False
right = False
isJump = False
jumpCount = 10
walkCount = 0

#Platforms

#Images and stuff
library = pygame.transform.scale(pygame.image.load('bookshelves.png'), (WIDTH, HEIGHT))

#Sprite Animation stuff
def sprite_movement(character, walkLeft, walkRight):
  global walkCount

  if walkCount + 1 >= 4:
    walkCount = 0

  if left:
    WINDOW.blit(walkLeft[walkCount//2], (POS_X, POS_Y))
    walkCount += 1
  elif right:
    WINDOW.blit(walkRight[walkCount//2], (POS_X, POS_Y))
    walkCount += 1
  else:
    WINDOW.blit(character, (POS_X, POS_Y))

#Put things on the screen
def draw_level_one(character, walkRight, walkLeft):
  WINDOW.blit(library, (0,0))
  sprite_movement(character, walkLeft, walkRight)
  pygame.display.update()

#Loop
def level_one(walkRight, character,walkLeft):
  global POS_X, POS_Y, isJump, jumpCount, walkCount, left, right
  run = True
  clock = pygame.time.Clock()
  while run:
    clock.tick(FPS)

    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
        run = False 
        pygame.quit()

    keys = pygame.key.get_pressed()  

    if keys[pygame.K_LEFT] and (POS_X > VELOCITY): 
        POS_X -= VELOCITY
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and (POS_X < WIDTH - VELOCITY - BS_WIDTH):  
        POS_X += VELOCITY 
        right = True
        left = False

    else:
      left = False
      right = False
      walkCount = 0

    if not (isJump):
      if keys[pygame.K_UP]:
        isJump = True
        left = False
        right = False
        walkCount = 0
    else:
      if jumpCount >= -10:
        neg = 1
        if jumpCount < 0:
          neg = -1
        POS_Y -= (jumpCount ** 2)*0.5*neg
        jumpCount -= 1
      else:
        isJump = False
        jumpCount = 10

    draw_level_one(character, walkRight, walkLeft)
  main_menu()


###############################
#CHOOSE YOUR CHARACTER MENU

#Loading images
IMAGE_WIDTH, IMAGE_HEIGHT = 128,128
WHITE_WIDTH, WHITE_HEIGHT = 175, 250
ybs = pygame.transform.scale(pygame.image.load('yellowbookstand.png'), (IMAGE_WIDTH, IMAGE_HEIGHT))
rbs = pygame.transform.scale(pygame.image.load('redbookstand.png'), (IMAGE_WIDTH, IMAGE_HEIGHT))
bbs = pygame.transform.scale(pygame.image.load('bluebookstand.png'), (IMAGE_WIDTH, IMAGE_HEIGHT))
whitebox = pygame.transform.scale(pygame.image.load('whitebox.png'), (WHITE_WIDTH, WHITE_HEIGHT))
CHOOSE_WIDTH, CHOOSE_HEIGHT  = 100, 40
choose = pygame.transform.scale(pygame.image.load('choose.png'), (CHOOSE_WIDTH, CHOOSE_HEIGHT))
textchoose = pygame.transform.scale(pygame.image.load('textcharacter.png'), (600, 65))

#Miscellaneous
yellow_rest_x =  60
red_rest_x = WIDTH//2 - IMAGE_WIDTH//2
blue_rest_x = WIDTH - IMAGE_WIDTH - 60
yellow_rest_y = HEIGHT//2-IMAGE_HEIGHT//2-50
red_rest_y = HEIGHT//2-IMAGE_HEIGHT//2-50
blue_rest_y = HEIGHT//2-IMAGE_HEIGHT//2-50

#Whitebox positions
whitebox_x_1 = 37
whitebox_x_2 = 311
whitebox_x_3 = 588

#Choosebox positions
choosebox_x_1 = 75
choosebox_x_2 = 350
choosebox_x_3 = 627
choosebox_y = 390

#Font stuff
font_for_names = pygame.font.SysFont('Courier New', 20)
font_for_descs = pygame.font.SysFont('Garamond', 20)

#Yellow Information
nameY = "Name: Yellow"
fnameY = font_for_names.render(nameY, 1, BLACK)
descY = ["Yellow likes to", "go to the beach and", "spend time with its", "human."]
def print_yellow_desc():
  desc_pos_y = 305
  for sentence in descY:
    desc_pos_y += 7
    fsentence = font_for_descs.render(sentence,1, BLACK)
    WINDOW.blit(fsentence,(65,desc_pos_y))
    desc_pos_y = desc_pos_y + 7

  
#Red Information
nameR = "Name: Red"
fnameR = font_for_names.render(nameR, 1, BLACK)
descR = ["Red gets angry", "when you leave its", "spine bent in half."]
def print_red_desc():
  desc_pos_y = 305
  for sentence in descR:
    desc_pos_y += 7
    fsentence = font_for_descs.render(sentence,1, BLACK)
    WINDOW.blit(fsentence,(340,desc_pos_y))
    desc_pos_y = desc_pos_y + 7

#Blue Information
nameB = "Name: Blue"
fnameB = font_for_names.render(nameB, 1, BLACK)
descB = ["Blue enjoys sitting", "on the coffee table", "with your magazines."]
def print_blue_desc():
  desc_pos_y = 305
  for sentence in descB:
    desc_pos_y += 7
    fsentence = font_for_descs.render(sentence,1, BLACK)
    WINDOW.blit(fsentence,(619,desc_pos_y))
    desc_pos_y = desc_pos_y + 7


#Buttons for chooseboxs
choosebox1 = pygame.Rect(choosebox_x_1, choosebox_y, CHOOSE_WIDTH, CHOOSE_HEIGHT)
choosebox2 = pygame.Rect(choosebox_x_2, choosebox_y, CHOOSE_WIDTH, CHOOSE_HEIGHT)
choosebox3 = pygame.Rect(choosebox_x_3, choosebox_y, CHOOSE_WIDTH, CHOOSE_HEIGHT)

#Choose the yellow character
def choose_yellow():
  #Animations for moving right
  walkRight = [pygame.transform.scale(pygame.image.load('ybw.png'),(BS_WIDTH, BS_HEIGHT)), pygame.transform.scale(pygame.image.load('ybs.png'),(BS_WIDTH, BS_HEIGHT))]
  #Animations for moving left
  walkLeft = [pygame.transform.flip(pygame.transform.scale(pygame.image.load('ybw.png'),(BS_WIDTH, BS_HEIGHT)), True, False), pygame.transform.flip(pygame.transform.scale(pygame.image.load('ybs.png'),(BS_WIDTH, BS_HEIGHT)), True, False)]
  #Regular Standing
  character = pygame.transform.scale(pygame.image.load('ybs.png'),(BS_WIDTH, BS_HEIGHT))
  #Move to level one
  level_one(walkRight, character, walkLeft)

#Choose the red character
def choose_red():
  #Animations for moving right
  walkRight = [pygame.transform.scale(pygame.image.load('rbw.png'),(BS_WIDTH, BS_HEIGHT)), pygame.transform.scale(pygame.image.load('rbs.png'),(BS_WIDTH, BS_HEIGHT))]
  #Animations for moving left
  walkLeft = [pygame.transform.flip(pygame.transform.scale(pygame.image.load('rbw.png'),(BS_WIDTH, BS_HEIGHT)), True, False), pygame.transform.flip(pygame.transform.scale(pygame.image.load('rbs.png'),(BS_WIDTH, BS_HEIGHT)), True, False)]
  #Regular Standing
  character = pygame.transform.scale(pygame.image.load('rbs.png'),(BS_WIDTH, BS_HEIGHT))
  #Move to level one
  level_one(walkRight, character, walkLeft)

#Choose the blue character
def choose_blue():
  #Animations for moving right
  walkRight = [pygame.transform.scale(pygame.image.load('bbw.png'),(BS_WIDTH, BS_HEIGHT)), pygame.transform.scale(pygame.image.load('bbs.png'),(BS_WIDTH, BS_HEIGHT))]
  #Animations for moving left
  walkLeft = [pygame.transform.flip(pygame.transform.scale(pygame.image.load('bbw.png'),(BS_WIDTH, BS_HEIGHT)), True, False), pygame.transform.flip(pygame.transform.scale(pygame.image.load('bbs.png'),(BS_WIDTH, BS_HEIGHT)), True, False)]
  #Regular Standing
  character = pygame.transform.scale(pygame.image.load('bbs.png'),(BS_WIDTH, BS_HEIGHT))
  #Move to level one
  level_one(walkRight, character, walkLeft)

#Put things onto the screen
def draw_game_menu(yellow_rest_x, red_rest_x, blue_rest_x, yellow_rest_y, red_rest_y, blue_rest_y):
  WINDOW.fill(BLACK)
  WINDOW.blit(textchoose, (WIDTH//2 - 300, 40))
  #Yellow box
  WINDOW.blit(whitebox, (whitebox_x_1, 200))
  pygame.draw.rect(WINDOW, (0,0,0), choosebox1)
  WINDOW.blit(choose, (75,390))
  WINDOW.blit(fnameY, (55,280))
  print_yellow_desc()
  #Red box
  WINDOW.blit(whitebox, (whitebox_x_2, 200))
  pygame.draw.rect(WINDOW, (0,0,0), choosebox2)
  WINDOW.blit(choose, (350,390))
  WINDOW.blit(fnameR, (330,280))
  print_red_desc()
  #Blue box
  WINDOW.blit(whitebox, (whitebox_x_3, 200))
  pygame.draw.rect(WINDOW, (0,0,0), choosebox3)
  WINDOW.blit(choose, (627,390))
  WINDOW.blit(fnameB, (607,280))
  print_blue_desc()
  #Other stuff
  WINDOW.blit(ybs, (yellow_rest_x, yellow_rest_y))
  WINDOW.blit(rbs, (red_rest_x,red_rest_y))
  WINDOW.blit(bbs, (blue_rest_x,blue_rest_y))
  pygame.display.update()

def game_menu():
  run = True
  clock = pygame.time.Clock()
  click = False
  while run:
    clock.tick(FPS)
    mx, my = pygame.mouse.get_pos()
    if choosebox1.collidepoint((mx,my)):
      if click:
        choose_yellow()
    elif choosebox2.collidepoint((mx,my)):
      if click:
        choose_red()
    elif choosebox3.collidepoint((mx,my)):
      if click:
        choose_blue()
    click = False
      

    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
        run = False 
        pygame.quit()
      
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button  == 1:
          click = True
      
      

    draw_game_menu(yellow_rest_x, red_rest_x, blue_rest_x,yellow_rest_y, red_rest_y, blue_rest_y)
  main_menu()

###############################
#INTRO MENU

#Loading Images & Related
box_WIDTH, box_HEIGHT = 600,150
textbox = pygame.transform.scale(pygame.image.load('textbox.png'),(box_WIDTH,box_HEIGHT))
box_X, box_Y = WIDTH//2-box_WIDTH//2,300
cat_width, cat_height = 224,224
wcat = pygame.transform.scale(pygame.image.load('wdiversitycat.png'), (cat_width, cat_height))
rcat = pygame.transform.scale(pygame.image.load('diversitycat.png'), (cat_width, cat_height))
mission = pygame.transform.scale(pygame.image.load('mission.png'), (cat_width, cat_height))
wevilflying = pygame.transform.scale(pygame.image.load('wevilflying.png'), (cat_width, cat_height))
wpen = pygame.transform.scale(pygame.image.load('wpen.png'), (cat_width//2, cat_height//2))
examplebook = pygame.transform.scale(pygame.image.load('examplebook.png'), (192,192))

#Button surrounding textbox
box_w, box_h = box_WIDTH, box_HEIGHT
box_x, box_y = box_X, box_Y


#Messages
#1
def display_message_one(backbox):
  WINDOW.fill((0,0,0))
  WINDOW.blit(wcat, (WIDTH//2 - cat_width//2, 80))
  pygame.draw.rect(WINDOW, (WHITE), backbox)
  WINDOW.blit(textbox,(box_X, box_Y))
  message_one = "Welcome to the library..."
  starting_pos =  130
  msg = font.render(message_one, 1, WHITE)
  WINDOW.blit(msg, (starting_pos, 325))
  pygame.display.update()


#2
def display_message_two(backbox):
  WINDOW.fill((0,0,0))
  WINDOW.blit(wcat, (WIDTH//3 - cat_width//2, 80))
  WINDOW.blit(mission, (WIDTH - WIDTH//3 - cat_width//2, 80))
  pygame.draw.rect(WINDOW, (WHITE), backbox)
  WINDOW.blit(textbox,(box_X, box_Y))
  message_two = ["Your mission, should you choose to accept", "it, is to rid your library from the clutches", "of evil books..."]
  starting_pos = 130
  word_pos = 0
  for sentence in message_two:
    msg = font.render(sentence, 1, WHITE)
    word_pos += 15
    WINDOW.blit(msg, (starting_pos, 310 + word_pos))
    word_pos = word_pos + 15
  pygame.display.update()

#3
def display_message_three(backbox):
  WINDOW.fill((0,0,0))
  WINDOW.blit(wevilflying, (WIDTH//2 - cat_width//2, 80))
  pygame.draw.rect(WINDOW, (WHITE), backbox)
  WINDOW.blit(textbox,(box_X, box_Y))
  message_three =  ["Evil books are books written by old dead", "white men, and they plague your library", "with a lack of diversity..."]
  starting_pos = 130
  word_pos = 0
  for sentence in message_three:
    msg = font.render(sentence, 1, WHITE)
    word_pos += 15
    WINDOW.blit(msg, (starting_pos, 310 + word_pos))
    word_pos = word_pos + 15
  pygame.display.update()

#4
def display_message_four(backbox):
  WINDOW.fill((0,0,0))
  WINDOW.blit(examplebook, (WIDTH//3 - cat_width//2, 90))
  WINDOW.blit(wpen, (WIDTH//2 - 70, 125))
  WINDOW.blit(wevilflying, (WIDTH - WIDTH//3 - cat_width//2, 80))
  pygame.draw.rect(WINDOW, (WHITE), backbox)
  WINDOW.blit(textbox,(box_X, box_Y))
  message_four = ["Shoot pens at the evil books to kill them", ",and collect as many diversity stars ", "as possible to unlock new good books.."]
  starting_pos = 130
  word_pos = 0
  for sentence in message_four:
    msg = font.render(sentence, 1, WHITE)
    word_pos += 15
    WINDOW.blit(msg, (starting_pos, 310 + word_pos))
    word_pos = word_pos + 15
  pygame.display.update()

#5
def display_message_five(backbox):
  WINDOW.fill((0,0,0))
  WINDOW.blit(wcat, (WIDTH//2 - cat_width//2, 80))
  pygame.draw.rect(WINDOW, (WHITE), backbox)
  WINDOW.blit(textbox,(box_X, box_Y))
  message_five = "Now, it's time to choose your first book..."
  starting_pos = 130
  msg = font.render(message_five, 1, WHITE)
  WINDOW.blit(msg, (starting_pos, 325))
  pygame.display.update()

#Clear the screen and show textbox again
def clear_message(backbox):
  WINDOW.fill((0,0,0))
  pygame.draw.rect(WINDOW, (WHITE), backbox)
  WINDOW.blit(textbox,(box_X, box_Y))
  pygame.display.update()

#Main Intro Loop
def intro_menu():
  run = True
  clock = pygame.time.Clock()
  backbox = pygame.Rect(box_x, box_y, box_w, box_h)
  display_message_one(backbox)
  click = False
  while run:
    clock.tick(FPS)
    mx, my = pygame.mouse.get_pos()
    if backbox.collidepoint((mx,my)):
      if click:
        clear_message(backbox)
        intro_two_menu()

    click = False

    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
        run = False 
        pygame.quit()

      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button  == 1:
          click = True


#Second Intro Loop
def intro_two_menu():
  run = True
  clock = pygame.time.Clock()
  backbox = pygame.Rect(box_x, box_y, box_w, box_h)
  click = False
  display_message_two(backbox)
  while run:
    clock.tick(FPS)
    mx, my = pygame.mouse.get_pos()
    if backbox.collidepoint((mx,my)):
      if click:
        clear_message(backbox)
        intro_three_menu()

    click = False

    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
        run = False 
        pygame.quit()

      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button  == 1:
          click = True

#Third Intro Loop
def intro_three_menu():
  run = True
  clock = pygame.time.Clock()
  backbox = pygame.Rect(box_x, box_y, box_w, box_h)
  click = False
  display_message_three(backbox)
  while run:
    clock.tick(FPS)
    mx, my = pygame.mouse.get_pos()
    if backbox.collidepoint((mx,my)):
      if click:
        clear_message(backbox)
        intro_four_menu()

    click = False

    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
        run = False 
        pygame.quit()

      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button  == 1:
          click = True

#Fourth Intro Loop
def intro_four_menu():
  run = True
  clock = pygame.time.Clock()
  backbox = pygame.Rect(box_x, box_y, box_w, box_h)
  click = False
  display_message_four(backbox)
  while run:
    clock.tick(FPS)
    mx, my = pygame.mouse.get_pos()
    if backbox.collidepoint((mx,my)):
      if click:
        clear_message(backbox)
        intro_fifth_menu()

    click = False

    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
        run = False 
        pygame.quit()

      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button  == 1:
          click = True

#Fifth Intro Loop
def intro_fifth_menu():
  run = True
  clock = pygame.time.Clock()
  backbox = pygame.Rect(box_x, box_y, box_w, box_h)
  click = False
  display_message_five(backbox)
  while run:
    clock.tick(FPS)
    mx, my = pygame.mouse.get_pos()
    if backbox.collidepoint((mx,my)):
      if click:
        game_menu()

    click = False

    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
        run = False 
        pygame.quit()

      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button  == 1:
          click = True
          
###############################
#MAIN MENU 

#Button stuff
button_width, button_height = 120,40
button_x, button_y = WIDTH//2 - button_width//2, HEIGHT//3 + button_height*2.5
start = pygame.transform.scale(pygame.image.load('start.png'), (button_width, button_height))

#Loading images
darktitle_Width , darktitle_Height = 500, 100
darktitle = pygame.transform.scale(pygame.image.load('propertitle.png'),(darktitle_Width, darktitle_Height))


#Put stuff on screen
def draw_window(button_x, button_y, clickStart):
  WINDOW.blit(background, (0,0))
  WINDOW.blit(darktitle, (WIDTH//2-darktitle_Width//2 ,HEIGHT//3 - darktitle_Height//3 + 30))
  pygame.draw.rect(WINDOW, (0,0,0), clickStart)
  WINDOW.blit(start, (button_x, button_y))
  pygame.display.update()

#Loop
def main_menu():
  run = True
  clock = pygame.time.Clock()
  clickStart = pygame.Rect(button_x,button_y,button_width, button_height)
  click = False
  while run:
    clock.tick(FPS)
    mx, my = pygame.mouse.get_pos()
    if clickStart.collidepoint((mx,my)):
      if click:
        intro_menu()

    click = False

    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
        run = False 
        pygame.quit()

      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button  == 1:
          click = True

    draw_window(button_x, button_y, clickStart)
  main_menu()

if __name__ == "__main__":
  main_menu()


