#!/usr/bin/env python3
from land_commands.db_storage import *
import argparse
import sqlite3


# get root of company hierarchy
def get_root(company, db_cursor):
    current_parent = get_item(company, 'company_relations', db_cursor)[0][2]
    if current_parent == '':
        return company
    else:
        return get_root(current_parent, db_cursor)


# tree printer from the node level and current company level
# [] list tuple values could be wrapped into type of Company with accessors but for sake of quickness I used the [0][1]
def print_from_root(node: str, level, current_company, db_cursor):
    children = get_by_parent_company(node, 'company_relations', db_cursor)
    for c in children:
        company = " | - " + str(c[0]) + "; " + c[1] + "; " + str(count_parcel_items(c[0], 'land_ownership', db_cursor))
        mark = "" if not c[0] == current_company else "***"
        print(" " * level + str(company) + "  " + mark)
        print_from_root(c[0], level + 1, current_company, db_cursor)


def main():
    db_name = "land_ownership.db"
    connection = sqlite3.connect(db_name)
    db_cursor = connection.cursor()
    parser = argparse.ArgumentParser(
        'landtree',
        epilog=(
            'Example:\n'
            'landtree --mode=from_root C45353'
        )
    )
    parser.add_argument(
        '-mode', '--mode', type=str, dest='mode', required=True,
        help=(
            'mode of tree expanding'
        )
    )

    parser.add_argument(
        '-company', '--company', type=str, dest='company', required=True,
        help=(
            'company id to create the tree'
        )
    )
    args = parser.parse_args()
    if args.mode == "from_root":
        company_tree_root = get_root(args.company, db_cursor)
        root_details = get_item(company_tree_root, 'company_relations', db_cursor)
        print(str(root_details[0][0]) + "; " + str(root_details[0][1]) + "; "
              + str(count_parcel_items(root_details[0][0], 'land_ownership', db_cursor)))
        print_from_root(company_tree_root, 0, args.company, db_cursor)
    if args.mode == "expand":
        print_from_root(args.company, 0, args.company, db_cursor)
    connection.close()


if __name__ == '__main__':
    main()
