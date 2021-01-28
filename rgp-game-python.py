### IMPORT ###
import cmd # not currently used, from tutorial
import textwrap # not currently used, from tutorial
import sys
import os
import time
import random # not currently used, from tutorial

### TEXT EFFECT FUNCTION ###
def texteffect(string, n = 0.04):

    q = string
    for character in q:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(n)

### Random number + somme de tous -> Need de générer nombre aléatoire à chaque fois et les additionner à chaque fois

def random_number(x,n):
  d = random.randint(x,n)
  return d

### Variable pour les rondins de bois qui s'additionnent
rondins = 0

## Jeu du Pierre Feuille Ciseau 

def choix_utilisateur():
    """Cette fonction permet au joueur de choisir son mouvement"""
    joueur = input("\nPierre, Papier ou Ciseaux ? (à écrire avec sans majuscule !)\n")
    while joueur not in ["pierre","papier","ciseaux"]:
        joueur = input("Pierre, Papier ou Ciseaux ? (à écrire avec une majuscule !)\n")
    return(joueur)

def choix_ordinateur():
    """Cette fonction permet à l'ordinateur de générer aléatoirement un mouvement"""
    n = random.randint(1,3)
    if n == 1:
        ordi = "pierre"
    elif n==2:
        ordi = "papier"
    else:
        ordi = "ciseaux"
    return(ordi)

### Mort lors du jeu 
def mort():
  texteffect("\nMalheureusement vous avez succombé. Et votre sentence est irrévocable.\nRetour au menu principal dans\n3... 2... 1...\n\n\n",.02)
  title_screen()

def win():
  texteffect("\nFÉLICITATIONS ! Tu as été suffisamment talentueux pour t'apprivoiser les lieux, et recueuillir assez de bois pour te construire une barque et t'en aller ! Ta mission est terminée !\nRetour au menu principal dans\n3... 2... 1...\n\n\n",.02)
  title_screen()
### Figuring out how users might respond ###

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes", "oui"]
no = ["N", "n", "no", "oui"]

required = ("\nOn a dit A, B ou C, pas d'autres choses !\n")

####################
### MENU SCREENS ###
####################

def intro():
  # rondrand = random_number(1,10)
  # rondins = rondrand
  # print(rondins)
  # global rondins
  # rondins = rondins
  # rondintro = random_number(1,3)
  # rondins = rondins + rondintro
  # print(rondins)
  print ("\n" + myPlayer.name + " vous vous reveillez sans souvenir, vous etes seul sur une plage. Voulez vous bronzer ou aller dans la foret ?\n")
  time.sleep(1)
  print ("""  A. Explorer vers le nord, et s'engonfrer dans la forêt
  B. Bronzer sur la plage...même si il n'y a pas le (tri) cocktail""")
  # rondrand2 = random_number(1,10)
  # rondins = rondins + rondrand2
  # print(rondins)
  choice = input("> ") #Here is your first choice.
  if choice in answer_A:
    foret_1()
  elif choice in answer_B:
    print ("\nVous avez perdu une journée, mais avancée quand-même dans la forêt. Il faut pas abuser " + myPlayer.name + "!")
    time.sleep(1)
    foret_1()
  else:
    print (required)
    intro()

def foret_1():
  # global rondins
  # rondins = rondins
  # rondforet = random_number(1,3)
  # rondins = rondins + rondforet
  # print(rondins)
  print ("\nAprès quelques minutes de marche vous vous enfoncez dans la foret. Vous apercevez un sommet montagneux et entendez un cours d'eau. Ou voulez vous aller" + myPlayer.name + "?")
  time.sleep(1)
  print ("""  A. Montagne
  B. Rivière à l'ouest""")
  choice = input("> ")
  if choice in answer_A:
    montagne_2()
  elif choice in answer_B:
    riviere_2()
  else:
    print (required)
    foret_1()

###################################### IMPORTANT C'EST A FAIRE, TOUTE LA PARTIE RIVIERE ########################################################
def riviere_2():
  print ("\nAprès des heures vous arrivez au cours d'eau, felicitations ! Etant toujours prisonnier de cette nature, une jungle et un marecage barre ton chemin. Lequel veux-tu empreinter ?")
  time.sleep(1)
  print ("""  A. Marécage
  B. Jungle""")
  choice = input("> ")
  if choice in answer_A:
    marecage_4()
  elif choice in answer_B:
    jungle_4()
  else:
    print (required)
    riviere_2()
  
