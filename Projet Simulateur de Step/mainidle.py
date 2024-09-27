import pygame;
from random import randint;
leftnote=False
rightnote=False
upnote=False
downnote=False
#Création de la classe Personnage qui réprésentera notre personnage
class Personnage():
    def __init__(self,pv):
        self.pv=pv
        self.position = 0 #self.position représente l'état du personnage , 0 pour la position par défaut
        self.score=0#initialisation du score à 0
        self.combo=1
        self.combomult=1

    def move(self,position):#permet de faire changer l'id de position
        self.position = position

personnage1=Personnage(3)

#Initialisation de la fenêtre PyGame
pygame.init()
pygame.mixer.init()

ecran = pygame.display.set_mode((780,500))
pygame.display.set_caption("Simulateur de Step")

#Chargement des images du menu et des son
pygame.mixer.music.load("./image_bank/badpiggies.mp3")

ezimage=pygame.image.load("./image_bank/ezbutton.png").convert_alpha()
medimage=pygame.image.load("./image_bank/medbutton.png").convert_alpha()
hardimage=pygame.image.load("./image_bank/hardbutton.png").convert_alpha()
startimage=pygame.image.load("./image_bank/startbutton.png").convert_alpha()
surfdroit=pygame.image.load("./image_bank/surfdroit.png").convert_alpha()
surfgauche=pygame.image.load("./image_bank/surfgauche.png").convert_alpha()
basique=pygame.image.load("./image_bank/basique.png").convert_alpha()
devant=pygame.image.load('./image_bank/devant.png').convert_alpha()
gymnase=pygame.image.load('./image_bank/gymnase.jpg').convert_alpha()

InMenu=0
while InMenu==0:#Tant que le jeu est pas arreté 

    #Raffraichissement de l'affichage pygame en boucle
    
    #affichage image menu difficulté et mise du fond en blanc
    ecran.fill('white')
    ecran.blit(ezimage,(30,30))
    zoneClicableEzButton=pygame.Rect((30,30),(100,75))
    ecran.blit(medimage,(30,180))
    zoneClicableMedButton=pygame.Rect((30,180),(100,75))
    ecran.blit(hardimage,(30,330))
    zoneClicableHardButton=pygame.Rect((30,330),(100,75))
    
    pygame.display.flip()
    
    for event in pygame.event.get():#Possibilité de fermer la fenetre pygame ce qui arrete le programme
        if event.type==pygame.QUIT:
            Arret=1
        elif event.type==pygame.MOUSEBUTTONUP:#Detection des clics sur les difficultés
            if event.button==1:
                if zoneClicableEzButton.collidepoint(event.pos):
                    InMenu=1
                    personnage1.pv=3
                elif zoneClicableMedButton.collidepoint(event.pos):
                    InMenu=1
                    personnage1.pv=2
                elif zoneClicableHardButton.collidepoint(event.pos):
                    InMenu=1
                    personnage1.pv=1

print(personnage1.pv)
EnJeu=False

HautOn=False
BasOn=False
DroiteOn=False
GaucheOn=False


InMenu=0
while InMenu==0:#Tant que le jeu est pas arreté 

    #Raffraichissement de l'affichage pygame en boucle
    
    #affichage image menu difficulté et mise du fond en blanc
    ecran.fill('white')
    ecran.blit(ezimage,(30,30))
    zoneClicableEzButton=pygame.Rect((30,30),(100,75))
    ecran.blit(medimage,(30,180))
    zoneClicableMedButton=pygame.Rect((30,180),(100,75))
    ecran.blit(hardimage,(30,330))
    zoneClicableHardButton=pygame.Rect((30,330),(100,75))
    
    pygame.display.flip()
    
    for event in pygame.event.get():#Possibilité de fermer la fenetre pygame ce qui arrete le programme
        if event.type==pygame.QUIT:
            Arret=1
        elif event.type==pygame.MOUSEBUTTONUP:#Detection des clics sur les difficultés
            if event.button==1:
                if zoneClicableEzButton.collidepoint(event.pos):
                    InMenu=1
                    personnage1.pv=3
                elif zoneClicableMedButton.collidepoint(event.pos):
                    InMenu=1
                    personnage1.pv=2
                elif zoneClicableHardButton.collidepoint(event.pos):
                    InMenu=1
                    personnage1.pv=1

print(personnage1.pv)
EnJeu=False

