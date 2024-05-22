import mariadb
from argon2 import PasswordHasher


def isEmail(email_address: str):
    
     if "@" in email_address:
          return True
     else:
          return False
     

def hashPassword(password: str):

    ph=PasswordHasher()
    hash=ph.hash(password)
    return hash


def add_client(name: str, surname: str, email: str, login: str, password: str, budget: float):
     
     connection=mariadb.connect(
          user="desktop",
          password="MKzixgh61$!#baj",
          host="192.168.1.100",
          database="used_car_dealer")
     
     cursor=connection.cursor()

     try:
          cursor.execute("INSERT INTO clients (client_name, client_surname, client_email, client_login, client_password, client_budget) VALUES (?, ?, ?, ?, ?, ?)", (name, surname, email, login, password, budget))
          print("Client created successfully")
     except mariadb.IntegrityError:
          print("Given email or login already exist in database. Please choose different.")    
     except mariadb.Error as e:
          print(f"Error: {e}")

     connection.commit()

     connection.close()


def create_client():
     
     while True:
          name=input("Enter you name here: \n")
          surname=input("Enter your surname here: \n")
          email=input("Enter your email here: \n")
          login=input("Enter your login here: \n")
          password=input("Enter your password here: \n")
          budget=float(input("Enter your budget here: \n"))

          if isEmail(email) and name.isalpha() and surname.isalpha():
               hashed_password=hashPassword(password)
               add_client(name, surname, email, login, hashed_password, budget)
               break
          else:
               print("Email must contain @. Name and surname must be only letters. \n")
            
          
