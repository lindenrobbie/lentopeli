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

#Käyttää sanakirjaa laukaistakseen jokaiseen kenttään liitetyn minipelin
    airportgame={2:minigames.words(),3:minigames.bike(),4:minigames.frankfurt(),7:minigames.delgado(),8:minigames.late(),9:minigames.roulette(),10:minigames.bank(),11:minigames.kastrup(),12:minigames.carddraw(),15:minigames.stockholm(),18:minigames.donalduck(),19:minigames.pummi()}
    minigame=airportgame[id]