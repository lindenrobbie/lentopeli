import db_modules
import minigames
import reset_db

#Arpoo uuden kentän id:n 10 kertaa ja asettaa tietokantaan sen id:n arvoksi 1
visited=9
while visited <10:
    nextairport= (db_modules.select_airport())
    id=nextairport[0][0]
    visited +=1
    db_modules.db_command(f'UPDATE airport SET airport_visited = 1 WHERE airport_id = {id};')

#Käyttää sanakirjaa laukaistakseen jokaiseen kenttään liitetyn minipelin
    airportgame={2:minigames.words(),3:minigames.bike(),4:minigames.frankfurt(),7:minigames.delgado(),8:minigames.late(),9:minigames.roulette(),10:minigames.bank(),11:minigames.kastrup(),12:minigames.carddraw(),15:minigames.stockholm(),18:minigames.donalduck(),19:minigames.pummi()}
    minigame=airportgame[id]

