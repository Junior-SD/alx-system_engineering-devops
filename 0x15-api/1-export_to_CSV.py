#!/usr/bin/python3
"""A python script that exports the parse data to csv format
"""


import csv
import requests
from sys import argv


def employee_data_csv_converter():
    try:
        emp_id = int(argv[1])
        data = []
        url = "https://jsonplaceholder.typicode.com"
        emp_url = f'{url}/users/{emp_id}'
        todo_url = f'{url}/todos?userId={emp_id}'

        todo_data = requests.get(todo_url).json()
        emp_data = requests.get(emp_url).json()

        """count = sum(1 for todo in todo_data if todo['completed']
                    is True or todo['completed'] is False)"""
        name = emp_data.get("username")

        for items in todo_data:
            data.append({
                items['userId']: "id",
                name: "name",
                items['completed']: "bool",
                items['title']: "title"
            })

        with open(f'{emp_id}.csv', mode="w", newline="") as open_file:
            writer = csv.writer(open_file, quoting=csv.QUOTE_ALL)

            for row in data:
                writer.writerow(row)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    employee_data_csv_converter()
