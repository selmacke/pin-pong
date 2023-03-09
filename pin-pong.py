from pygame import *
from random import *
from time import time as timer

window = display.set_mode((700,500))

display.set_caption("Pin-Pong")
background=transform.scale(image.load("field.jpg"), (700,500))




class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image), (40,120))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
        
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 380:
            self.rect.y += self.speed 

    
    def update2(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 380:
            self.rect.y += self.speed 
   

rocket_left=Player("pinpong.png",25,200,10)
rocket_right=Player("pinpong.png",635,200,10)

clock=time.Clock()
FPS=60    
lost=0
score=0
class   Enemy(GameSprite):
    def update(self):
        global lost 
        if self.rect.y<=470:
            self.speed=abs(self.speed)
            self.rect.y+=self.speed
        else:
            self.rect.y = 0
            self.rect.x = randint(20,640)
            self.speed = randint(1,2)
            lost+=1
ball = Enemy("ballforpinpong.png",350,250,5)


#font.init()
#font1=font.SysFont("Arial",40)
#font2=font.SysFont("Arial",80)
#win=font1.render("Ты победил!",True,(13,43,22))
#lose=font2.render("Ты проигал!",True,(240, 12, 12))


real_time = False
game=True
game_over=False
while game:
    if game_over == False:
        window.blit(background,(0,0))
        ball.reset()
        rocket_left.update()
        rocket_left.reset()
        rocket_right.update2()
        rocket_right.reset()

        #keys=key.get_pressed()
        #timer=font1.render("Пропущено: "+str(lost),True,(247, 5, 37))
        #window.blit(timer,(25,35))
        #lives=font1.render("Жизней осталось: "+str(lost),True,(247, 5, 37))
        #window.blit(lives,(25,350))
        #if lost >= 9:
        #    game_over=True
        #    window.blit(lose,(150,200))
        #window.blit(win,(250,250))
        #while num_of_lose != 0:
            #if sprite.spritecollide(asteroid1,spaceship, False) or sprite.spritecollide(asteroid2,spaceship, False):
                #num_of_lose - 1
        #if real_time == True:
    #if num_of_lose == 0:
        #game_over = True
        #window.blit(lose,(150,200))

    if sprite.spritecollide(ball,rocket_left,False):
        speed_y *= -1
    if sprite.spritecollide(ball,rocket_right,False):
        speed_y *= -1
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
clock.tick(FPS)