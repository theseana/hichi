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

    def update(self,firstName, lastName, id_):
        query = """UPDATE person
        SET firstName=%s, lastName=%s
        WHERE personId=%s"""
        data = (firstName, lastName, id_)
        self.cursor.execute(query, data)
        self.cnx.commit()
        self.cnx.close()

    def delete(self, id_):
        query = """DELETE FROM person
        WHERE personId=%s"""
        data = (id_,)
        self.cursor.execute(query, data)
        self.cnx.commit()
        self.cnx.close()


    def select(self):
        query = """SELECT * FROM person"""
        self.cursor.execute(query)
        jib = self.cursor.fetchall()
        self.cnx.close()
        return jib


jibeman = DataBase().select()
print(jibeman)



