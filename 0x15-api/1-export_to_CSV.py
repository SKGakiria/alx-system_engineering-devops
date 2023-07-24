#!/usr/bin/python3
"""Employee TODO list progress information"""
import requests
import sys
import csv


if __name__ == "__main__":
    usr_id = sys.argv[1]
    b_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(b_url + "users/{}".format(usr_id)).json()
    u_name = user.get("username")
    todos = requests.get(b_url + "todos",
                         params={"userId": usr_id}).json()

    with open("{}.csv".format(usr_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [usr_id, u_name, t.get("completed"), t.get("title")]
         ) for t in todos]