def jungle_4():
  global rondins
  rondins = rondins
  rondjungle = random_number(1,3)
  rondins = rondins + rondjungle
  print ("\nBienvenue dans la jungle il commence a faire tard. Il s'avère que tu as trouvé " + str(rondjungle) + " rondins de bois, veux-tu en profiter pour aller te faire un feu ou te refugier dans une cabane un peu plus loin ?")
  time.sleep(1)
  if rondins >= 7:
    win()
  print ("""  A. Cabane
  B. Feu""")
  choice = input("> ")
  if choice in answer_A:
    cabane_5()
  elif choice in answer_B:
    feu_5()
  else:
    print (required)
    jungle_4()

def cabane_5():
  print ("\nTu te poses tranquillement dans la cabane MAIS ATTENTION !!!! Une tarentule arrive.  Decides-tu de l'affronter ou de prendre tes jambes a ton cou")
  time.sleep(1)
  print ("""  A. Oui
  B. Non""")
  choice = input("> ")
  if choice in answer_A:
    randAraignée = random_number(1,2)
    if randAraignée == 1:
      print("La fuite aurait été une meilleure option... La morsure d'araignée ta tué dans d'atroces souffrance. La nature restera plus forte")
      mort()
    else:
      print("Pas de quoi avoir peur c'etait une petite araignée. Apres un jour de repos, tu vas en direction d'un feu de camp !")
      feu_5()
  elif choice in answer_B:
    print("Fragile, tu vas pas survir longtemps toi... tu es retourné à la plage.")
    intro()
  else:
    print (required)
    cabane_5()

def feu_5():
  print ("\nVous n'etes pas tres discret et vous entendez des bruits bizarre toute la nuit. Mais le feu vous a rechauffer et vous etes assez reveiller pour continuer votre marche. Au bout de quelque kilometre un maya vous a reperé et vous emmene dans sa tribu.")
  time.sleep(2)
  maya_6()

def maya_6():
  print ("\nApres votre arrivée les Mayas vous offre un marché : Ou bien vous restez 2 jours en échange d'un bois ou bien vous continuer votre route.")
  time.sleep(2)
  print ("""  A. Accepter le deal avec le Maya
  B. Continuer son chemin vers une direction qui nous intrigue""")
  choice = input("> ")
  if choice in answer_A:
    print ("\nPas dev' encore.")
    intro() ## Dev le rondin de bois + 1 enfaite
  elif choice in answer_B:
    plagesud()
  else:
    print (required)
    maya_6()

def plagesud():
  global rondins
  rondins = rondins
  rondplage = random_number(1,3)
  rondins = rondins + rondplage
  print ("\nVoici quelques jours que vous êtes sur cette ile maudite. Vous découvrez une belle plage, sur laquelle vous trouvez" + str(rondplage) + " rondins de bois.")
  print("Vous regardez le coucher de soleil malheureusement votre moment est pertubé par un bruit sourd qui vient du Nord c'est ainsi que vous decouvrez.... UN BAR ?!?!")
  if rondins >= 7:
    win()
  time.sleep(2)
  bar_5()

def bar_5():
  print ("\nVous ne vous posez pas de question, accoudé au bar. Vous choisissez de prendre de l'eau ou un martini ?")
  time.sleep(2)
  print ("""  A. Eau
  B. Alcool""")
  choice = input("> ")
  if choice in answer_A:
    ##rajouter rondins je pense!
    print("Sans mémoire vous vous reveillez en haut d'une montagne . Vous etiez dans le coma quelqu'un a sans doute du vous droguer. Vous avez perdu 1 jour, mais tout va bien pour vous.")
    montagne_2()
  elif choice in answer_B:
    print("Vous vous reveillez sur la plage de depart nu, depouillé et avec une gueule de bois monstrueuse. Vous avez perdu tout votre bois.")
    intro()
  else:
    print (required)
    bar_5()

def ruines_5():
  print ("\nCes ruines cachent bien leur jeu. De nombreuse choses ont été détruites sauf un temple, un bar et tu aperçois quelqu'un. Que décides tu de faire ? ")
  time.sleep(1)
  print ("""  A. Temple
  B. Denys
  C. Bar""")
  choice = input("> ")
  if choice in answer_A:
    temple_5()
  elif choice in answer_B:
    denys_5()
  elif choice in answer_C:
    bar_5()
  else:
    print (required)
    ruines_5()

