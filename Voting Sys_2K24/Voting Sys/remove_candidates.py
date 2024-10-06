import mysql.connector

def main():
    def register_candidate():
        name = input("Enter candidate's name: ")
        cursor.execute("INSERT INTO candidates (name) VALUES (%s)", (name,))
        cnx.commit()
        print("Candidate registered successfully!")

    def remove_candidate():
        name = input("Enter the name of the candidate to remove: ")
        cursor.execute("DELETE FROM candidates WHERE name = %s", (name,))
        cnx.commit()
        print("Candidate removed successfully!")

    if __name__ == "__main__":
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Banku@sushi123",
            database="voting_system"
        )
        cursor = cnx.cursor()

        register_candidate()

        # To remove a candidate, call the remove_candidate function
        remove_candidate()

        cursor.close()
        cnx.close()

main()

