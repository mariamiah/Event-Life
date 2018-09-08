import sys
from app.database.events_db import Databaseconnection


class Ticket:
    def __init__(self, user_id, event_id, is_valid, verification_code, created_at, ticket_id):
        self.user_id = user_id
        self.event_id = event_id
        self.is_valid = is_valid
        self.verification_code = verification_code
        self.created_at = created_at
        self.ticket_id = ticket_id
        self.available_tickets = dict()

    def add_ticket(self):
        if len(self.available_tickets.keys()) == 0:
            return "Tickets fields blank"

        if len(self.available_tickets.keys()) != 7:
            return "Please enter all the required fields"

        if self.available_tickets["ticket_id"] is None:
            return "Ticket_id cannot be blank"

        if self.available_tickets["ticket_id"]:
            sql = """INSERT INTO tickets VALUES (%s, %s, %s, %s, %s, %s) % (self.user_id, self.event_id,
            self.is_valid, self.verification_code, self.created_at, self.ticket_id)"""
            cur.execute(sql)
            conn.commit()
            conn.close


    ticket = Ticket("001", "57", True, "345", datime.now(), "23")
    ticket.add_ticket()
