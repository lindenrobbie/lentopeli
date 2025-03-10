import mariadb, db_modules

conn = mariadb.connect(
    user="root",
    password="root",
    host="localhost",
    database="lentopeli"
)
cursor = conn.cursor()

def store_final_score():
    try:
        # Hakee pelaajadatat game pöydästä
        cursor.execute("SELECT game_playername, SUM(game_playerscore) FROM game GROUP BY game_playername")
        player_scores = cursor.fetchall()

        # Tallentaa tiedot scoreboard pöytään
        for player_name, total_score in player_scores:
            cursor.execute("""
                INSERT INTO scoreboard (scoreboard_playername, scoreboard_finalscore)
                VALUES (%s, %s)
            """, (player_name, total_score))

        #tyhjentää game pöydän rivit (resettaa game pöydän)
        cursor.execute("TRUNCATE TABLE game")

        conn.commit()
        print("\nPisteesi ovat tallentuneet taulukkoon!")
    except mariadb.Error as e:
        print(f"Error: {e}") #debuggausta varten
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

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