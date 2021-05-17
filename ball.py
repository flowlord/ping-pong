import pygame
from random import randint

BLACK = (0, 0, 0)

class Ball(pygame.sprite.Sprite):
    #Cette classe représente une voiture. Il dérive de la classe "Sprite" de Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Définissez la couleur d'arrière-plan et définissez-la pour qu'elle soit transparente
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # On dessine une balle (un rectangle)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        #définition de la vélocité de la balle (sa vitesse)
        self.velocity = [randint(3,5),randint(-5,5)]

        # Récupérez l'objet rectangle qui a les dimensions de l'image.
        self.rect = self.image.get_rect()

    #mise à jour
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


    #Rebondissement de la balle
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)


#INJOUABLE POUR LE JOUEUR ROUGE !!

#    #J'ajoute une difficulté pour un peut plus de piment !

#    def difficulty(self):
#        self.velocity = [randint(4,6),randint(-8,8)]

