import mariadb

def add_car():

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

        while True:

            choice=int(input("Enter 1 to add a car. Enter 0 to exit to main menu. \n"))
            if choice==1:
                cursor=connection.cursor()
                mark=input("Enter car mark here: \n")
                model=input("Enter car model here: \n")
                value=float(input("Enter car value here: \n"))
                cursor.execute("INSERT INTO cars (car_mark, car_model, car_value) VALUES (?, ?, ?)", (mark, model, value))
                connection.commit()
                cursor.close()
                print("Car added successfully")
            elif choice==0:
                connection.close()
                break
            else:
                print("Choice not recognized. Please try again.")

    except mariadb.Error as e:
        print("Cannot connect to database. Wrong credentials")