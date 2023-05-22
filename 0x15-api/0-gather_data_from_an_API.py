#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys

api_url = 'https://jsonplaceholder.typicode.com'
employee_id = int(sys.argv[1])

user_response = requests.get("{}/users/{}".format(api_url, employee_id))
todos_response = requests.get("{}/todos".format(api_url))
user_dict = user_response.json()
todos_list = todos_response.json()
done_tasks = 0
tot_number_tasks = 0
list_completed = ""
for item in todos_list:
    if item['completed'] and item['userId'] == employee_id:
        list_completed += '\t ' + item["title"] + '\n'
        done_tasks += 1
    if item['userId'] == employee_id:
        tot_number_tasks += 1

print("Employee {} is done with tasks ({}/{}):"
      .format(user_dict["name"], done_tasks, tot_number_tasks))
print(list_completed[:-1])
