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
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # SQL query to get all married couples
    all_relationships_query = """
    SELECT prsn1.name, prsn2.name, start_date
    FROM relationships
    JOIN people prsn1 ON relationships.person1_id = prsn1.id
    JOIN people prsn2 ON relationships.person2_id = prsn2.id
    WHERE type = "spouse";
    """
    cur.execute(all_relationships_query)
    all_relationships = cur.fetchall()
    con.close()

    married_couples = [(prsn1, prsn2, start_date) for prsn1, prsn2, start_date in all_relationships]
    return married_couples

def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date  

    Args:
        married_couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path of CSV file
    """
    df = pd.DataFrame(married_couples, columns=["Person 1", "Person 2", "Anniversary"])
    df.to_csv(csv_path, index=False)

if __name__ == '__main__':
    main()
