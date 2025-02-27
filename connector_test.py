import mariadb

connection = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    database='lentopeli',
    user='root',
    password='root',
    autocommit=True
)

"""def db_command(command):
    cursor = connection.cursor()
    cursor.execute(command)

    # Check if the query is a SELECT query (which will return a result set)
    if command.strip().upper().startswith("SELECT"):
        results = cursor.fetchall()  # Call fetchall() only for SELECT queries
        if results == []:
            return None  # If the result is an empty list, return None
        else:
            return results  # Return the fetched results
    else:
        # If it's not a SELECT query (e.g., INSERT, UPDATE, DELETE), don't call fetchall
        return None  # No results for queries like INSERT, UPDATE, DELETE

command = input('Syötä SQL query: ')

i = db_command(command)
print(i)"""

def db_command(command):
    cursor = connection.cursor()
    cursor.execute(command)
    try:
        return cursor.fetchall()  # ei palauta mitään jos käyttää esim. INSERT komentoo
    except:
        pass

command = input('Syötä SQL query: ')

i = db_command(command)
print(i)