def marecage_4():
  global rondins
  rondins = rondins
  rondmarecage = random_number(1,3)
  rondins = rondins + rondmarecage
  print ("\nL'odeur est nauséabonde tu en fais un malaise. Mais dans cette horreur, tu y trouves ton bonheur " + str(rondmarecage) + " rondins de bois.")
  if rondins >= 7:
    win()
  print("Tu décides de ne pas trainer et te diriges vers des ruines que tu apercois. Ce passage t'as énormément fatigué.")
  time.sleep(3)
  print (""" Tu n'as pas le choix, tu avances tout droit, tu n'as pas d'autres issues""")
  ruines_5()



def temple_5():
  print ("\nLe temple est magnifique mais pour y accéder tu dois traverser un pont qui parait très fragile. Tu serres les fesses pour pas qu'il ne casse")
  time.sleep(2)
  randPont = random_number(1,2)
  if randPont == 1:
    maya_6()
  else:
    riviere_2()  

def denys_5():
  print ("\nEn te rapprochant de cette personne tu te rends compte qu'il s'agit de Deny Bruyard. Tu ne sais plus si c'est la fatigue ou la folie mais il te propose une épreuve.")
  time.sleep(1)
  print("""\nBonsoir à tous, tu vas devoir m'affronter à une épreuve appelé pierre, feuille, ciseaux. Si tu gagnes tu remportes un bois, si tu perds tu passes ton chemin. Concentre toi cela pourrait t'aider dans ta quête".""")
  a = choix_utilisateur()
  b = choix_ordinateur()
  if a == "pierre" and b == "ciseaux":
      print("Vous avez gagné.")
      print("Bravo vous remportez X rondis de bois ! : AH ! bien joué je ne m'attendais pas a ce que tu gagnes. Voici un bois bon courage pour la suite. Evite de te faire manger. Vous marchez")
      plagesud()
  elif a == "pierre" and b == "papier":
      print("Vous avez perdu, et votre sentence est irrévocable!")
      plagesud()
  elif a == "pierre" and b == "pierre":
      print("Egalite. Alors on recommence !")
      denys_5()
  
  if a == "papier" and b == "pierre":
      print("Vous avez gagné.")
      print("Bravo vous remportez X rondis de bois ! : AH ! bien joué je ne m'attendais pas a ce que tu gagnes. Voici un bois bon courage pour la suite. Evite de te faire manger. Vous marchez")
      plagesud()
  elif a == "papier" and b == "ciseaux":
      print("Vous avez perdu, et votre sentence est irrévocable!")
      plagesud()
  elif a == "papier" and b == "papier":
      print("Egalite. Alors on recommence !")
      denys_5()
  
  if a == "ciseaux" and b == "papier":
      print("Vous avez gagne.")
      print("Bravo vous remportez X rondis de bois ! : AH ! bien joué je ne m'attendais pas a ce que tu gagnes. Voici un bois bon courage pour la suite. Evite de te faire manger. Vous marchez")
      plagesud()
  elif a == "ciseaux" and b == "pierre":
      print("Vous avez perdu, et votre sentence est irrévocable!")
      plagesud()
  elif a == "ciseaux" and b == "ciseaux":
      print("Egalite. Alors on recommence !")
      denys_5()


def montagne_2():
  print ("\nATu as rejoins le sommet de la montagne perdu, quelle belle vue ! Mais ne traine pas, des dangers rodent. Ce panorama t'offre la possibilité d'aller dans 3 endroits : la grotte, la cascade, et le volcan ! Ou décides-tu aller ? ")
  time.sleep(1)
  print ("""  A. Grotte
  B. Cascade
  C. Volcan""")
  choice = input("> ")
  if choice in answer_A:
    grotte_3()
  elif choice in answer_B:
    cascade_3()
  elif choice in answer_C:
    volcan_3()
  else:
    print (required)
    montagne_2()

def grotte_3():
  print ("\nTu t'enfonces de plus en plus dans la grotte et tu remarques une lumière au fond de la noirceur. Mais là où tu es, il fait très noir, beaucoup trop noir. Tu perds 1 rondins de bois dans ce noir si sombre. Un ange apparait devant toi, tu te frottes les yeux tu n'y crois cependant il est bien la. Cet ange te propose de t'emmener a l'endroit que tu désires. Marécage, Forêt ou Jungle ?")
  global rondins
  rondins = rondins - 1
  time.sleep(1)
  print ("""  A. Marécage
  B. Forêt
  C. Jungle""")
  choice = input("> ")
  if choice in answer_A:
    marecage_4()
  elif choice in answer_B:
    foret_1()
  elif choice in answer_C:
    jungle_4()
  else:
    print (required)
    grotte_3()

