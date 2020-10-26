#!/usr/bin/env python3

import sqlite3


# generates db structure with indexes on queries columns
def create_db_structure(db_cursor, connection):
    db_cursor.execute("CREATE TABLE company_relations (company_id TEXT, name TEXT, parent TEXT);")
    db_cursor.execute("CREATE INDEX company_index_1 ON company_relations (name);")
    db_cursor.execute("CREATE INDEX company_index_2 ON company_relations (parent);")
    db_cursor.execute("CREATE TABLE land_ownership (land_id TEXT, company_id TEXT);")
    db_cursor.execute("CREATE INDEX land_index_1 ON land_ownership (land_id);")
    db_cursor.execute("CREATE INDEX land_index_2 ON land_ownership (company_id);")
    connection.commit()


# loads data into 'company_relations' with fixed company_relations.csv file
def add_companies_from_csv(file, db_cursor, connection):
    counter = 0
    db_list = []
    with open(file) as infile:
        for line in infile:
            data = line.strip('\n').split(",")
            if counter > 0:
                company_id = data[0]
                name = data[1]
                parent = data[2]
                db_list.append((company_id, name, parent))
            counter += 1
    print(len(db_list))
    db_cursor.executemany("INSERT INTO company_relations VALUES (?, ?, ?)", db_list)
    connection.commit()


# loads data into 'land_ownership' with fixed land_ownership.csv file
def add_ownership_from_csv(file, db_cursor, connection):
    counter = 0
    db_list = []
    with open(file) as infile:
        for line in infile:
            data = line.strip('\n').split(",")
            if counter > 0:
                land_id = data[0]
                company_id = data[1]
                db_list.append((land_id, company_id))
            counter += 1
    print(len(db_list))
    db_cursor.executemany("INSERT INTO land_ownership VALUES (?, ?)", db_list)
    connection.commit()


def main():
    db_name = "land_ownership.db"
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    create_db_structure(cursor, connection)
    add_companies_from_csv('./company_relations.csv', cursor, connection)
    add_ownership_from_csv('./land_ownership.csv', cursor, connection)
    connection.close()


if __name__ == '__main__':
    main()
