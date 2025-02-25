import db_modules

#palauttaa tietokannan alkuperäiseen muotoon

db_modules.db_command("delete from scoreboard")
db_modules.db_command("delete from game")
db_modules.db_command("alter table game auto_increment = 0")
db_modules.db_command("update airport set airport_visited = False")