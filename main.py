# Import the pygame library and initialise the game engine

import pygame
from paddle import Paddle
from ball import Ball
import sys
from clean_cache import*

#on nettoye le cache
clean()

pygame.init()

# Définition des couleurs
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 64, 64)
BLUE = (89, 164, 255)

# Ouvverture d'une fenetre
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

#on dessine les bars
paddleA = Paddle(BLUE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(RED, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

#on dessine la balle
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

#on créer une list qui va contenir tous les obj du jeu
all_sprites_list = pygame.sprite.Group()

# On ajoute les deux bars et la balle dans la liste
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# ( carry on continuer) variable pour quitter le jeu
carryOn = True

# pour controler la mise à jour de l'écrand
clock = pygame.time.Clock()

#On initialise les scores
scoreA = 0
scoreB = 0

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
              pygame.quit()
              sys.exit()
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Si il Appuye suer la touche x il quit le jeu
                     carryOn=False

    #Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(8)
    if keys[pygame.K_s]:
        paddleA.moveDown(8)
    if keys[pygame.K_UP]:
        paddleB.moveUp(8)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(8)

    # --- on met à jour les objets du jeu
    all_sprites_list.update()


    #on vérifie si la balle rebondit sur les 4 murs

    if ball.rect.x>=690:
        scoreA+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]

    #Détectection des collisions entre la balle et la bar
    #et augmente la difficulté à chaque collision
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
      ball.bounce()
      #ball.difficulty()


    #mise à jour de l'écrand
    # 1, on met le font en noir.
    screen.fill(BLACK)
    #2, on dessine la line blanche
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    #on dessine tous les obj
    all_sprites_list.draw(screen)

    #affiche les scores:
    font = pygame.font.SysFont('Arial', 74)
    text = font.render(str(scoreA), 1, BLUE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, RED)
    screen.blit(text, (420,10))

    # --- on met à jour l'écran avec ce que nous avons dessiné.
    pygame.display.flip()

    # --- Limitation à 160 frames par seconde
    clock.tick(180)

#on quit le jeu:
pygame.quit()
sys.exit()