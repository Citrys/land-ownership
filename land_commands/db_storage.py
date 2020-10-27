#!/usr/bin/env python3
import sqlite3


# get single item from table
def get_item(company_id: str, table: str, cursor: sqlite3.Cursor):
    sql = f"SELECT * FROM {table} WHERE company_id='{company_id}'"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


# count parcels for particular company_id
def count_parcel_items(company_id: str, table: str, cursor: sqlite3.Cursor):
    sql = f"SELECT COUNT(*) FROM {table} WHERE company_id='{company_id}'"
    cursor.execute(sql)
    result = cursor.fetchall()[0][0]
    return result


# get company by parent id
def get_by_parent_company(parent: str, table: str, cursor: sqlite3.Cursor):
    sql = f"SELECT * FROM {table} WHERE parent='{parent}'"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
