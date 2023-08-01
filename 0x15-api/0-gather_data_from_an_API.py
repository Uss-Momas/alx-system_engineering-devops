#!/usr/bin/python3
"""
TODO List
"""
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
    username = user_info.get("name")
    done_tasks = 0
    titles = []
    for todo in todos_list:
        if todo.get("completed"):
            done_tasks += 1
            titles.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}):"
          .format(username, done_tasks, len(todos_list)))
    for title in titles:
        print("\t {}".format(title))


if __name__ == "__main__":
    main(argv[1])
