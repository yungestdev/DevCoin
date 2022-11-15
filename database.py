import sqlite3 

class Crypto:

    def __init__(self):
        self.__conn = sqlite3.connect("crypto.db")
        self.__c = self.__conn.cursor()

        self.__c.execute("""
            CREATE TABLE IF NOT EXISTS blockchain(
                numver VARCHAR(10), 
                hash VARCHAR(64),
                previous VARCHAR(64),
                data VARCHAR(100),
                nonce VARCHAR(15)
            )
        """)

        self.__conn.commit()
    
    def add(self, previous):
        pass

Crypto()