import db_modules
import minipelitville
import reset_db
visited=9
while visited <10:
    nextairport= (db_modules.select_airport())
    id=nextairport[0][0]
    print(id)
    visited +=1
    db_modules.db_command(f'UPDATE airport SET airport_visited = 1 WHERE airport_id = {id};')
    airportgame={10:'minipelitville.minigame_bank()',15:'minipelitville.minigame_stockholm()'}
    minigame=airportgame[id]

