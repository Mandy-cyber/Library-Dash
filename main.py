import pygame
import random
pygame.init()
pygame.font.init()
pygame.mixer.init()

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
FPS = 60
VELOCITY = 5

#Width and Height of characters
BS_WIDTH, BS_HEIGHT = 80,80

###############################
#MAIN GAME

#Miscellaneous
POS_X, POS_Y = 45, 400

#Miscellaneous pt2
isJump = False
jumpCount = 10
stepIndex = 0

#Images and stuff
library = pygame.transform.scale(pygame.image.load('bookshelves.png'), (WIDTH, HEIGHT))

#Generating Enemies Stuff
EB_WIDTH, EB_HEIGHT = 100,100
evilbook = pygame.transform.scale(pygame.image.load('evilflying.png'), (EB_WIDTH, EB_HEIGHT))
evil_books = []
SPAWNENEMY = pygame.USEREVENT
pygame.time.set_timer(SPAWNENEMY, 3500)

def create_enemy(): #create the enemy
  added_heights = [0, 10, 40]
  addH = random.choice(added_heights)
  new_evil_book = evilbook.get_rect(midtop = (WIDTH, POS_Y-addH))
  return new_evil_book

def move_enemy(enemies): #move the enemy
  for enemy in enemies:
    enemy.centerx -= 10
  return enemies

def draw_enemy(enemies): #draw the enemy
  for enemy in enemies:
    WINDOW.blit(evilbook, enemy)
    #Generate hitbox for enemies
    e_hitbox_radius = EB_WIDTH // 2
    pygame.draw.circle(WINDOW, WHITE, (enemy.x + 50, enemy.y + 50), e_hitbox_radius, 2)


#Make book look like it is running
def moving_book(walkRight, character, stepIndex):
  character = walkRight[stepIndex//4]
  WINDOW.blit(character, (POS_X, POS_Y))

#Generate hitbox for character
def character_hitbox(character):
  c_hitbox_radius = BS_WIDTH // 2
  pygame.draw.circle(WINDOW, WHITE, (POS_X + 40, POS_Y + 40), c_hitbox_radius, 2)

#Something for moving background
i = 0

#Put things on the screen
def draw_main_game(character, walkRight, stepIndex):
  WINDOW.blit(library, (i,0))
  WINDOW.blit(library, (WIDTH + i, 0))
  moving_book(walkRight, character, stepIndex)
  character_hitbox(character)
  draw_enemy(evil_books)
  pygame.display.update()


#Loop
def main_game(walkRight, character, stepIndex):
  global POS_X, POS_Y, isJump, jumpCount, walkCount, i, evil_books
  run = True
  clock = pygame.time.Clock()
  while run:
    clock.tick(FPS)

    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
        run = False 
        pygame.quit()
      
      if event.type == SPAWNENEMY:
        evil_books.append(create_enemy())

    evil_books = move_enemy(evil_books)
    draw_enemy(evil_books)

    keys = pygame.key.get_pressed()    

    if not (isJump):
      if keys[pygame.K_UP]:
        isJump = True
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

    if i == -WIDTH:
      WINDOW.blit(library, (WIDTH + i, 0))
      i = 0


    draw_main_game(character, walkRight, stepIndex)
    i -= 8
    stepIndex += 1
    if stepIndex >= 5:
      stepIndex = 0
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
#whitebox_x_1 = 37
#whitebox_x_2 = 311
#whitebox_x_3 = 588

#Choosebox positions
choosebox_x_1 = 75
choosebox_x_2 = 350
choosebox_x_3 = 627
choosebox_y = 390

#Font stuff
font_for_names = pygame.font.SysFont('Courier New', 20)
font_for_descs = pygame.font.SysFont('Garamond', 20)

#Buttons for chooseboxs
choosebox1 = pygame.Rect(choosebox_x_1, choosebox_y, CHOOSE_WIDTH, CHOOSE_HEIGHT)
choosebox2 = pygame.Rect(choosebox_x_2, choosebox_y, CHOOSE_WIDTH, CHOOSE_HEIGHT)
choosebox3 = pygame.Rect(choosebox_x_3, choosebox_y, CHOOSE_WIDTH, CHOOSE_HEIGHT)

#Choose the yellow character
def choose_yellow():
  #Animations for moving right
  walkRight = [pygame.transform.scale(pygame.image.load('ybw.png'),(BS_WIDTH, BS_HEIGHT)), pygame.transform.scale(pygame.image.load('ybs.png'),(BS_WIDTH, BS_HEIGHT))]
  #Regular Standing
  character = pygame.transform.scale(pygame.image.load('ybs.png'),(BS_WIDTH, BS_HEIGHT))
  #Move to level one
  main_game(walkRight, character, stepIndex)

#Choose the red character
def choose_red():
  #Animations for moving right
  walkRight = [pygame.transform.scale(pygame.image.load('rbw.png'),(BS_WIDTH, BS_HEIGHT)), pygame.transform.scale(pygame.image.load('rbs.png'),(BS_WIDTH, BS_HEIGHT))]
  #Regular Standing
  character = pygame.transform.scale(pygame.image.load('rbs.png'),(BS_WIDTH, BS_HEIGHT))
  #Move to level one
  main_game(walkRight, character, stepIndex)

#Choose the blue character
def choose_blue():
  #Animations for moving right
  walkRight = [pygame.transform.scale(pygame.image.load('bbw.png'),(BS_WIDTH, BS_HEIGHT)), pygame.transform.scale(pygame.image.load('bbs.png'),(BS_WIDTH, BS_HEIGHT))]
  #Regular Standing
  character = pygame.transform.scale(pygame.image.load('bbs.png'),(BS_WIDTH, BS_HEIGHT))
  #Move to level one
  main_game(walkRight, character, stepIndex)

#Put things onto the screen
def draw_game_menu(yellow_rest_x, red_rest_x, blue_rest_x, yellow_rest_y, red_rest_y, blue_rest_y):
  WINDOW.fill(BLACK)
  WINDOW.blit(textchoose, (WIDTH//2 - 300, 40))
  #Yellow box
  pygame.draw.rect(WINDOW, (0,0,0), choosebox1)
  WINDOW.blit(choose, (75,390))
  #Red box
  pygame.draw.rect(WINDOW, (0,0,0), choosebox2)
  WINDOW.blit(choose, (350,390))
  #Blue box
  pygame.draw.rect(WINDOW, (0,0,0), choosebox3)
  WINDOW.blit(choose, (627,390))
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

#Sound


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


