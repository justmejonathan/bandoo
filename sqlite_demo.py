import sqlite3
#from app import gls
conn = sqlite3.connect('glasses.db')

c = conn.cursor()

#c.execute("""create table glasses (
#	        id Integer,
#	        name Varchar (255), 
#	        counter Integer
#       )""")

#c.execute("INSERT INTO glasses VALUES (4, 'Beach Vibes Baby', 0)")

#gls = artist + color + drink

#c.execute('SELECT * FROM glasses WHERE name="Beach Vibes Baby"')
#def update_counter (id, counter):
#    with conn:
c.execute('UPDATE glasses SET counter = counter +1 WHERE id = 1 ')

c.execute(('SELECT * FROM glasses WHERE id = 1'))
#only returns one row:
print(c.fetchall())
#print(gls)

conn.commit()

conn.close()