HautOn=False
BasOn=False
DroiteOn=False
GaucheOn=False



InMenuStart=0#Passage au menu Start même detection qu'au dessus
while InMenuStart==0:
    pygame.display.flip()
    ecran.fill('white')
    ecran.blit(startimage,(300,180))
    zoneClicableStartButton=pygame.Rect((300,180),(100,75))
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONUP:
            if event.button==1:
                if zoneClicableStartButton.collidepoint(event.pos):
                    InMenuStart=1

EnJeu=0
ecran.fill('white')
ecran.blit(gymnase,(0,0))
ecran.blit(devant,(0,0))
pygame.mixer.music.play()
pygame.mixer.music.load("./image_bank/fail.mp3")
TPSZero=pygame.time.get_ticks()

while EnJeu<=0:
    pygame.display.flip()
    keys=pygame.key.get_pressed()
    if personnage1.pv==0:EnJeu=1#Arrêt du jeu si personnage n'a plus de pv
    def posgauche():
        rdmgauche=randint(0,0)
        if rdmgauche==0:
                ecran.fill('white')
                ecran.blit(gymnase,(0,0))
                ecran.blit(surfgauche,(0,0))
                print('surf gauche')#changer affichage du perso en pos surf gauche
                print(personnage1.score,personnage1.pv)
    def posdroite():
        rdmdroite=randint(0,0)
        if rdmdroite==0:
                ecran.fill('white')
                ecran.blit(gymnase,(0,0))
                ecran.blit(surfdroit,(0,0))
                print('surf droite')#changer affichage du perso en pos surf gauche
                print(personnage1.score,personnage1.pv)
    def poshaute():
        rdmhaute=randint(0,0)
        if rdmhaute==0:
                ecran.fill('white')
                ecran.blit(gymnase,(0,0))
                ecran.blit(basique,(0,0))
                print('basique')#changer affichage du perso en pos surf gauche
                print(personnage1.score,personnage1.pv)
    def posbasse():
        rdmbasse=randint(0,0)
        if rdmbasse==0:
                ecran.fill('white')
                ecran.blit(gymnase,(0,0))
                ecran.blit(devant,(0,0))
                print('devant')#changer affichage du perso en pos surf gauche
                print(personnage1.score,personnage1.pv)
                if 0<=personnage1.combo<10:
                    personnage1.combomult=1
                if 10<=personnage1.combo<20:
                    personnage1.combomult=2
                if 20<=personnage1.combo<30:
                    personnage1.combomult=3
                if 30<=personnage1.combo<40:
                    personnage1.combomult=4
                if 40<=personnage1.combo<50:
                    personnage1.combomult=5
                if 50<=personnage1.combo<60:
                    personnage1.combomult=6
                if 60<=personnage1.combo<70:
                    personnage1.combomult=7
                if 70<=personnage1.combo<80:
                    personnage1.combomult=8
                if 80<=personnage1.combo<90:
                    personnage1.combomult=9
                if 100<=personnage1.combo:
                    personnage1.combomult=10
    for event in pygame.event.get():
            if keys[pygame.K_LEFT]:
                if leftnote==True:
                    personnage1.score+=100*personnage1.combomult
                    personnage1.combo+=1
                    posgauche()
                if leftnote==False:
                    personnage1.combo=0
                    personnage1.pv-=1
                    posgauche()
                    pygame.mixer.music.play()
            if keys[pygame.K_RIGHT]:
                if rightnote==True:
                    personnage1.score+=100*personnage1.combomult
                    personnage1.combo+=1
                    posdroite()
                if rightnote==False:
                    personnage1.combo=0
                    personnage1.pv-=1
                    posdroite()
                    pygame.mixer.music.play()
            if keys[pygame.K_UP]:
                if upnote==True:
                    personnage1.score+=100*personnage1.combomult
                    personnage1.combo+=1
                    poshaute()
                if upnote==False:
                    personnage1.combo=0
                    personnage1.pv-=1
                    poshaute()
                    pygame.mixer.music.play()
            if keys[pygame.K_DOWN]:
                if downnote==True:
                    personnage1.score+=100*personnage1.combomult
                    personnage1.combo+=1
                    posbasse()
                if downnote==False:
                    personnage1.combo=0
                    personnage1.pv-=1
                    posbasse()
                    pygame.mixer.music.play()
