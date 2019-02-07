import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (1280, 720) #resolution of the game
global HORIZ_MOV_INCR
HORIZ_MOV_INCR = 16 #speed of movement
global FPS
global clock
clock = pygame.time.Clock()
global time_spent
global amountoftime
amountoftime = 1800

def RelRect(actor, camera):
    return pygame.Rect(actor.rect.x-camera.rect.x, actor.rect.y-camera.rect.y, actor.rect.w, actor.rect.h)

class Camera(object):
    '''Class for center screen on the player'''
    def __init__(self, screen, player, level_width, level_height):
        self.player = player
        self.rect = screen.get_rect()
        self.rect.center = self.player.center
        self.world_rect = Rect(0, 0, level_width, level_height)

    def update(self):
      if self.player.centerx > self.rect.centerx + 25:
          self.rect.centerx = self.player.centerx - 25
      if self.player.centerx < self.rect.centerx - 25:
          self.rect.centerx = self.player.centerx + 25
      if self.player.centery > self.rect.centery + 25:
          self.rect.centery = self.player.centery - 25
      if self.player.centery < self.rect.centery - 25:
          self.rect.centery = self.player.centery + 25
      self.rect.clamp_ip(self.world_rect)

    def draw_sprites(self, surf, sprites):
        for s in sprites:
            if s.rect.colliderect(self.rect):
                surf.blit(s.image, RelRect(s, self))


class Obstacle(pygame.sprite.Sprite):
    '''Class for create obstacles'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("world/brick.jpg").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

class Boost(pygame.sprite.Sprite):
    '''Class for create obstacles'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("world/boost.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

