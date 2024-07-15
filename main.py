import mysql.connector
from queries import *;
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="mininetdb"
        )
        if connection.is_connected():
            print("Connected to MySQL database")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection()

# Remember to close the connection when done
def close_db():
    if connection and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Error as e:
        print(f"Error: {e}")

def user_menu():
    connection = create_connection()
    if not connection:
        return
    while True:
        print("\n Menu:")
        print("\n1. Export all the data about users in HD subscriptions")
        print("\n2. Export all data about actors and their associated movies")
        print("\n3. Export all data to group actors from a specific city, showing also the average age (per city)")
        print("\n4. Export all data to show the favourite comedy movies for a specific user")
        print("\n5. Export all data to count how many subscriptions are in the database per country")
        print("\n6. Export all data to find the movies that start with the keyword The")
        print("\n7. Export data to find the number of subscriptions per movie category")
        print("\n8. Export data to find the username and the city of the youngest customer in the UHD subscription category")
        print("\n9. Export data to find users between 22 - 30 years old (including 22 and 30 )")
        print("\n10. Export data to find the average age of users with low score reviews (less than 3). Group your data for users under 20, 21-40, and 41 and over")
        print("\n11. Export all data of users with specific subscription")
        print("\n12. Export all the data about a specific actor and movies associated with that actor")
        print("\n13. Export all data of the actors from a specific city, showing their average age")
        print("\n14. Export all data to show the favourite comedy movies for a particular user")
        print("\n15. Export all data to count how many subscriptions are in the database for a specific country")
        print("\n16. Close Database Connection")
        print("\n17. Exit")

        choice = input("Enter the number of query you want to run: ")

        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                execute_query(connection, query_1)
            elif choice == 2:
                execute_query(connection, query_2)
            elif choice == 3:
                execute_query(connection, query_3)
            elif choice == 4:
                execute_query(connection, query_4)
            elif choice == 5:
                execute_query(connection, query_5)
            elif choice == 6:
                execute_query(connection, query_6)
            elif choice == 7:
                execute_query(connection, query_7)
            elif choice == 8:
                execute_query(connection, query_8)
            elif choice == 9:
                execute_query(connection, query_9)
            elif choice == 10:
                execute_query(connection, query_10)
            elif choice == 11:
                subscription_type = input("Enter subscription type (HD/UHD): ").strip()
                query = f"SELECT * FROM user u 
                            JOIN subscription s
                            ON u.subscription_type = s.subscription_id 
                            WHERE s.subscription_type = '{subscription_type}';"
                execute_query(connection, query)
            elif choice == 12:
                actor_name = input("Enter actor name: ").strip()
                query = f"SELECT actor.*, movie.* 
                            FROM actor 
                            JOIN movieactor 
                            ON actor.actor_id = movieactor.actor_id 
                            JOIN movie 
                            ON movie.movie_id = movieactor.movie_id 
                            WHERE actor.actor_name = '{actor_name}';"
                execute_query(connection, query)
            elif choice == 13:
                city_name = input("Enter city name: ").strip()
                query = f"SELECT city, COUNT(actor_id) AS number_of_actors, AVG(YEAR(CURDATE()) - YEAR(dob)) 
                            AS average_age 
                            FROM actor 
                            WHERE city = '{city_name}' 
                            GROUP BY city;"
                execute_query(connection, query)
            elif choice == 14:
                username = input("Enter username: ").strip()
                query = f"SELECT favouritemovie.user_id, movie.* 
                            FROM favouritemovie 
                            JOIN user 
                            ON favouritemovie.user_id = user.user_id 
                            JOIN movie 
                            ON movie.movie_id = favouritemovie.movie_id 
                            WHERE user.username = '{username}' 
                            AND movie.genre = 'Comedy';"
                execute_query(connection, query)
            elif choice == 15:
                country_name = input("Enter country name: ").strip()
                query = f"SELECT country, COUNT(subscription_type) AS subscription_count 
                            FROM user 
                            WHERE country = '{country_name}' 
                            GROUP BY country;"
                execute_query(connection, query)
            elif choice == 16:
                close_db()
                break
            else:
                print("Invalid choice. Please select a number from the menu.")
        else:
            print("Invalid input. Please enter a number.")

        continue_choice = input("Do you want to continue? (Y/N): ").strip().upper()
        if continue_choice != 'Y':
            break

user_menu()
                




