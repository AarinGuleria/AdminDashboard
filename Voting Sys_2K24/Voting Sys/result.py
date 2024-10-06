import mysql.connector

def display_result():
    cursor.execute("SELECT candidates.name, COUNT(votes.id) AS vote_count FROM candidates LEFT JOIN votes ON candidates.id = votes.candidate_id GROUP BY candidates.id")
    results = cursor.fetchall()
    print("Election Results:")
    for result in results:
        print(f"{result[0]}: {result[1]} votes")

if __name__ == "__main__":
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Banku@sushi123",
        database="voting_system"
    )
    cursor = cnx.cursor()

    display_result()

    cursor.close()
    cnx.close()
