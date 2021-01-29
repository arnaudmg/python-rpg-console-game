### IMPORT ###
import cmd 
import textwrap
import sys
import os
import time
import random 

### TEXT EFFECT FUNCTION ###
def texteffect(string, n = 0.04):

    q = string
    for character in q:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(n)

### Random number 

def random_number(x,n):
  d = random.randint(x,n)
  return d

### Variable pour les rondins de bois qui s'additionnent
rondins = 0

## Jeu du Pierre Feuille Ciseau 

def choix_utilisateur():
    joueur = input("\nPierre, Papier ou Ciseaux ? (à écrire sans majuscule !)\n")
    while joueur not in ["pierre","papier","ciseaux"]:
        joueur = input("Pierre, Papier ou Ciseaux ? (à écrire sans majuscule !)\n")
    return(joueur)

def choix_ordinateur():
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

def inventaire():
  texteffect("Vous avez " + str(rondins) + " rondins dans votre inventaire. Pour rappel, il vous en faut 7 pour pouvoir vous enfuir!",.02)

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_I = ["I", "i"]
yes = ["Y", "y", "yes", "oui"]
no = ["N", "n", "no", "oui"]

required = ("\nOn a dit A, B ou C, pas d'autres choses !\n")

####################
###    GAME      ###
####################

def intro():
  texteffect("\n" + myPlayer.name + " vous vous réveillez sans souvenirs, vous êtes seul sur une plage. Voulez-vous bronzer ou aller dans la forêt ?\n",.02)
  time.sleep(1)
  print ("""  A. Explorer vers le nord, et s'engonfrer dans la forêt
  B. Bronzer sur la plage...même si il n'y a pas le (tri) cocktail""")
  choice = input("> ") 
  if choice in answer_A:
    foret_1()
  elif choice in answer_B:
    texteffect("\nVous avez perdu une journée, mais avancée quand-même dans la forêt. Il faut pas abuser " + myPlayer.name + "!",.02)
    time.sleep(1)
    foret_1()
  else:
    print (required)
    intro()

def foret_1():
  texteffect("\nAprès quelques minutes de marche vous vous enfoncez dans la foret. Vous apercevez un sommet montagneux et entendez un cours d'eau. Où voulez-vous aller " + myPlayer.name + "?\n")
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

def riviere_2():
  texteffect("\nAprès des heures vous arrivez au cours d'eau, félicitations ! Étant toujours prisonnier de cette nature, une jungle et un marecage barrent ton chemin. Mais quel chemin veux-tu tenter de prendre pour t'en sortir et poursuivre ta quête ?\n")
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
  texteffect("\nBienvenue dans la jungle ! Il commence à se faire tard. Il s'avère que tu as trouvé " + str(rondjungle) + " rondins de bois, veux-tu en profiter pour aller te faire un feu ou te réfugier dans une cabane un peu plus loin ?\n")
  texteffect("Vous avez " + str(rondins) + " rondins dans votre inventaire. Pour rappel, il vous en faut 7 pour pouvoir vous enfuir!\n")
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
  texteffect("\nTu te poses tranquillement dans la cabane MAIS ATTENTION !!!! Une tarentule arrive. Decides-tu de l'affronter ou de prendre tes jambes à ton cou et de t'enfuir ?\n")
  time.sleep(1)
  texteffect("""  A. Oui
  B. Non
  I. Inventaire""")
  choice = input("> ")
  if choice in answer_A:
    randAraignée = random_number(1,2)
    if randAraignée == 1:
      print("La fuite aurait été une meilleure option... La morsure d'araignée t'as tué dans d'atroces souffrances. La nature restera plus forte.")
      mort()
    else:
      print("Pas de quoi avoir peur, c'etait une petite araignée. Après un jour de repos, tu vas en direction d'un feu de camp !")
      feu_5()
  elif choice in answer_B:
    print("Fragile, tu vas pas survir longtemps toi... tu es retourné à la plage.")
    intro()
  elif choice in answer_I:
    inventaire()
    cabane_5()
  else:
    print (required)
    cabane_5()

