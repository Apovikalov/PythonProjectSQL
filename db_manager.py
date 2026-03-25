import psycopg2

from config import config

class DBManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = psycopg2.connect(dbname=self.db_name, **config())