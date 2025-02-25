import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='lentopeli',
         user='root',
         password='root',
         autocommit=True,
         collation='utf8mb3_unicode_ci'
         )

def hae_tietokannasta(komento):

    kursori = yhteys.cursor()
    kursori.execute(komento)
    tulos = kursori.fetchall()

    return tulos

