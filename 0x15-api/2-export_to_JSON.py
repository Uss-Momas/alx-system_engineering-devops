#!/usr/bin/python3
"""
TODO List
"""
import json
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
    todos = []
    dict_data = {}
    for todo in todos_list:
        todo.pop("userId", None)
        todo.pop("id", None)
        todo["task"] = todo.pop("title")
        todo["username"] = username
        todos.append(todo)
    dict_data[id] = todos
    return dict_data


def export_to_json():
    """
    Export data as json format
    """
    filename = "{}.json".format(argv[1])
    data = main(argv[1])
    with open(filename, "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    export_to_json()
