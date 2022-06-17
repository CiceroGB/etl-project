import mysql.connector as mysql

class DatabaseConnection:

    connection = None

    @classmethod
    def connect(cls):
        db_connection = mysql.connect(
            host = "database",
            port = 3306,
            database = "etl",
            user = "root",
            passwd = "rootpw"
        )
        cls.connection = db_connection
