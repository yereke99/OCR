import mysql.connector, os
from mysql.connector import errorcode
from sys import exit

user_data = {}

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password = "121212",
        port = "3306",
        database = "sayat_db"
    )


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Пайдаланушы аты немесе пароль қате!")
        exit()
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("DATABASE does not exit")
        exit()
    else:
        print(err)
        exit()

cursor = db.cursor()

#cursor.execute("CREATE DATABASE sayat_db")

#cursor.execute("CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, aty VARCHAR(100),surname VARCHAR(100), telenumber VARCHAR(100), type VARCHAR(100), date_time VARCHAR(30),  check VARCHAR(50))")
#db.commit()

#cursor.execute("CREATE TABLE CLIENT (id INT AUTO_INCREMENT PRIMARY KEY, n VARCHAR(100), s VARCHAR(50), tele VARCHAR(50), data VARCHAR(50), type VARCHAR(100),   c VARCHAR(10))")
#db.commit()


#cursor.execute("CREATE TABLE CLIENT_ZA (id INT AUTO_INCREMENT PRIMARY KEY, n VARCHAR(100), s VARCHAR(50), tele VARCHAR(50), data VARCHAR(50), type VARCHAR(100),   c VARCHAR(10))")
#db.commit()

#cursor.execute("CREATE TABLE DOCS (id INT AUTO_INCREMENT PRIMARY KEY, doc VARCHAR(100), datetime VARCHAR(30))")
#db.commit()


#cursor.execute("CREATE TABLE hashtags (id INT AUTO_INCREMENT PRIMARY KEY, hashtags VARCHAR(255) UNIQUE )")
#db.commit()


#cursor.execute("CREATE TABLE docs_from (id INT AUTO_INCREMENT PRIMARY KEY, file_name VARCHAR(255), data VARCHAR(255))")
#db.commit()

#cursor.execute("CREATE TABLE hashtag_page (id INT AUTO_INCREMENT PRIMARY KEY, Instagram_Accounts VARCHAR(255) )")
#db.commit()

#cursor.execute("CREATE TABLE accounts (id INT AUTO_INCREMENT PRIMARY KEY, usr VARCHAR(255) )")
#db.commit()

# DELETE ALL RECORD
#cursor.execute("DELETE FROM accounts ")
#db.commit()
#print('Записи удалена!')

class User:
    def __init__(self, login):
        self.login = login
        self.password = ''






