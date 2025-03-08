
import mariadb,tietokantaluontiskripti,db_modules, ascii_art,pygame


connection = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    database='lentopeli',
    user='root',
    password='tietotekniikka',
    autocommit=True
)
db_modules.add_player()
command = "SELECT game_playername FROM game WHERE game_ID = (SELECT MAX(game_ID) FROM game)"
db_modules.db_command(command)
result = db_modules.db_command(command)
for i in result:
    print ("Tervetuloa pelaamaan Amazing flight Race peliä!:",i)



