import mariadb

def client_view(actual_client_login: str):

    connection=mariadb.connect(
        user="desktop",
        password="MKzixgh61$!#baj",
        host="192.168.1.100",
        database="used_car_dealer"
    )

    while True:
        choice=int(input("Enter 1 to view your data. Enter 2 to see all available cars on sale. Enter 3 to order a car. Enter 4 to view your orders. Enter 5 to return to main menu \n"))
        if choice==1:
            
            cursor=connection.cursor()
            cursor.execute("SELECT client_name, client_surname, client_budget FROM clients WHERE client_login=?", (actual_client_login,))

            data=cursor.fetchone()

            print(f"Your name: {data[0]}")
            print(f"Your surname: {data[1]}")
            print(F"Your budget: {data[2]}")

            cursor.close()

        elif choice==2:

            cursor=connection.cursor()
            cursor.execute("SELECT car_id, car_mark, car_model, car_value FROM cars WHERE is_sold=FALSE")

            cars=cursor.fetchall()

            for car in cars:
                print(f"Car id: {car[0]}, car mark: {car[1]}, car model: {car[2]}, car value: {car[3]} ")

            cursor.close()

        elif choice==3:

            actual_car_id=int(input("Enter car ID here you want to order: \n"))

            try:
                cursor=connection.cursor()
                cursor.execute("SELECT car_value FROM cars WHERE car_id=?", (actual_car_id,))
                actual_car_value=cursor.fetchone()[0]
                cursor.execute("SELECT client_budget FROM clients WHERE client_login=?", (actual_client_login,))
                actual_client_budget=cursor.fetchone()[0]
                if actual_client_budget>actual_car_value:
                    print("Car odered successfully. ")
                    cursor.execute("UPDATE cars SET is_sold=TRUE WHERE car_id=?", (actual_car_id,))
                    new_client_budget=actual_client_budget-actual_car_value
                    cursor.execute("UPDATE clients SET client_budget=? WHERE client_login=?", (new_client_budget, actual_client_login))
                    cursor.execute("SELECT client_id FROM clients WHERE client_login=?", (actual_client_login,))
                    actual_client_id=cursor.fetchone()[0]
                    cursor.execute("INSERT INTO orders(ordering_client_id, ordered_car_id) VALUE (?, ?)", (actual_client_id, actual_car_id))
                    connection.commit()
                    cursor.close()
                else:
                    print("Not enough budget to buy a car. ")

            except TypeError:
                print("Car with given id does not exist. Please make sure that you want to buy right car. ")

        elif choice==4:

            cursor=connection.cursor()
            cursor.execute("SELECT client_id FROM clients WHERE client_login=?", (actual_client_login,))
            actual_client_id=cursor.fetchone()[0]
            cursor.execute("SELECT car_mark, car_model, car_value FROM cars JOIN orders ON car_id=ordered_car_id WHERE ordering_client_id=?", (actual_client_id,))
            orders=cursor.fetchall()
            for order in orders:
                print(f"Ordered car mark: {order[0]}, car model: {order[1]}, car value: {order[2]}")
            cursor.close()

        elif choice==5:
            connection.close()
            break

        else:
            print("Choice not recognized. Please try again")