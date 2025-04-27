import sqlite3

connection = sqlite3.connect("tasks.db")
cursor = connection.cursor()

cursor.execute(
    '''
    create table if not exists tasklist(id integer primary key autoincrement, task text not null)
'''
)

connection.commit()
connection.close()

print("Database and table created successfully!")

