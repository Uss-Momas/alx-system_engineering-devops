#!/usr/bin/python3
"""Export response data to JSON format"""
import json
import requests
import sys


def export_all_to_JSON():
    """Script to export user request into JSON file
    format"""
    user_url = 'https://jsonplaceholder.typicode.com/users'
    all_user = requests.get(user_url).json()
    all_user_dict = {}
    for user in all_user:
        user_id = user.get("id")
        username = user.get("username")
        todo_url = '{}/{}/todos'.format(user_url, user_id)
        user_todos = requests.get(todo_url).json()
        u_todos = {}
        todos = []
        for todo in user_todos:
            u_todos["username"] = username
            u_todos["task"] = todo.get("title")
            u_todos["completed"] = todo.get("completed")
            todos.append(u_todos)

        all_user_dict[str(user_id)] = todos
    with open("todo_all_employees.json", mode='w') as file:
        json.dump(all_user_dict, file)


if __name__ == '__main__':
    export_all_to_JSON()
