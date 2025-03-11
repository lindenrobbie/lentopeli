import mariadb

#Yhdistää tietokantaan ilman että lentopeli tietokanta on olemassa, olettaa että login on root/root
connection = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',
    autocommit=True
)

# db_modules:ista, syöttää SQL query:n
def db_command(command):
    cursor = connection.cursor()
    cursor.execute(command)
    return

# Kaikki tarvittavat SQL query:t pelin tietokannan asennukseen

def install():
    return [
        """CREATE DATABASE lentopeli;

    USE lentopeli;

    CREATE TABLE airport (
        airport_ID INT NOT NULL PRIMARY KEY,
        airport_name VARCHAR(255) NOT NULL,
        airport_visited BOOLEAN DEFAULT FALSE
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

    CREATE TABLE game (
        game_ID INT AUTO_INCREMENT PRIMARY KEY,
        game_playername VARCHAR(100) NOT NULL,
        game_playerscore INT NOT NULL,
        game_playerpos INT NOT NULL,
        FOREIGN KEY (game_playerpos) REFERENCES airport (airport_ID)
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

    CREATE TABLE scoreboard (
        scoreboard_ID INT AUTO_INCREMENT PRIMARY KEY,
        scoreboard_playername VARCHAR(100) NOT NULL,
        scoreboard_finalscore INT NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

    INSERT INTO airport (airport_ID, airport_name, airport_visited)
    VALUES
    (1, 'London Heathrow Airport', FALSE),
    (2, 'Charles de Gaulle International Airport', FALSE),
    (3, 'Amsterdam Airport Schiphol', FALSE),
    (4, 'Frankfurt am Main Airport', FALSE),
    (5, 'Rome–Fiumicino Leonardo da Vinci International Airport', FALSE),
    (6, 'Humberto Delgado Airport Lisbon Portela', FALSE),
    (7, 'Palma de Mallorca Airport', FALSE),
    (8, 'Athens Eleftherios Venizelos International Airport', FALSE),
    (9, 'Vienna International Airport', FALSE),
    (10, 'Zurich Airport', FALSE),
    (11, 'Copenhagen Kastrup Airport', FALSE),
    (12, 'Manchester Airport', FALSE),
    (13, 'Oslo Airport, Gardermoen', FALSE),
    (14, 'Brussels Airport', FALSE),
    (15, 'Stockholm-Arlanda Airport', FALSE),
    (16, 'Warsaw Chopin Airport', FALSE),
    (17, 'Budapest Liszt Ferenc International Airport', FALSE),
    (18, 'Helsinki Vantaa Airport', FALSE),
    (19, 'Tirana International Airport Mother Teresa', FALSE),
    (20, 'Keflavik International Airport', FALSE),
    (21, 'Riga International Airport', FALSE);

    ALTER DATABASE lentopeli CHARACTER SET utf8 COLLATE utf8_unicode_ci;"""
    ]

#Toistaa kunnes syöttää tyhjän kentän, A = Asentaa, P = Poistaa

while True:

    request = input('Haluatko resetoida, asentaa, vai poistaa tietokannan?: A/P ')

    #Tyhjä kenttä, lopettaa ohjelman
    if request == '':
        break

    #Asennus
    elif request == 'A': #
        for query in install():
            db_command(query)
        print("Tietokanta on nyt asennettu.")

    #Poisto
    elif request == 'P':
        db_command("DROP DATABASE IF EXISTS lentopeli;")
        print("Tietokanta on nyt poistettu.")

    #Jos syöte ei oo A/P tai ei mitään niin toistorakenne jatkuu
    else:
        print("Syötä validi pyyntö (A/P)")
