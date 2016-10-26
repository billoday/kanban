from datetime import date
import sqlite3


class Board:
    def __init__(self, file):
        self.db = file
        conn = sqlite3.connect(self.db)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute('''create table if not exists kb_board(
                     id integer primary key autoincrement,
                     state integer,
                     title text,
                     notes text,
                     created text);''')
        conn.commit()
        c.close()

    def newItem(self, title, state):
        t = (title, state, str(date.today()))
        conn = sqlite3.connect(self.db)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute('''insert into kb_board(title, state, created) values (?,?,?);''', t)
        conn.commit()
        c.close()

    def getState(self, state):
        listing = []
        t = (state, )
        conn = sqlite3.connect(self.db)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute('''select * from kb_board where state=?;''', t)
        for item in c.fetchall():
            listing.append({'id': item['id'], 'title': item['title'], 'created': item['created']})
        c.close()
        return listing

    def moveItem(self, newState, id):
        t = (newState, id)
        conn = sqlite3.connect(self.db)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute('''update kb_board set state=? where id=?;''', t)
        conn.commit()
        c.close()