def cascade_3():
  print ("\nTu es a la cascade, quelle beauté. Tu remarques que ton odeur devient insupportable et attire les prédateurs quoi de mieux qu'une petite baignade. Cependant le courant est fort et tu finis dans la Rivière (Back to river)")
  time.sleep(1)
  riviere_2()

def volcan_3():
  rondins = rondins
  rondvolcan = random_number(2,3)
  rondins = rondins + rondvolcan
  print ("\nTu arrives au volcan, mais tu ressens quelque vibration sous tes pieds et commence à entendre le grondement de celui-ci. Tu ne sais pas d'où ça sort...mais voilà qu'arrives dans tes bras" + rondvolcan +" rondins de bois.")
  if rondins >= 7:
    win()
  print("""Un énorme oiseau passe au dessus de toi tu sautes pour l'attraper et de sortir de cette galère (1 chance sur 4).""") 
  time.sleep(1)
  rand = random_number(1,4)
  if rand == 1 :
    print("Quelle idée de sauter pour attraper un oiseau tu tombes et tu finis dans la lave, t'es mort. Tu n'es pas Indiana Jones.")
    time.sleep(1)
    mort()
  elif rand == 2 or rand == 3 or rand == 4:
    print("On t'emmène dans un lieu...plutôt cool.")
    denys_5()
  else:
    print (required)
    volcan_3()  

### TITLE SCREEN SELECTIONS FUNCTION ###
def title_screen_selections():
    """
    Creates options for the title screen
    """
    option = ""
    while option.lower not in ["help", "quitter", "jouer"]:
        print("Tappez jouer, help, ou quitter")
        option = input("> ")
        if option.lower() == "jouer":
            setup_game()
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "quitter":
            sys.exit()
            
####################            
### TITLE SCREEN ###                   
def title_screen():
    """
    Creates the title screen
    """
    #os.system('cls')#this was added in tutorial, not sure I need it
    print('\n################################')
    print('###   Bienvenue chez nous !  ###')      
    print('################################')      
    print(' -            .Jouer.           - ')
    print(' -            .Help.            - ')
    print(' -          .Quitter.           - ')
    print('################################\n') 
    title_screen_selections()

#################   
### HELP MENU ###   
def help_menu():
    """
    Creates the help menu
    """
    print('\n##################################################')
    print('################     Help Menu     ###############')  
    print('##################################################')
    print(' Type move or examine for each turn')      
    print(' If moving, type up, down, left, or right')
    print(' If examining, you may need to answer yes or no')
    print('##################################################\n')
    title_screen_selections()
  
####################
### GAME BACKEND ###
####################

### PLAYER SET UP ###

class player:
    def __init__(self):
        self.name = ''
myPlayer = player()
    
    
##############################        
##### GAME FUNCTIONALITY #####
##############################  

def setup_game():
    
    ## NAME COLLECTING ##
    texteffect("\nBonjour, jeune aventurier ! Comment tu t'appelles ?\n",0.02)
    player_name = input("> ")
    myPlayer.name = player_name.capitalize()
    texteffect("\nBonjour " + myPlayer.name +"\n",0.02)     
    texteffect("\nOn suppose que tu connais Koh-Lanta...et tu sais ici c'est un peu la même aventure. Tu préfères : Moundir l'agressif, Freddy l'ingénieur, ou Claude le héros ?\n",0.02)
    player_job = input("> ")
    myPlayer.job = player_job.capitalize()
    valid_jobs = ['Moundir', 'Freddy', 'Claude']
    if player_job in valid_jobs :
        texteffect("\nJe ne sais pas si tu as fais le bon choix..Mais bon, on verra bien par la suite.\n",0.02)
    
    texteffect("\nBienvenue dans ce RPG textuel, dans lequel tu vas devoir te déplacer, prendre des décisions, et t'adapter à la dure loin de la jungle...aussi. On ne peut pas t'en dire plus, mise à part de suivre les indications. (Et appuies sur A, B ou C afin de prendre tes décisions !) \n",0.015)
    time.sleep(2)
    intro()


    
title_screen()

