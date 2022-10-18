# DrugConsumption
CMPE 285 Project: Create a Tableu Dashboard to analyze the Drug Consumption dataset.

# Getting Started

## Application Architecture 
TBD.

## Set up virtual environment

Create your virtual environment. 
```
python3 -m venv <venv_name>
```

Activate your environment (in macOS). 
```
source venv/bin/activate
```
Install dependencies. 
```
pip3 install -r requirements.txt
```

## PostgreSQL
Start your PostgreSQL in its GUI, then you can connect it to via CLI by running: 
```
psql postgresql://<your_username>@localhost:5432/<db_name>
```
Confirm you're connected. 
```
\conninfo
```

## Run Flask Server
```
export FLASK_APP=main
flask run
```