def feu_5():
  texteffect("\nVous n'êtes pas tres discret et vous entendez des bruits bizarre toute la nuit. Mais le feu vous a réchauffer et vous êtes assez réveiller pour continuer votre marche. Au bout de quelques kilomètres un Maya vous a reperé et vous emmène dans sa tribu...\n")
  time.sleep(2)
  maya_6()

def maya_6():
  texteffect("\nDès votre arrivée les Mayas vous proposent un marché : Vous restez 2 jours en échange d'1 rondins de bois OU BIEN vous continuez votre route.\n")
  time.sleep(2)
  print ("""  A. Accepter le deal avec le Maya
  B. Continuer son chemin vers une direction qui nous intrigue
  I. Inventaire""")
  choice = input("> ")
  if choice in answer_A:
    texteffect("\nChoix difficile, mais pourquoi pas, on voit que vous voulez gagner.")
    global rondins
    rondins = rondins
    rondins = rondins + 1 
    texteffect("\nMaintenant, il faut se remettre en route ! Et en plus, le maya vous guide..")
    plagesud()
  elif choice in answer_B:
    plagesud()
  elif choice in answer_I:
    inventaire()
    maya_6()
  else:
    print (required)
    maya_6()

def plagesud():
  global rondins
  rondins = rondins
  rondins = rondins + 1
  texteffect("\nVoici quelques jours que vous êtes sur cette île maudite. Vous découvrez une belle plage, sur laquelle vous trouvez 1 rondin de bois, par miracle.")
  texteffect("Vous regardez le coucher de soleil malheureusement votre moment est pertubé par un bruit d'ambiance qui vient du Nord. Mais que se passe-t-il ? C'est ainsi que vous découvrez.... UN BAR DANSANT ?!?!")
  if rondins >= 7:
    win()
  time.sleep(2)
  bar_5()

def bar_5():
  texteffect("\nVous ne vous posez pas de question, et vous vous accoudez au bar. Vous choisissez de prendre de l'eau ou un martini ?\n")
  time.sleep(2)
  print ("""  A. Eau
  B. Alcool
  I. Inventaire""")
  choice = input("> ")
  if choice in answer_A:
    ##rajouter rondins je pense!
    texteffect("Sans mémoire vous vous réveillez en haut d'une montagne . Vous étiez dans le coma. Dans ce bar, on a certainement dû se jouer de vous. Vous avez perdu 1 jour, mais tout va bien pour vous...forte heureusement")
    montagne_2()
  elif choice in answer_B:
    texteffect("Vous vous réveillez sur la plage de depart, nu, dépouillé et avec une gueule de bois monstrueuse. Vous perdez 2 rondins de bois. Allez, courage")
    global rondins
    rondins = rondins - 2
    intro()
  elif choice in answer_I:
    inventaire()
    bar_5()
  else:
    print (required)
    bar_5()

def ruines_5():
  texteffect("\nCes ruines cachent bien leur jeu. De nombreuses choses ont été détruites sauf un temple, un bar et tu aperçois quelqu'un. Que décides-tu de faire ?\n ")
  time.sleep(1)
  texteffect("""  A. Temple
  B. Denys
  C. Bar
  I. Inventaire""")
  choice = input("> ")
  if choice in answer_A:
    temple_5()
  elif choice in answer_B:
    denys_5()
  elif choice in answer_C:
    bar_5()
  elif choice in answer_I:
    inventaire()
    ruines_5()
  else:
    print (required)
    ruines_5()

def marecage_4():
  global rondins
  rondins = rondins
  rondmarecage = random_number(1,3)
  rondins = rondins + rondmarecage
  texteffect("\nL'odeur est nauséabonde, et tu en fais un malaise. Mais dans cette horreur, tu y trouves ton bonheur " + str(rondmarecage) + " rondins de bois.")
  if rondins >= 7:
    win()
  texteffect("Tu décides de ne pas trainer et te diriges vers des ruines que tu apercois un peu plus loin. Ce passage t'as énormément fatigué.")
  time.sleep(3)
  texteffect(""" Tu n'as pas le choix, tu avances tout droit, tu n'as pas d'autres issues""")
  ruines_5()



