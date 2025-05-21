import mysql.connector
from mysql.connector import Error

def connect():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='PDBC',
            user='root',
            password='Your Mysql Password'
        )
        if connection.is_connected():
            print("Connection Established")
            return connection
    except Error as e:
        print(f"Error: {e}")
    return None

def insert_user(connection):
    cursor = connection.cursor()
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    name = input("Enter Name: ")
    email = input("Enter Email: ")

    query = "INSERT INTO users (username, password, name, email) VALUES (%s, %s, %s, %s)"
    try:
        cursor.execute(query, (username, password, name, email))
        connection.commit()
        print("User inserted successfully!")
    except Error as e:
        print(f"Error: {e}")
    cursor.close()

def view_all_users(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    rows = cursor.fetchall()
    if rows:
        print("All Users:")
        for row in rows:
            print(f"{row[0]} {row[1]} {row[2]} {row[3]}")
    else:
        print("No users found.")
    cursor.close()

def view_user_by_username(connection):
    cursor = connection.cursor()
    username = input("Enter username to search: ")
    query = "SELECT * FROM users WHERE username=%s"
    cursor.execute(query, (username,))
    row = cursor.fetchone()
    if row:
        print(f"{row[0]} {row[1]} {row[2]} {row[3]}")
    else:
        print("No user found.")
    cursor.close()

def update_password(connection):
    cursor = connection.cursor()
    username = input("Enter the username to update password: ")
    new_password = input("Enter new password: ")
    query = "UPDATE users SET password=%s WHERE username=%s"
    cursor.execute(query, (new_password, username))
    connection.commit()
    if cursor.rowcount > 0:
        print("Password updated successfully!")
    else:
        print("User not found.")
    cursor.close()

def delete_user(connection):
    cursor = connection.cursor()
    username = input("Enter username to delete: ")
    query = "DELETE FROM users WHERE username=%s"
    cursor.execute(query, (username,))
    connection.commit()
    if cursor.rowcount > 0:
        print("User deleted successfully!")
    else:
        print("User not found.")
    cursor.close()

def menu():
    connection = connect()
    if not connection:
        print("Connection not Established")
        return

    while True:
        print("\n=== MENU ===")
        print("1. Insert a User")
        print("2. View All Users")
        print("3. View User by Username")
        print("4. Update Password")
        print("5. Delete User")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            insert_user(connection)
        elif choice == '2':
            view_all_users(connection)
        elif choice == '3':
            view_user_by_username(connection)
        elif choice == '4':
            update_password(connection)
        elif choice == '5':
            delete_user(connection)
        elif choice == '6':
            print("Thanks for using...!")
            connection.close()
            break
        else:
            print("Invalid choice. Please select from 1 to 6.")
menu()
