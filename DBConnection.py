import os

import psycopg2
from dotenv import load_dotenv, find_dotenv


class DBConnection:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.host = os.environ.get("host")
        self.dname = os.environ.get("dname")
        self.user = os.environ.get("user")
        self.password = os.environ.get("password")

    def get_connection(self):
        return psycopg2.connect("host=" + self.host + " dbname=" + self.dname + " user=" + self.user + " password=" + self.password)
