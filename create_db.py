"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import sqlite3
from datetime import datetime
from faker import Faker
#import random
# Determine the path of the database

def main():
    con = sqlite3.connect('social_network.db')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, 'social_network.db')
    con.commit()
    cur = con.cursor()
    create_people_table()
    populate_people_table()
    con.close()

def create_people_table():
    """Creates the people table in the database"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Creating a Table"
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    ppl_tbl_query = """CREATE TABLE IF NOT EXISTS people
                    (id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    address TEXT NOT NULL,
                    city TEXT NOT NULL,
                    province TEXT NOT NULL,
                    bio TEXT,
                    age INTEGER,
                    created_at DATETIME NOT NULL,
                    updated_at DATETIME NOT NULL);"""
    cur.execute(ppl_tbl_query)
    con.commit()
    con.close()
    return

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Inserting Data into a Table"
    # Hint: See example code in lab instructions entitled "Working with Faker"
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    add_person_query = """INSERT INTO PEOPLE(
                          name,
                          email,
                          address,
                          city,
                          province,
                          bio,
                          age,
                          created_at,
                          updated_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    fake = Faker("en_CA")
    for i in range(200):
        nm = fake.name()
        ema_il = fake.email()
        add_ress = fake.address()
        ci_ty = fake.city()
        pro_vince = fake.administrative_unit()
        L=["Enjoys making Funny sounds while talking", "Very smart and hardworking", "Well-mannered and kind person", "Bold and strong personality", ""]
        bi_o = fake.word(ext_word_list = L)
        ag_e = fake.random_int(min=1, max=100)
        date1 = datetime.now()
        date2 = datetime.now()
        L1 = (nm,ema_il,add_ress,ci_ty,pro_vince,bi_o,ag_e,date1,date2)
        cur.execute(add_person_query,L1)
    con.commit()
    con.close()
    return



if __name__ == '__main__':
   main()