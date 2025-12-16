import sqlite3

#Initalizes the database
def init_database():
# Connects to file using SQLite!
    connection = sqlite3.connect('EscapeTheLab.db')
    data_base = connection.cursor() # Does the commands

    # Creates table if dosent already exist (SQL format)
    data_base.execute('''
        CREATE TABLE IF NOT EXISTS highscores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT,
            score INTEGER
        )
    ''')
    connection.commit() # Saves changes to database
    connection.close() # closes the database


def save_scores(player_name, score):
    connection = sqlite3.connect('EscapeTheLab.db')
    data_base = connection.cursor()

    data_base.execute(
        "INSERT INTO highscores (player_name, score) VALUES(?, ?) ",
        (player_name, score)
    )

    connection.commit()
    connection.close()

def get_highscores(limit = 7):
    connection = sqlite3.connect('EscapeTheLab.db')
    data_base = connection.cursor()

    data_base.execute('''
        SELECT player_name, score
        FROM highscores
        ORDER BY score DESC
        LIMIT ?
    ''', (limit,))

    score = data_base.fetchall() # gets all the scores
    connection.close()
    return score