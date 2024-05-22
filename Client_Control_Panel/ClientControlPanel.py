from AddClient import create_client
from ClientLogin import client_login

def main():

    while True:
        choice=int(input("Enter 1 if you want to register. Enter 2 if you want to login. Enter 0 if you want to exit from program. \n"))
        if choice==1:
            create_client()
        elif choice==2:
            client_login()
        elif choice==0:
            break
        else:
            print("Choice not recognized. Please enter again. \n")          


if __name__=="__main__":
    main()