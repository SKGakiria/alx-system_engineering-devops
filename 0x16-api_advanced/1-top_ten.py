#!/usr/bin/python3
"""1-top_ten"""
import requests


def top_ten(subreddit):
    """Function queries and prints the titles of the first 10 hot posts
    listed for a given subreddit"""
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
               "User-Agent": "Ubuntu.20.04:alx.advanced.api:v1.0 (by /u/sk001)"
    }
    params = {"limit": 10}
    response = requests.get(URL, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(k.get("data").get("title")) for k in results.get("children")]
