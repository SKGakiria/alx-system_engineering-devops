#!/usr/bin/python3
"""Employee TODO list progress information"""
import requests
import sys


if __name__ == "__main__":
    usr_id = sys.argv[1]
    b_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(b_url + "users/{}".format(usr_id)).json()
    todos = requests.get(b_url + "todos",
                         params={"userId": usr_id}).json()

    done_tasks = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done_tasks), len(todos)))
    [print("\t {}".format(d)) for d in done_tasks]
