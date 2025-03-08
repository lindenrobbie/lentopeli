import db_modules, minigames

#pelisilmukka, toistuu 10 kertaa
for i in range(10):
    #haetaan 2 satunnaista lentokenttää, joissa pelaaja ei ole käynyt
    choice = db_modules.choose_airport() 
    airport1 = choice[0]
    airport2 = choice[1]

    #pelaaja valitsee lentokentän
    query = minigames.query("Mihin maahan haluaisit matkustaa?", 
                    [f"1: {airport1[0][1]}", f"2: {airport2[0][1]}"], 
                    ["1", "2"])
    
    #current_pos sisältää valitun kentän airport_id, airport_name ja airport_visited
    #näyttää esim. [(1, 'London Heathrow Airport', FALSE)]
    current_pos = airport1 if query == "1" else airport2

    #päivitetään valittu lentokenttä käydyksi sekä pelaajan sijainti valittuun lentokenttään
    db_modules.travel_to(current_pos[0][0], 1) #parametreina siis lentokentän airport_id ja game_id, joka on aina 1 (jos resetoidaan db jokaisen pelin lopussa)
    

    #tähän väliin vois lisätä komentoja esim. pisteiden tarkistamiseen
    #sitten jatkaa painamalla entteriä

    #seuraavaksi alkaa minipeli
    #voit yhdistää minipelit ja vastaavat lentokentät joko tietokannassa tai koodissa kirjastolla
    #kaikki minipelit ovat nyt minigames.py tiedostossa. nimet vaihdettu vastaaviksi lentokentiksi (esim helsinki-vantaa kentän minipeli on helsinki() ) selkeyden vuoksi. 
    #osa minipeleistä on vielä tyhjiä ja printtaavat vaan kentän nimen

    #minipelin jälkeen muokataan pelaajan pistemäärää modify_score tai multiply_score funktioilla
    #on parempi tehdä täällä kuin jokaisessa minipelissä erikseen
    #muokataan minipelejä myöhemmin niin, että ne palauttaa pistemäärän / kertoimen



#visited=9
#while visited <10:
#    nextairport= (db_modules.select_airport())
#    id=nextairport[0][0]
#    print(id)
#    visited +=1
#    db_modules.db_command(f'UPDATE airport SET airport_visited = 1 WHERE airport_id = {id};')
#    airportgame={10:'minipelitville.minigame_bank()',15:'minipelitville.minigame_stockholm()'}
#    minigame=airportgame[id]

