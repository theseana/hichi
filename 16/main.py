import mysql.connector

class DataBase:
    def __init__(self):       
        self.cnx = mysql.connector.connect(
            user='poulstar',
            password='poulstar',
            database='hichi',
            host='localhost',
        )
        self.cursor = self.cnx.cursor()

    def create(self,firstName, lastName):
        query = """INSERT INTO person
        (firstName, lastName)
        VALUES
        (%s, %s)"""
        data = (firstName, lastName)
        self.cursor.execute(query, data)
        self.cnx.commit()
        self.cnx.close()


DataBase().create('mobin', 'moghaddam')



SELECT idcompany FROM company WHERE name='SAIPA'; 