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

print_scoreboard()