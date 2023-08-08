#!/usr/bin/python3
"""0-subs"""
import requests


def number_of_subscribers(subreddit):
    """Function queries and returns number of subscribers
    for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "Ubuntu.20.04:alx.advanced.api:v1.0 by /u/sk001)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
