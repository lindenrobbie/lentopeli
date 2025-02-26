from tk_moduulit import hae_tietokannasta

def print_scoreboard():

    komento = 'SELECT scoreboard_playername, scoreboard_finalscore FROM scoreboard ORDER BY scoreboard_finalscore DESC LIMIT 10;'

    results = hae_tietokannasta(komento)

    print("")
    print("===== Leaderboard =====")

    if results:


        print("")

        rank = 1

        for row in results:
            name, score = row
            print(f'{rank} | {name} | {score}')
            rank += 1
    else:
        print("")
        print("Näyttää tyhjältä...")
print_scoreboard()