from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Banku@sushi123",
    database="voting_system"
)
mycursor = mydb.cursor()

# Function to display the candidates for voting
def display_candidates():
    mycursor.execute("SELECT * FROM candidates")
    candidates = mycursor.fetchall()
    return candidates

# Function to vote for a candidate
def vote(user_id, candidate_id):
    try:
        mycursor.execute("SELECT * FROM votes WHERE user_id = %s", (user_id,))
        existing_vote = mycursor.fetchone()
        if existing_vote:
            return "Error: Invalid Vote (Voter Already Exists)"
        
        sql = "INSERT INTO votes (user_id, candidate_id) VALUES (%s, %s)"
        val = (user_id, candidate_id)
        mycursor.execute(sql, val)
        mydb.commit()
        return "Vote submitted successfully!"
    except Exception as e:
        return "Error casting vote: " + str(e)

# Main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        user_id = request.form['user_id']
        candidate_id = request.form['candidate_id']
        message = vote(user_id, candidate_id)
        candidates = display_candidates()
        return render_template('index.html', message=message, candidates=candidates)
    else:
        candidates = display_candidates()
        return render_template('index.html', candidates=candidates)

if __name__ == "__main__":
    # Change the host parameter to '0.0.0.0' to listen on all available network interfaces
    # This makes your Flask application accessible from other devices on the same network
    app.run(host='0.0.0.0', debug=True)
