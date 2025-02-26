import db_modules

def print_scoreboard():

    command = 'SELECT scoreboard_playername, scoreboard_finalscore FROM scoreboard ORDER BY scoreboard_finalscore DESC LIMIT 10;'

    results = db_modules.db_command(command)

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