def temple_5():
  texteffect("\nLe temple est magnifique mais pour y accéder tu dois traverser un pont qui parait très fragile. Tu serres les fesses pour pas qu'il ne casse ! Il fallait de l'aventure...alors tu as une chance sur 2 qu'il casse !\n")
  time.sleep(2)
  randPont = random_number(1,2)
  if randPont == 1:
    texteffect("\nC'est passé ! Ouf !")
    maya_6()
  else:
    texteffect("\nMalheuresement...tu es tombé. Allez, repars de la rivière, ça te fera du bien.")
    riviere_2()  

def denys_5():
  global rondins
  texteffect("\nEn te rapprochant de cette personne tu te rends compte qu'il s'agit de Denys Brognard ! Tu ne sais plus si c'est la fatigue ou la folie mais il te propose une épreuve...\n")
  time.sleep(1)
  texteffect("""\nBonsoir à toi, jeune aventurier. Tu vas devoir m'affronter à une épreuve appelé "pierre, feuille, ciseaux", c'est tout nouveau, c'est produit par TF1, tu vas voir c'est une super épreuve. Si tu gagnes tu remportes un rondin de bois, si tu perds tu en perds un ! Concentre toi cela pourrait t'aider dans ta quête".""")
  a = choix_utilisateur()
  b = choix_ordinateur()
  if a == "pierre" and b == "ciseaux":
      print("Vous avez gagné. Vous gagnez de l'expérience (+12xp) et vous devenez plus fort, et réduisez vos chances de perdre aux jeux de chance dans la jungle !")
      print("Bravo vous remportez 1 rondis de bois ! : AH ! bien joué je ne m'attendais pas a ce que tu gagnes. Voici un bois bon courage pour la suite. Evite de te faire manger. Vous marchez.")
      rondins = rondins + 1
      plagesud()
  elif a == "pierre" and b == "papier":
      print("Vous avez perdu, et votre sentence est irrévocable! Vous perdez de l'expérience (-12xp) et vous devenez plus fort, et réduisez vos chances de perdre aux jeux de chance dans la jungle ! Tu perds 1 rondin en plus...cadeau.")
      rondins = rondins - 1
      plagesud()
  elif a == "pierre" and b == "pierre":
      print("Egalite. Alors on recommence !")
      denys_5()
  
  if a == "papier" and b == "pierre":
      print("Vous avez gagné. Vous gagnez de l'expérience (+12xp) et vous devenez plus fort, et réduisez vos chances de perdre aux jeux de chance dans la jungle !")
      print("Bravo vous remportez 1 rondis de bois ! : AH ! bien joué je ne m'attendais pas a ce que tu gagnes. Voici un bois bon courage pour la suite. Evite de te faire manger. Vous marchez.")
      rondins = rondins + 1
      plagesud()
  elif a == "papier" and b == "ciseaux":
      print("Vous avez perdu, et votre sentence est irrévocable! Vous perdez de l'expérience (-12xp) et vous devenez plus fort, et réduisez vos chances de perdre aux jeux de chance dans la jungle ! Tu perds 1 rondin en plus...cadeau.")
      rondins = rondins - 1
      plagesud()
  elif a == "papier" and b == "papier":
      print("Egalite. Alors on recommence !")
      denys_5()
  
  if a == "ciseaux" and b == "papier":
      print("Vous avez gagné. Vous gagnez de l'expérience (+12xp) et vous devenez plus fort, et réduisez vos chances de perdre aux jeux de chance dans la jungle !")
      print("Bravo vous remportez 1 rondis de bois ! : AH ! bien joué je ne m'attendais pas a ce que tu gagnes. Voici un bois bon courage pour la suite. Evite de te faire manger. Vous marchez.")
      rondins = rondins + 1
      plagesud()
  elif a == "ciseaux" and b == "pierre":
      print("Vous avez perdu, et votre sentence est irrévocable! Vous perdez de l'expérience (-12xp) et vous devenez plus fort, et réduisez vos chances de perdre aux jeux de chance dans la jungle ! Tu perds 1 rondin en plus...cadeau.")
      rondins = rondins - 1
      plagesud()
  elif a == "ciseaux" and b == "ciseaux":
      print("Egalite. Alors on recommence !")
      denys_5()


