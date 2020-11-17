import sqlite3
#from app import gls


conn = sqlite3.connect('glasses.db')
c = conn.cursor()



    
#print(glasses)
conn.commit()
conn.close()