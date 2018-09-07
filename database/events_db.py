import psycopg2

# Connect to the database
conn = psycopg2.connect(host="localhost", database="events", user="postgres", password="123")
# create a cursor
conn.autocommit = True
cur = conn.cursor()

Users_table = """create table if not exists Users(user_id serial PRIMARY KEY NOT NULL,
                                             first_name VARCHAR NOT NULL,
                                             last_name VARCHAR NOT NULL,
                                             age VARCHAR,
                                             email VARCHAR,
                                             password VARCHAR,
                                             created_at TIME)"""

cur.execute(Users_table)


Events_table = """create table if not exists Event(event_id serial PRIMARY KEY NOT NULL,
                                             event_name VARCHAR NOT NULL,
                                             price VARCHAR,
                                             location VARCHAR)"""

cur.execute(Events_table)


Tickets_table = """create table if not exists Ticket(ticket_id serial PRIMARY KEY NOT NULL,
                                                     user_id INT REFERENCES Users(user_id),
                                                     event_id INT REFERENCES Event(event_id),
                                                     is_valid BOOLEAN,
                                                     verification_code VARCHAR,
                                                     created_at TIME)"""
cur.execute(Tickets_table)

conn.close()
