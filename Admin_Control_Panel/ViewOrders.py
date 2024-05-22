import mariadb

def orders():

    admin_login=input("Enter admin login here: \n")
    admin_password=input("Enter admin password here: \n")

    try:
        connection=mariadb.connect(
            user=admin_login,
            password=admin_password,
            host="192.168.1.100",
            database="used_car_dealer"
        )

        print("Login successfull")

        cursor=connection.cursor()

        cursor.execute("SELECT client_name, client_surname, car_mark, car_model FROM clients JOIN orders ON ordering_client_id=client_id JOIN cars ON ordered_car_id=car_id")

        listOfOrders=cursor.fetchall()

        for order in listOfOrders:
            print(f"Ordering client name: {order[0]}, surname: {order[1]}. Ordered car mark: {order[2]}, model: {order[3]}")

        with open("orders.txt", "w") as file:
            for order in listOfOrders:
                file.write(f"Ordering client name: {order[0]}, surname: {order[1]}. Ordered car mark: {order[2]}, model: {order[3]} \n")

        print("Orders saved to local file orders.txt")

        cursor.close()

        connection.close()

    except mariadb.Error as e:
        print("Cannot connect to database. Wrong credentials")
    except TypeError:
        print("There are no orders at this time in database")