#!/usr/bin/python3
"""Export response data to JSON format"""
import json
import requests
import sys


def export_to_JSON(user_id):
    """Script to export user request into JSON file
    format"""
    user_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = '{}/{}/todos'.format(user_url, user_id)
    user_dict = {}
    user_data = requests.get('{}/{}'.format(user_url, user_id)).json()
    username = user_data.get("username")
    tasks = requests.get(todo_url).json()
    jobs_list = []
    for item in tasks:
        aux_dict = {}
        aux_dict["task"] = item.get("title")
        aux_dict["completed"] = item.get("completed")
        aux_dict["username"] = username
        jobs_list.append(aux_dict)
    user_dict[str(user_id)] = jobs_list
    filename = '{}.json'.format(user_id)
    # with open(filename, mode='w') as f:
    #    json_dump = json.dumps(user_dict)
    #    f.write(json_dump)
    with open(filename, mode='w') as f:
        json.dump(user_dict, f)


if __name__ == '__main__':
    export_to_JSON(int(sys.argv[1]))
