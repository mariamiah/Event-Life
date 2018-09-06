import psycopg2

class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
           """
           dbname = 'adminuser' user = 'adminuser' password = 'newpassword' host = "localhost" port = "5432"

           """
        )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print('Connected to the database')
        except Exception as e:
            print(e.message)
            print("Failed to connect to db")
