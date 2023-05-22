#!/usr/bin/python3
"""Gather data from an API
And Export to CSV file format
"""
import csv
import requests
import sys


def get_user_todo(user_id):
    """get the user information in json
    """
    api_url = 'https://jsonplaceholder.typicode.com'
    employee_id = user_id

    user_response = requests.get("{}/users/{}".format(api_url, employee_id))
    todos_response = requests.get("{}/todos".format(api_url))

    user_dict = user_response.json()
    todos_list = todos_response.json()

    done_tasks = 0
    tot_number_tasks = 0
    list_completed = ""

    for item in todos_list:
        if item.get('completed') and item.get('userId') == employee_id:
            list_completed += '\t ' + item.get("title") + '\n'
            done_tasks += 1
        if item.get('userId') == employee_id:
            tot_number_tasks += 1

    print("Employee {} is done with tasks ({}/{}):"
          .format(user_dict.get("name"), done_tasks, tot_number_tasks))
    print(list_completed[:-1])


def export_to_csv(user_id):
    """Export the data of user to a csv file"""
    user_api_url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(
            user_id)
    todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            user_id)
    user = requests.get(user_api_url).json()
    user_todos = requests.get(todos_url).json()
    filename = "{}.csv".format(user_id)
    with open(filename, mode='w') as user_file:
        user_name = user.get("username")
        employee_writer = csv.writer(user_file, delimiter=',', quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for item in user_todos:
            list = []
            list.append(item.get("userId"))
            list.append(user_name)
            list.append(item.get("completed"))
            list.append(item.get("title"))
            employee_writer.writerow(list)


if __name__ == '__main__':
    export_to_csv(int(sys.argv[1]))