def montagne_2():
  texteffect("\nATu as rejoins le sommet de la montagne perdu, quelle belle vue ! Mais ne traine pas, des dangers rodent. Ce panorama t'offre la possibilité d'aller dans 3 endroits : la grotte, la cascade, et le volcan ! Ou décides-tu aller ?\n ")
  time.sleep(1)
  print ("""  A. Grotte
  B. Cascade
  C. Volcan
  I. Inventaire""")
  choice = input("> ")
  if choice in answer_A:
    grotte_3()
  elif choice in answer_B:
    cascade_3()
  elif choice in answer_C:
    volcan_3()
  elif choice in answer_I:
    inventaire()
    montagne_2()
  else:
    print (required)
    montagne_2()

def grotte_3():
  texteffect("\nTu t'enfonces de plus en plus dans la grotte et tu remarques une lumière au fond de la noirceur. Mais là où tu es, il fait très noir, beaucoup trop noir. Tu perds 1 rondins de bois dans ce noir si sombre. Un ange apparait devant toi, tu te frottes les yeux tu n'y crois cependant il est bien la. Cet ange te propose de t'emmener a l'endroit que tu désires. Marécage, Forêt ou Jungle ?\n")
  global rondins
  rondins = rondins - 1
  time.sleep(1)
  print ("""  A. Marécage
  B. Forêt
  C. Jungle
  I. Inventaire""")
  choice = input("> ")
  if choice in answer_A:
    marecage_4()
  elif choice in answer_B:
    foret_1()
  elif choice in answer_C:
    jungle_4()
  elif choice in answer_I:
    inventaire()
    maya_6()
  else:
    print (required)
    grotte_3()

def cascade_3():
  texteffect("\nTu es a la cascade, quelle beauté. Tu remarques que ton odeur devient insupportable et attire les prédateurs quoi de mieux qu'une petite baignade. Cependant le courant est fort et tu finis dans la Rivière (Back to river)")
  time.sleep(1)
  riviere_2()

def volcan_3():
  global rondins
  rondins = rondins
  rondvolcan = random_number(1,2)
  rondins = rondins + rondvolcan
  texteffect("\nTu arrives au volcan, mais tu ressens quelques vibrations sous tes pieds et commence à entendre le grondement de celui-ci. Tu ne sais pas d'où ça sort...mais voilà qu'arrives dans tes bras" + str(rondvolcan) +" rondins de bois..comme par magie ?")
  if rondins >= 7:
    win()
  texteffect("""Un énorme oiseau passe au dessus de toi tu sautes pour l'attraper et de sortir de cette galère. Bon, il fallait de l'aventure, alors tu 1 chance sur 4 de succomber ici.""") 
  time.sleep(1)
  rand = random_number(1,4)
  if rand == 0 :
    texteffect("Quelle idée de sauter pour attraper un oiseau tu tombes et tu finis dans la lave, t'es mort. Tu n'es pas Indiana Jones.")
    time.sleep(1)
    mort()
  elif rand == 2 or rand == 3 or rand == 4 or rand == 5 or rand == 6:
    texteffect("Tu as de la chance, et tu t'en sors. On t'emmène dans un lieu...plutôt cool, du coup.")
    denys_5()
  else:
    print (required)
    volcan_3()  

### TITLE SCREEN SELECTIONS FUNCTION ###
def title_screen_selections():

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
#################  
def help_menu():
    print('\n##################################################')
    print('################     Help Menu     ###############')  
    print('##################################################')
    print(' Tape A, B ou C à chaque choix possible ')      
    print(' Il te faut trouver 7 rondins et survivre à tout \n ce qui se mettra sur ton passage')
    print(' Bon courage, et amuses-toi bien !')
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
#####     GAME SETUP     #####
##############################  

def setup_game():
    
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