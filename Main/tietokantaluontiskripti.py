import mysql.connector

#Yhdistää tietokantaan ilman että lentopeli tietokanta on olemassa, olettaa että login on root/root
connection = mysql.connector.connect(
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
        "CREATE DATABASE IF NOT EXISTS lentopeli;",
        "USE lentopeli;",
        """CREATE TABLE IF NOT EXISTS game (
            game_ID INT AUTO_INCREMENT PRIMARY KEY,
            game_playername VARCHAR(100) NOT NULL,
            game_playerscore INT NOT NULL,
            game_playerinventory TEXT
        );""",
        """CREATE TABLE IF NOT EXISTS scoreboard (
            scoreboard_ID INT AUTO_INCREMENT PRIMARY KEY,
            scoreboard_playername VARCHAR(100) NOT NULL,
            scoreboard_finalscore INT NOT NULL
        );""",
        """CREATE TABLE IF NOT EXISTS airport (
            airport_ID INT AUTO_INCREMENT PRIMARY KEY,
            airport_name VARCHAR(255) NOT NULL,
            airport_country VARCHAR(100),
            airport_latitude DECIMAL(9, 6),
            airport_longitude DECIMAL(9, 6),
            airport_visited BOOLEAN DEFAULT FALSE
        );""",
        """INSERT INTO airport (airport_ID, airport_name, airport_country, airport_latitude, airport_longitude, airport_visited) VALUES 
        (1, 'London Heathrow Airport', 'GB', 51.4706, -0.461941, FALSE), 
        (2, 'Charles de Gaulle International Airport', 'FR', 49.012798, 2.55, FALSE), 
        (3, 'Amsterdam Airport Schiphol', 'NL', 52.308601, 4.76389, FALSE), 
        (4, 'Frankfurt am Main Airport', 'DE', 50.036249, 8.559294, FALSE), 
        (5, 'Rome–Fiumicino Leonardo da Vinci International Airport', 'IT', 41.804532, 12.251998, FALSE), 
        (6, 'Humberto Delgado Airport Lisbon Portela', 'PT', 38.7813, -9.13592, FALSE), 
        (7, 'Palma de Mallorca Airport', 'ES', 39.551701, 2.73881, FALSE), 
        (8, 'Athens Eleftherios Venizelos International Airport', 'GR', 37.936401, 23.9445, FALSE), 
        (9, 'Vienna International Airport', 'AT', 48.110298, 16.5697, FALSE), 
        (10, 'Zurich Airport', 'CH', 47.458056, 8.548056, FALSE), 
        (11, 'Copenhagen Kastrup Airport', 'DK', 55.617901, 12.656000, FALSE), 
        (12, 'Manchester Airport', 'GB', 53.349375, -2.279521, FALSE), 
        (13, 'Oslo Airport, Gardermoen', 'NO', 60.193901, 11.1004, FALSE), 
        (14, 'Brussels Airport', 'BE', 50.901402, 4.48444, FALSE), 
        (15, 'Stockholm-Arlanda Airport', 'SE', 59.651901, 17.918600, FALSE), 
        (16, 'Warsaw Chopin Airport', 'PL', 52.165699, 20.967100, FALSE), 
        (17, 'Budapest Liszt Ferenc International Airport', 'HU', 47.42976, 19.261093, FALSE), 
        (18, 'Helsinki Vantaa Airport', 'FI', 60.3172, 24.963301, FALSE), 
        (19, 'Tirana International Airport Mother Teresa', 'AL', 41.4147, 19.7206, FALSE), 
        (20, 'Keflavik International Airport', 'IS', 63.985001, -22.6056, FALSE), 
        (21, 'Riga International Airport', 'LV', 56.923599, 23.971100, FALSE)
        ON DUPLICATE KEY UPDATE airport_ID = airport_ID;"""
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
