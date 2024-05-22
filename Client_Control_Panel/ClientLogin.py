import mariadb
import argon2
from ClientFunctions import client_view

def client_login():

    login=input("Enter your login here: \n")
    password=input("Enter your password here: \n")
    ph=argon2.PasswordHasher()

    connection=mariadb.connect(
        user="desktop",
        password="MKzixgh61$!#baj",
        host="192.168.1.100",
        database="used_car_dealer"
    )

    try:
        cursor=connection.cursor()
        cursor.execute("SELECT client_login, client_password FROM clients WHERE client_login=?", (login,))
        user=cursor.fetchone()
        if ph.verify(user[1], password):
            print("Login successfull")
            client_view(user[0])
    except argon2.exceptions.VerifyMismatchError:
        print("Password does not match")
    except TypeError:
        print("User with defined login does not occur")

    cursor.close()

    connection.close()