class Bomb(pygame.sprite.Sprite):
    '''Class for create obstacles'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("world/bomb.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]
            

class Crashman(pygame.sprite.Sprite):
    '''class for player and collision'''
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.movy = 0
        self.movx = 0
        self.x = x
        self.y = y
        self.contact = False
        self.jump = False
        self.image = pygame.image.load('actions/right.jpg').convert()
        self.rect = self.image.get_rect()
        self.run_left = ["actions/run_left000.png","actions/run_left001.png",
                         "actions/run_left002.png", "actions/run_left003.png",
                         "actions/run_left004.png", "actions/run_left005.png",
                         "actions/run_left006.png", "actions/run_left007.png"]
        self.run_right = ["actions/run_right000.png","actions/run_right001.png",
                         "actions/run_right002.png", "actions/run_right003.png",
                         "actions/run_right004.png", "actions/run_right005.png",
                         "actions/run_right006.png", "actions/run_right007.png"]

        self.direction = "right"
        self.rect.topleft = [x, y]
        self.frame = 0

    def update(self, up, down, left, right):
        style = "bomb"
        if up:
            if self.contact:
                if self.direction == "right":
                    self.image = pygame.image.load("actions/jump_right.png")
                self.jump = True
                self.movy -= 20
        if down:
            if self.contact and self.direction == "right":
                self.image = pygame.image.load('actions/down_right.png').convert_alpha()
            if self.contact and self.direction == "left":
                self.image = pygame.image.load('actions/down_left.png').convert_alpha()

        if not down and self.direction == "right":
                self.image = pygame.image.load('actions/right.jpg').convert_alpha()

        if not down and self.direction == "left":
            self.image = pygame.image.load('actions/left.jpg').convert_alpha()

        if left:
            self.direction = "left"
            self.movx = -HORIZ_MOV_INCR
            if self.contact:
                self.frame += 1
                self.image = pygame.image.load(self.run_left[self.frame]).convert_alpha()
                if self.frame == 6: self.frame = 0
            else:
                self.image = self.image = pygame.image.load("actions/jump_left.png").convert_alpha()

        if right:
            self.direction = "right"
            self.movx = +HORIZ_MOV_INCR
            if self.contact:
                self.frame += 1
                self.image = pygame.image.load(self.run_right[self.frame]).convert_alpha()
                if self.frame == 6: self.frame = 0
            else:
                self.image = self.image = pygame.image.load("actions/jump_right.png").convert_alpha()

        if not (left or right):
            self.movx = 0
        self.rect.right += self.movx

        self.collide(self.movx, 0, world)
        #instance.of class of object


        if not self.contact:
            self.movy += 0.3
            if self.movy > 10:
                self.movy = 10
            self.rect.top += self.movy

        if self.jump:

            self.movy += 2
            self.rect.top += self.movy
            if self.contact == True:
                self.jump = False

        self.contact = False
        self.collide(0, self.movy, world)


    def collide(self, movx, movy, world):
        self.contact = False
        for o in world:
            if self.rect.colliderect(o):
                if isinstance(o,Bomb):
                    screen.blit(font2.render("You Win!", True, (255, 255, 255)), (350, 225))
                    screen.blit(font.render("You found the bomb in time", True, (255, 255, 255)), (430, 360))
                    pygame.display.flip()
                    break
                elif isinstance(o,Bomb):
                    amountoftime += 300
                else:
                    if movx > 0:
                        self.rect.right = o.rect.left
                    if movx < 0:
                        self.rect.left = o.rect.right
                    if movy > 0:
                        self.rect.bottom = o.rect.top
                        self.movy = 0
                        self.contact = True
                    if movy < 0:
                        self.rect.top = o.rect.bottom
                        self.movy = 0

class Level(object):
    '''Read a map and create a level'''
    def __init__(self, open_level):
        self.level2 = []
        self.world = []
        self.all_sprite = pygame.sprite.Group()
        self.level = open(open_level, "r")

    def create_level(self, x, y):
        for l in self.level:
            self.level2.append(l)

        for row in self.level2:
            for col in row:
                if col == "X":
                    obstacle = Obstacle(x, y)
                    self.world.append(obstacle)
                    self.all_sprite.add(self.world)
                if col == "P":
                    self.crashman = Crashman(x,y)
                    self.all_sprite.add(self.crashman)
                if col == "S":
                    obstacle = Boost(x, y)
                    self.world.append(obstacle)
                    self.all_sprite.add(self.world)
                if col == "C":
                    obstacle = Bomb(x, y)
                    self.world.append(obstacle)
                    self.all_sprite.add(self.world)
                x += 25
            y += 25
            x = 0

    def get_size(self):
        lines = self.level2
        #line = lines[0]
        line = max(lines, key=len)
        self.width = (len(line))*25
        self.height = (len(lines))*25
        return (self.width, self.height)



def tps(orologio,fps):
    temp = orologio.tick(fps)
    tps = temp / 1000.
    return tps


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN, 32)
screen_rect = screen.get_rect()
background = pygame.image.load("world/background3.jpg").convert_alpha()
background_rect = background.get_rect()
level = Level("level/level2.txt")
level.create_level(0,0)
world = level.world
crashman = level.crashman
pygame.mouse.set_visible(0)

#counter, text = 60, '60'.rjust(3)
#pygame.time.set_timer(pygame.USEREVENT, 1000)   #FONT STUFF
font = pygame.font.SysFont('Arial', 40)
font2 = pygame.font.SysFont('Times New Roman', 144)

camera = Camera(screen, crashman.rect, level.get_size()[0], level.get_size()[1])
all_sprite = level.all_sprite

FPS = 30
clock = pygame.time.Clock()

up = down = left = right = False
x, y = 0, 0
counter =1
while True:
    amountoftime-=1
    screen.blit(font.render("Time Left: ", True, (255, 255, 0)), (10, 10))
    screen.blit(font.render(str(int(amountoftime/30)), True, (255, 255, 0)), (190, 11))
    pygame.display.flip()
    #clock.tick(60)
    if amountoftime <= 0:
        screen.blit(font2.render("You Lose!", True, (255, 255, 255)), (350, 225))
        screen.blit(font.render("Did not find the bomb in time", True, (255, 255, 255)), (400, 375))
        pygame.display.flip()
        break
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter).rjust(3)if counter > 0 else 'BOOM!'
            
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key == K_UP:
            up = True
        if event.type == KEYDOWN and event.key == K_DOWN:
            down = True
        if event.type == KEYDOWN and event.key == K_LEFT:
            left = True
        if event.type == KEYDOWN and event.key == K_RIGHT:
            right = True

        if event.type == KEYUP and event.key == K_UP:
            up = False
        if event.type == KEYUP and event.key == K_DOWN:
            down = False
        if event.type == KEYUP and event.key == K_LEFT:
            left = False
        if event.type == KEYUP and event.key == K_RIGHT:
            right = False

    asize = ((screen_rect.w // background_rect.w + 1) * background_rect.w, (screen_rect.h // background_rect.h + 1) * background_rect.h)
    bg = pygame.Surface(asize)

    for x in range(0, asize[0], background_rect.w):
        for y in range(0, asize[1], background_rect.h):
            screen.blit(background, (x, y))

    time_spent = tps(clock, FPS)
    camera.draw_sprites(screen, all_sprite)

    crashman.update(up, down, left, right)
    camera.update()
    pygame.display.flip()
