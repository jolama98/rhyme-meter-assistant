import sqlite3
from datetime import datetime
from typing import Optional
from models.poem import Poem

class PoemRepository:
    """Handles database operations"""
    
    def __init__(self, db_path='database.db'):
        """Constructor - runs when you create PoemRepository()"""
        self.db_path = db_path
        self._initialize_db()
    
    def _initialize_db(self):
        """Create table if not exists"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS poems (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    form_type TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
    
    def create_poem(self, poem_data: Poem) -> Poem:
        """INSERT new poem into database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            sql = '''
                INSERT INTO poems (title, content, form_type, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?)
            '''
            
            values = (
                poem_data.title,
                poem_data.content,
                poem_data.form_type,
                datetime.now(),
                datetime.now()
            )
            
            cursor.execute(sql, values)
            conn.commit()
            
            poem_data.id = cursor.lastrowid
            poem_data.created_at = datetime.now()
            poem_data.updated_at = datetime.now()
            
            return poem_data
