import mariadb, random

connection = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    database='lentopeli',
    user='root',
    password='root',
    autocommit=True
)


def db_command(command):
    cursor = connection.cursor()
    cursor.execute(command)
    try:
        return cursor.fetchall()
    except:
        pass


# muokkaa pelaajan pistemäärää, yhteen- tai vähennyslasku
def modify_score(id, amount):
    db_command(f"UPDATE game SET game_playerscore = game_playerscore + {amount} WHERE game_ID = {id}")

#kertoo käyttäjän pisteet
def multiply_score(id, amount):
    score = db_command(f"SELECT game_playerscore FROM game WHERE game_ID = {id}")
    score = score[0][0] * amount
    db_command(f"UPDATE game SET game_playerscore = {round(score)} WHERE game_ID = {id}")


# arpoo lentokentän, jossa pelaaja ei ole käynyt
def select_airport():
    while True:
        i = random.randint(1, 21)
        try:
            db_command(f"SELECT airport_name FROM airport WHERE airport_ID = {i} AND airport_visited = FALSE")
        except:
            pass
        else:
            break
    return db_command(f"SELECT airport_name FROM airport WHERE airport_ID = {i} AND airport_visited = FALSE")


# arpoo 2 lentokenttää, jossa pelaaja ei ole käynyt
# voidaan käyttää tätä lentokentän valitsemiseen
def choose_airport():
    airport1 = select_airport()

    while True:
        airport2 = select_airport()

        if airport2 != airport1:
            break

    return airport1, airport2


# lisää pelaajan tietokantaan, aloittaa 1000 pisteellä
def add_player():
    if False:  # muuta falseksi, jos haluut syöttää oman nimen
        name = "test"
    else:
        name = input("Syötä nimi: ")

    db_command(f"INSERT INTO game (game_playername, game_playerscore) VALUES ('{name}', 1000)")