import pygame,random
pygame.init()
screen = pygame.display.set_mode((800,800))
icon = pygame.image.load('gameicon.png')
pygame.display.set_caption('Legend of theodora')
pygame.display.set_icon(icon)
char = pygame.image.load('coconut.png')
spritesheet = pygame.image.load('char_spritesheet.png').convert_alpha()
enemy_spritesheet = pygame.image.load('Enemy_spritesheet.png')
background = pygame.image.load('map2.png')
run = True
white = (255,255,255)
black = (0,0,0)
frames = []
frames_d = []
frames_a = []
enemy_frames_d = []
for i in range(13) :
    x = i*32
    y = 0
    frame_rect = pygame.Rect(x, y , 32,32)
    frames.append(pygame.transform.scale(spritesheet.subsurface(frame_rect),(40,40)))
for i in range (10) :
    x = i*32
    y = 64
    frame_rect = pygame.Rect(x,y,32,32)
    frames_d.append(pygame.transform.scale(spritesheet.subsurface(frame_rect),(40,40)))
    frames_a.append(pygame.transform.flip((pygame.transform.scale(spritesheet.subsurface(frame_rect),(40,40))),True,False) )
for j in range(0,1) :    
    for i in range(6) :
        x = i*64
        y = 192+j*64
        frame_rect = pygame.Rect(x,y,64,64)
        enemy_frames_d.append(pygame.transform.scale((enemy_spritesheet.subsurface(frame_rect)),(40,40)))

