import psycopg2

# Connect to the database

class Databaseconnection:
    
    def set_up_database(self):
        """ This function sets up a database connection"""
        self.conn = psycopg2.connect(host="localhost", database="events", user="postgres", password="123")
        return self.conn
    
    def create_cursor(self):
        """ This function creates a cursor object """
        self.cur = self.conn.cursor()
        return self.cur

    def create_users_table(self):
        """ This function creates a users table in the events database"""
        Users_table = """create table if not exists Users(user_id serial PRIMARY KEY NOT NULL,
                                             first_name VARCHAR NOT NULL,
                                             last_name VARCHAR NOT NULL,
                                             age VARCHAR,
                                             email VARCHAR,
                                             password VARCHAR,
                                             created_at TIME)"""
        self.cur.execute(Users_table)
    
    def create_events_table(self):
        """ This function creates an events table in the database"""
        Events_table = """create table if not exists Event(event_id serial PRIMARY KEY NOT NULL,
                                             event_name VARCHAR NOT NULL,
                                             price VARCHAR,
                                             location VARCHAR)"""
        self.cur.execute(Events_table)
    
    def create_tickets_table(self):
        """ This function creates a tickets table in the events database"""
        Tickets_table = """create table if not exists Ticket(ticket_id serial PRIMARY KEY NOT NULL,
                                                     user_id INT REFERENCES Users(user_id),
                                                     event_id INT REFERENCES Event(event_id),
                                                     is_valid BOOLEAN,
                                                     verification_code VARCHAR,
                                                     created_at TIME)"""
        self.cur.execute(Tickets_table)
    
    def close_database_connection(self):
        self.conn.commit()
        self.conn.close()

db = Databaseconnection()
db.set_up_database()
db.create_cursor()
db.create_users_table()
db.create_events_table()
db.create_tickets_table()
db.close_database_connection()
