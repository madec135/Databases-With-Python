from AddCar import add_car
from ViewOrders import orders

def main():

    while True:
        choice=int(input("Enter 1 to add a car to database. Enter 2 to view all orders. Enter 0 to exit from program. \n"))
        if choice==1:
            add_car()
        elif choice==2:
            orders()
        elif choice==0:
            break
        else:
            print("Choice not recognized. Please try again.")


if __name__=="__main__":
    main()