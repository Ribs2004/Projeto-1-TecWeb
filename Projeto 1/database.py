import sqlite3
from dataclasses import dataclass

class Database:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name + '.db'
        self.conn = sqlite3.connect(self.db_name)
        self.conn.execute("""CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY, title STRING, content STRING NOT NULL)""")
        
    def add(self, note):
        sql = "INSERT INTO note (title, content) VALUES (?, ?)"
        args = (note.title, note.content)  
        cursor = self.conn.cursor()
        cursor.execute(sql, args)
        self.conn.commit() 

    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        data = []
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            note = Note(id=id, title=title, content=content)
            data.append(note)
        return data

    def update(self, entry):
        self.id = entry.id
        self.title = entry.title
        self.content = entry.content
        self.conn.execute(
            f"UPDATE note SET (title, content) = ('{self.title}', '{self.content}') WHERE id = '{self.id}'"
        )
        self.conn.commit()

    def delete(self, id):
        sql = "DELETE FROM note WHERE id = ?"
        arg = (id,)
        cursor = self.conn.cursor()
        cursor.execute(sql, arg)
        self.conn.commit()



@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''     