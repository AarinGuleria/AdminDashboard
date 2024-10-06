import mysql.connector

def main():
    def register_candidate():
        name = input("Enter candidate's name: ")
        cursor.execute("INSERT INTO candidates (name) VALUES (%s)", (name,))
        cnx.commit()
        print("Candidate registered successfully!")

    if __name__ == "__main__":
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Banku@sushi123",
            database="voting_system"
        )
        cursor = cnx.cursor()

        register_candidate()

        cursor.close()
        cnx.close()
    main()
main()


    
