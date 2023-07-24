#!/usr/bin/python3
"""Employee TODO list progress information"""
import json
import requests
import sys


if __name__ == "__main__":
    b_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(b_url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            usr.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": usr.get("username")
            } for t in requests.get(b_url + "todos",
                                    params={"userId": usr.get("id")}).json()]
            for usr in users}, jsonfile)
