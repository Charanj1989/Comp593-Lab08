"""
Description:
 Generates a CSV reports containing all married couples in
 the Social Network database.

Usage:
 python marriage_report.py
"""
import os
import sqlite3
from create_relationships import db_path, script_dir
import pandas as pd
def main():
    # Query DB for list of married couples
    married_couples = get_married_couples()
    # Save all married couples to CSV file
    csv_path = os.path.join(script_dir, 'married_couples.csv')
    save_married_couples_csv(married_couples, csv_path)

def get_married_couples():
    """Queries the Social Network database for all married couples.

    Returns:
        list: (name1, name2, start_date) of married couples 
    """
    # TODO: Function body
    # Hint: See example code in lab instructions entitled "Get a List of Relationships"
    con = sqlite3.connect(db_path)
    #con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    # SQL query to get all relationships
    all_relationships_query = """
                            SELECT prsn1.name, prsn2.name, start_date, type FROM relationships
                            JOIN people prsn1 ON prsn1_id = prsn1.id
                            JOIN people prsn2 ON prsn2_id = prsn2.id WHERE type="spouse";
                            """
    # Execute the query and get all results
    cur.execute(all_relationships_query)
    all_relationships = cur.fetchall()
    con.commit()
    con.close()
    T1 = list()
    L1 = list()
    
    # Print sentences describing each relationship
    for prsn1, prsn2, start_date, type in all_relationships:
        print(f'{prsn1} has been a {type} of {prsn2} since {start_date}.')
        T1 = [prsn1,prsn2,start_date]
        L1.append(T1)
    return L1

def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date  

    Args:
        married_couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path of CSV file
    """
    # TODO: Function body
    # Hint: We did this in Lab 7.
    name1 = []
    name2 = []
    start_dt = []
    for i in married_couples:
        name1.append(i[0])
        name2.append(i[1])
        start_dt.append(i[2])
    df1 = pd.DataFrame({"Prsn1": name1,"Prsn2":name2,"Anniversary": start_dt})
    filename = os.path.basename(csv_path)
    df1.to_csv(filename, index=False)
    return

if __name__ == '__main__':
   main()