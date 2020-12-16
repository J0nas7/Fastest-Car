import mysql.connector
from mysql.connector import Error
from config import dbpwd

"""
SINGLETON
Ensure a class only has one instance, and provide a global point of
access to it.
"""

class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None


    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class DatabaseController(metaclass=Singleton):
    """
    Example class.
    """
    cursor = None

    def DBconn(self):
        global cursor
        try:
            self.connection = mysql.connector.connect(host='mysql78.unoeuro.com',
                                                database='seobetter_dk_db_seobtr',
                                                user='seobetter_dk',
                                                password=dbpwd)
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                self.cursor = self.connection.cursor()
                print("Connected to MySQL Server version ", db_Info)
                print("You're connected to database: ")

        except Error as e:
            print("Error while connecting to MySQL", e)