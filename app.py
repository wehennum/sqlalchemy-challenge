from flask import Flask, jsonify

app = Flask(__name__)

# Define the homepage route
@app.route('/')
def homepage():
    return (
        "Welcome to the Climate App API!<br/><br/>"
        "Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/start_date<br/>"
        "/api/v1.0/start_date/end_date"
    )

# Add more routes as needed

if __name__ == '__main__':
    app.run(debug=True)
