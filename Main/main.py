#Tässä on main class tiedosto lentopelille

import ascii_art, db_modules, scoreboard, minigames, sound, mariadb

db_modules.db_command("update airport set airport_visited = False")

db_modules.add_player()

command = "SELECT game_playername FROM game WHERE game_ID = (SELECT MAX(game_ID) FROM game)"
db_modules.db_command(command)
result = db_modules.db_command(command)
for i in result:
    print ("\nTervetuloa pelaamaan Amazing flight Race peliä",i[0],"!")


#Minipelien sanakirja
airportgame={1:minigames.london,2:minigames.charles,3:minigames.amsterdam,4:minigames.frankfurt,5:minigames.rome,6:minigames.humberto,7:minigames.mallorca,8:minigames.athens,9:minigames.vienna,10:minigames.zurich,11:minigames.copenhagen,12:minigames.manchester,13:minigames.oslo,14:minigames.brussels,15:minigames.stockholm,16:minigames.warsaw,17:minigames.budapest,18:minigames.helsinki,19:minigames.tirana,20:minigames.keflavik,21:minigames.riga}
#pelisilmukka, toistuu 10 kertaa
for i in range(10):
    maxid = db_modules.db_command("SELECT MAX(game_ID) FROM game")
    #haetaan 2 satunnaista lentokenttää, joissa pelaaja ei ole käynyt
    choice = db_modules.choose_airport() 
    airport1 = choice[0]
    airport2 = choice[1]
    #print(airport1)
    #print(airport2)
    #pelaaja valitsee lentokentän
    query = minigames.nodashquery("\nMihin maahan haluaisit matkustaa?",
                    [f"\n\033[36m1\033[39m: {airport1[0][1]}", f"\n\033[36m2\033[39m: {airport2[0][1]}\n"],
                    ["1", "2"])
    
    #current_pos sisältää valitun kentän airport_id, airport_name ja airport_visited
    #näyttää esim. [(1, 'London Heathrow Airport', FALSE)]
    current_pos = airport1 if query == "1" else airport2

    #päivitetään valittu lentokenttä käydyksi sekä pelaajan sijainti valittuun lentokenttään
    db_modules.travel_to(current_pos[0][0], maxid[0][0]) 

    #tähän väliin vois lisätä komentoja esim. pisteiden tarkistamiseen

    #sitten jatkaa painamalla entteriä

    #seuraavaksi alkaa minipeli
    #voit yhdistää minipelit ja vastaavat lentokentät joko tietokannassa tai koodissa kirjastolla
    #kaikki minipelit ovat nyt minigames.py tiedostossa. nimet vaihdettu vastaaviksi lentokentiksi (esim helsinki-vantaa kentän minipeli on helsinki() ) selkeyden vuoksi. 
    #osa minipeleistä on vielä tyhjiä ja printtaavat vaan kentän nimen

    # Käyttää sanakirjaa laukaistakseen jokaiseen kenttään liitetyn minipelin
    minigame =airportgame[current_pos[0][0]]()

    #Luo maxid muuttujan ja antaa sen parametrinä modify_scorelle ja lisää/poistaa pisteet
    db_modules.modify_score(maxid[0][0],minigame[1])

    #Tulostaa uusimman tietokannan pelaajan nykyiset pisteet
    points = db_modules.db_command("SELECT game_playerscore FROM game WHERE game_ID = (SELECT MAX(game_ID) FROM game)")
    points = points[0][0]
    print(f'Pisteesi: {points}')

    #Jatka painamalla enter
    minigames.enter_continue()



def store_final_score():

    playerresult = db_modules.db_command("SELECT game_playername, game_playerscore FROM game WHERE game_ID = (SELECT MAX(game_ID) FROM game)")

    playername, playerscore = playerresult[0]

    db_modules.db_command(f"INSERT INTO scoreboard (scoreboard_playername, scoreboard_finalscore) VALUES ('{playername}', {playerscore})")


import db_modules

def print_scoreboard():

    command = 'SELECT scoreboard_playername, scoreboard_finalscore FROM scoreboard ORDER BY scoreboard_finalscore DESC LIMIT 10;'

    results = db_modules.db_command(command)

    print("")
    print("===== \033[93mPISTETAULUKKO\033[0m =====")

    if results:

        print("")

        rank = 1

        for rank, (name, score) in enumerate(results, start=1):
            medal = {1: "\033[33m🥇 ", 2: "\033[37m🥈 ", 3: "\033[35m🥉 "}.get(rank, "   ")
            print(f"{medal}{rank}. {name} - {score} points\033[0m")
    else:
        print("")
        print("Näyttää tyhjältä...")

store_final_score()

print_scoreboard()

