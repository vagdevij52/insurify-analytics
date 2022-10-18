import pandas as pd
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/lindanguyen'
db = SQLAlchemy(app)

@app.route("/")
def main():
    return "<h1>Drug Consumption Analysis with Tableau</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000) 

