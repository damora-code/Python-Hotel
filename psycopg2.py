import psycopg2
​
try:
    conn = psycopg2.connect(
        database="Cohort2",
        user="postgres",
        password="6108",
        host="127.0.0.1",
        port="5432"
    )
​
    # def retrieveUserInfo(id):
    #     cursor = conn.cursor()
    #     cursor.execute(
    #         f"SELECT first_name, last_name, phone_number FROM cohort2 WHERE user_id={id}"
    #     )
    #     rows = cursor.fetchall()
    #     if(rows):
    #         for row in rows:
    #             print(f'''
    #             First Name: {row[0]}
    #             Last Name: {row[1]}
    #             Phone: {row[2]}
    #             ''')
    #             cursor.close()
    #     else:
    #         print("Your database is empty")
​
    # userId = int(input("Enter the customer's id to pull their info >> "))
    # retrieveUserInfo(userId)
​
    # def insertUserInfo(name, lname, phone):
    #     cursor = conn.cursor()
    #     cursor.execute(
    #         f"INSERT INTO cohort2 (first_name, last_name, phone_number) VALUES ('{name}', '{lname}', '{phone}')"
    #     )
    #     conn.commit()
    #     print("Record inserted successfully")
    #     cursor.close()
    # name = input("Enter name >> ")
    # lname = input("Enter last name >> ")
    # phone = input("Enter phone number >> ")
    # insertUserInfo(name, lname, phone)
​
    # def deleteUserInfo(id):
    #     cursor = conn.cursor()
    #     cursor.execute(
    #         f"DELETE FROM cohort2 WHERE user_id={id}"
    #     )
    #     conn.commit()
    #     print("Record deleted successfully")
    #     cursor.close()
    # userId = int(input("Enter the customer's id you want to >> "))
    # deleteUserInfo(userId)
​
    def updateUserInfo(column_name, newValue, id):
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE cohort2 SET {column_name}='{newValue}' WHERE user_id={id}"
            # UPDATE cohort2 SET first_name='Fernando' WHERE user_id=1
        )
        conn.commit()
        cursor.close()
        print("Record updated successfully")
    id = int(input("Enter your id >> "))
    selection = int(input('''What do you want to update
    1. First Name
    2. Last Name
    3. Phone Number
    Make a selection [1-3] >> '''))
    newValue = input("Enter new value >> ")
    if(selection == 1):
        updateUserInfo("first_name", newValue, id)
    elif (selection == 2):
        updateUserInfo("last_name", newValue, id)
    else:
        updateUserInfo("phone_number", newValue, id)
​
except(Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)