class Player(pygame.sprite.Sprite) :      #Player class
    def __init__(self,x,y) :
        super().__init__()
        self.Health = 90
        self.frames = frames
        self.frames_d = frames_d
        self.frames_a = frames_a
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.current_frame = 0
        self.frametimer = 0
        self.frame_delay = 18
        self.current = 0
    def upadate(self) :
        self.frametimer = pygame.time.get_ticks()
        if self.frametimer - self.current >= self.frame_delay :
            self.current_frame = (self.current_frame+1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.frame_timer = 0
        self.current = pygame.time.get_ticks()
    def move_right(self) :
        if self.rect.x <=740  :
            self.rect.x +=40
        if pygame.sprite.spritecollide(self,blocked_areas,False) :
            self.rect.x -=40
        if pygame.sprite.spritecollide(self,blocked_areas_enemy,True) :
            self.Health-=10
            print(self.Health)        
    def move_left(self) :
        if self.rect.x >= 40 :
            self.rect.x -=40
        if pygame.sprite.spritecollide(self,blocked_areas,False) :
            self.rect.x +=40
        if pygame.sprite.spritecollide(self,blocked_areas_enemy,True) :
            self.Health-=10
            print(self.Health)
    def move_down(self) :
        if self.rect.y <=740 :
            self.rect.y +=40
        if pygame.sprite.spritecollide(self,blocked_areas,False) :
            self.rect.y -=40
        if pygame.sprite.spritecollide(self,blocked_areas_enemy,True) :
            self.Health-=10
            print(self.Health)
    def move_up(self) :
        if self.rect.y > 0 :
            self.rect.y -=40
        if pygame.sprite.spritecollide(self,blocked_areas,False) :
            self.rect.y +=40
        if pygame.sprite.spritecollide(self,blocked_areas_enemy,True) :
            self.Health-=10
            print(self.Health)
    def attack(self,current_mouse_pos,next_mousepos) :
        if next_mousepos[0] - current_mouse_pos[0] >0 :
            self.frametimer = pygame.time.get_ticks()
            if self.frametimer - self.current >= 5 :
                self.current_frame = (self.current_frame+1) % len(self.frames_d)
                self.image = self.frames_a[self.current_frame]
                self.frame_timer = 0
            self.current = pygame.time.get_ticks()    
        else :
            self.frametimer = pygame.time.get_ticks()
            if self.frametimer - self.current >= 5 :
                self.current_frame = (self.current_frame+1) % len(self.frames_d)
                self.image = self.frames_d[self.current_frame]
                self.frame_timer = 0
            self.current = pygame.time.get_ticks()
class Enemy (pygame.sprite.Sprite) :
    def __init__(self,x,y) :
        super().__init__()
        self.frames = enemy_frames_d
        self.frames_d = frames_d
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.current_frame = 0
        self.frametimer = 0
        self.frame_delay = 100
        self.current = 0
        self.d = -40
    def upadate(self) :
        self.frametimer = pygame.time.get_ticks()
        if self.frametimer - self.current >= self.frame_delay :
            self.current_frame = (self.current_frame+1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            self.frame_timer = 0
        self.current = pygame.time.get_ticks()
        self.rect.x += self.d
        if self.rect.x <= 40 :
            self.d=self.d*(-1)
        if self.rect.x >= 280 :
            self.d=self.d*(-1)
        
    def move_right(self) :
        if self.rect.x <=740  :
            self.rect.x +=40
        if pygame.sprite.spritecollide(self,blocked_areas,False) :
            self.rect.x -=40
    def move_left(self) :
        if self.rect.x >= 40 :
            self.rect.x -=40
        if pygame.sprite.spritecollide(self,blocked_areas,False) :
            self.rect.x +=40
    def move_down(self) :
        if self.rect.y <=740 :
            self.rect.y +=40
        if pygame.sprite.spritecollide(self,blocked_areas,False) :
            self.rect.y -=40
    def move_up(self) :
        if self.rect.y > 0 :
            self.rect.y -=40
        if pygame.sprite.spritecollide(self,blocked_areas,False) :
            self.rect.y +=40
clock = pygame.time.Clock() 
player = Player(0,0)
enemy_1 = Enemy(240,160)
m_b = False
Menu_state = True
class Bloackedareas(pygame.sprite.Sprite) :
     def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
blocked_areas = pygame.sprite.Group()
blocked_areas_enemy=pygame.sprite.Group()
blocked_area1 = Bloackedareas(80,0,480,40)
blocked_areas.add(blocked_area1)
enemy_1_bloacked = Bloackedareas(enemy_1.rect.x,enemy_1.rect.y,40,40)
blocked_areas_enemy.add(enemy_1_bloacked)
font = pygame.font.Font('freesansbold.ttf',36)
while Menu_state == True :    #Main Menu
    screen.fill(black)
    Text = font.render('RPG SHIT',True,white)
    text_rect = Text.get_rect(center=(400, 400))
    screen.blit(Text, text_rect)
    pygame.display.update()
    for event in pygame.event.get() :
        if event.type == pygame.KEYDOWN :
            Menu_state = False
            screen.fill(black)
while run == True  :           #Event handler
    current_mouse_pos = pygame.mouse.get_pos()
    player.upadate()
    enemy_1.upadate()
    screen.blit(background,(0,0))
    screen.blit(enemy_1.image,enemy_1.rect)
    screen.blit(player.image,player.rect)
    clock.tick(10)
    pygame.display.update()
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            run = False
        if event.type == pygame.KEYDOWN and event.key ==  pygame.K_d:
            player.move_right()
            screen.blit(background,(0,0))
            screen.blit(player.image,player.rect)
            pygame.display.update()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a :
            player.move_left()
            screen.blit(background,(0,0))
            screen.blit(player.image,player.rect)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s :
            player.move_down()
            screen.blit(background,(0,0))
            screen.blit(player.image,player.rect)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w :
            player.move_up()
            screen.blit(background,(0,0))
            screen.blit(player.image,player.rect)
        next_mousepos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and  event.button == 1 and next_mousepos != current_mouse_pos :
            for i in range(20) :
                player.attack(next_mousepos,current_mouse_pos)
                screen.blit(background,(0,0))
                screen.blit(player.image,player.rect)
                pygame.display.update()
                m_b =True
                time = pygame.time.get_ticks()
    
