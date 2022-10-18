import pandas as pd
import psycopg2

    
def insert_data(): 
    # Fetch dataset
    # dataset_url = "https://raw.githubusercontent.com/lindavy/DrugConsumption/main/drug_consumption.txt"
    dataset_loc = "/Users/lindanguyen/Desktop/DrugConsumption/drug_consumption.txt"
    col_names = ['ID', 'Age', 'Gender', 'Education', 'Country', 'Ethnicity', 
                'nscore', 'escore', 'oscore', 'ascore', 'cscore', 'impulsive', 'ss', 
                'alcohol', 'amphet', 'amyl', 'benzos', 'caffeine', 'cannibis', 'choc', 
                'coke', 'crack', 'ecstasy', 'heroin', 'ketamine', 'legalh', 'lsd', 
                'meth', 'shrooms', 'nicotine', 'semer', 'vsa']
    df = pd.read_csv(dataset_loc, sep=",", names=col_names)

    # *** Edit this on your computer ***
    db_name = "lindanguyen"
    user = "lindanguyen"
    password = "123"
    host = "localhost"
    port = "5432"

    try: 
        conn = psycopg2.connect(database=db_name, user = user, password = password, host = host, port = port)
        print("Opened database successfully")

        cur = conn.cursor()

        # Insert entries to PostgreSQL tables
        size = len(df)
        for i in range(size): 
            sql = "insert into background values(%s, %s, %s, %s, %s, %s)" % (df["ID"][i], df["Age"][i], df["Gender"][i], df["Education"][i], df["Country"][i], df["Ethnicity"][i])
            cur.execute(sql)

        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)



insert_data()