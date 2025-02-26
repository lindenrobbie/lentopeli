#import random
#def donalduck():
   # return
#question = input(print ("Lentokentän kahviossa edessä olevalta lapselta puuttuu pillimehusta rahaa 2 euroa.\nHaluatko antaa puuttuvan rahan?"
  #     " Kyllä, Ei: ")).lower()
#if question =="kyllä":
#    random= random.randint(1,10)
 #   if random ==1:
  #      print("Tehtävä epäonnistui, pillimehu tippui lapsen kädestä maahan ja meni rikki ;(")
 #   else:
 #       print("Saat palkinnoksi perheeltä kiiltävän Aku Ankka pinssin")
#
#if question =="ei":
  #  print("Etenet seuraavaan paikkaan menettämättä rahaa mutta kuulet surullisen lapsen itkua!!! ")

import random
def carddraw():
    return
print("Vieressä istuva aussi Hugh Jackman on tylistymässä kuoliaaksi ja "
      "haastaa sinut pelaamaan kortin vetoa, isoin kortti voittakoon!")
player1 =random.randint(2,14)
player2 =random.randint(2,14)
if player1==player2:
    coin=input(print("Ratkaistaan voittaja kolikolla, kruuna vai klaava?:  "))
    if coin=="kruuna":
        coin=1
    if coin=="klaava":
        coin=2
    random2=random.randint(1,2)
    if coin==random2:
        print("Arvasit oikein ja voitit!!")
    else:
        print("Voihan mielipaha arvasit väärin, hävisit tolle charmantille aussille!")
if player1>player2:
    print(f"Hugh Jackmanin kortti: {player1} sinun korttisi {player2}")
    print(f"Hugh Jackman voitti kortilla: {player1}. Äläkä ala mököttää, tapasit sentään charmantin julkkiksen ^_^  !")
else:
    print(f"Pelaaja (tähän pelaajan nimimerkki) voitti Hugh Jackmanin.\nPalkinnoksi sait wolverinen muoviset raateluterät. Oiva lahja siskon pojalle! Pisteesi kerrotaan kertoimella 1.2!")

