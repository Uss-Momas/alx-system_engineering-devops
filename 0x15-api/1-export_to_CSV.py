#!/usr/bin/python3
"""
TODO List
"""
import csv
import requests
from sys import argv


def main(id):
    """
    Main entrance program
    """
    url_root = "https://jsonplaceholder.typicode.com/todos?userId"
    user_url = "https://jsonplaceholder.typicode.com/users"
    # Or "https://jsonplaceholder.typicode.com/users/1/todos"
    todos_list = requests.get("{}={}".format(url_root, id)).json()
    user_info = requests.get("{}/{}".format(user_url, id)).json()
    username = user_info.get("username")
    list_to_export = []

    for todo in todos_list:
        obj = {}
        obj["id"] = id
        obj["name"] = username
        obj["completed"] = todo.get("completed")
        obj["title"] = todo.get("title")
        list_to_export.append(obj)
    return list_to_export


def export_to_csv():
    """
    Export the content to CSV format
    """
    list_to_export = main(argv[1])
    filename = "{}.csv".format(argv[1])
    fields = ["id", "name", "completed", "title"]
    with open(filename, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields,
                                quoting=csv.QUOTE_ALL)
        writer.writerows(list_to_export)


if __name__ == "__main__":
    export_to_csv()
