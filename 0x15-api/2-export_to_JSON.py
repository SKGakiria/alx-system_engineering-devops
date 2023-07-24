#!/usr/bin/python3
"""Employee TODO list progress information"""
import json
import requests
import sys


if __name__ == "__main__":
    usr_id = sys.argv[1]
    b_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(b_url + "users/{}".format(usr_id)).json()
    u_name = user.get("username")
    todos = requests.get(b_url + "todos",
                         params={"userId": usr_id}).json()

    with open("{}.json".format(usr_id), "w") as jsonfile:
        json.dump({usr_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u_name
            } for t in todos]}, jsonfile)
