# Разработай свою игру в этом файле!
import pygame
window = pygame.display.set_mode((700,500))
pygame.display.set_caption('Игра')
#picture = pygame.transform.scale(pygame.image.load('galaxy_1.jpg'),(700,500))
green = (0,255,0)
blue = (0,0,255)
window.fill(green)
class Gamesprite(pygame.sprite.Sprite):
    def __init__(self,picture,width,height,x,y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(picture),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Main_hero(Gamesprite):
    def __init__(self, image,x,y,width,height,playerspeed_x,playerspeed_y):
        Gamesprite.__init__(self,image,x,y,width,height)
        self.x_speed = playerspeed_x
        self.y_speed = playerspeed_y
    def update(self):
        if player.rect.x <= 620 and player.x_speed > 0 or player.rect.x >= 0 and player.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = pygame.sprite.spritecollide(self,walls,False)
        if self.x_speed > 0:
            for wall in platforms_touched:
                self.rect.right = min(self.rect.right,wall.rect.left)
        elif self.x_speed < 0:
            for wall in platforms_touched:
                self.rect.left = max(self.rect.left,wall.rect.right)       
        if player.rect.y <= 420 and player.y_speed > 0 or player.rect.y >= 0 and player.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = pygame.sprite.spritecollide(self,walls,False)
        if self.y_speed > 0:
            for wall in platforms_touched:
                self.rect.bottom = min(self.rect.bottom,wall.rect.top)
        elif self.y_speed < 0:
            for wall in platforms_touched:
                self.rect.top = max(self.rect.top,wall.rect.bottom)
    def fire(self):
        bullet = Bullet('weapon.png',15,20,self.rect.right,self.rect.centery,15)
        bullets.add(bullet)
class Enemy(Gamesprite):
    def __init__(self, image,x,y,width,height,speed):
        Gamesprite.__init__(self,image,x,y,width,height)
        self.speed = speed
    def update(self):
        if self.rect.x > 630 or self.rect.x < 380:
            self.speed = -1 * self.speed
        self.rect.x += self.speed
class Bullet(Gamesprite):
    def __init__(self, image,x,y,width,height,speed):
        Gamesprite.__init__(self,image,x,y,width,height) 
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 700:
            self.kill()
bullets = pygame.sprite.Group()
wall_1 = Gamesprite('platform_h.png',50,500,300,150)
wall_2 = Gamesprite('platform_v.png',270,50,100,350)
walls = pygame.sprite.Group()
walls.add(wall_1)
walls.add(wall_2)
player = Main_hero('hero.png',80,80,5,420,0,0)
monster1 = Enemy('enemy.png',80,80,620,180,-2)
monster2 = Enemy('enemy.png',80,80,620,100,-2)
monsters = pygame.sprite.Group()
monsters.add(monster1)
monsters.add(monster2)
final_sprite = Gamesprite('enemy2.png',80,80,615,400)
run = True
finish = False
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_speed = -5
            elif event.key == pygame.K_RIGHT:
                player.x_speed = 5
            elif event.key == pygame.K_UP:
                player.y_speed = -5
            elif event.key == pygame.K_DOWN:
                player.y_speed = 5
            elif event.key == pygame.K_SPACE:
                player.fire()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.x_speed = 0
            elif event.key == pygame.K_RIGHT:
                player.x_speed = 0
            elif event.key == pygame.K_UP:
                player.y_speed = 0
            elif event.key == pygame.K_DOWN:
                player.y_speed = 0
    #window.blit(picture,(0,0))
    if not finish:    
        window.fill(green)
        wall_1.reset()
        wall_2.reset()
        final_sprite.reset()
        pygame.sprite.groupcollide(monsters,bullets,True,True)
        monsters.draw(window)
        monsters.update()
        pygame.sprite.groupcollide(bullets,walls,True,False)
        bullets.draw(window)
        bullets.update()
        player.reset()
        player.update()
    if pygame.sprite.spritecollide(player,monsters,False):
        finish = True
        img = pygame.image.load('game-over_1.png')
        d = img.get_width() // img.get_height()
        window.fill((255,255,255))
        window.blit(pygame.transform.scale(img,(500*d,500)),(0,0))
    if pygame.sprite.collide_rect(player,final_sprite):
        finish = True
        img = pygame.image.load('thumb.jpg ')
        window.fill((255,255,255))
        window.blit(pygame.transform.scale(img,(500,500)),(0,0))
    pygame.display.update()