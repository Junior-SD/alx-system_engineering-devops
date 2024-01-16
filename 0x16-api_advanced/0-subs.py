#!/usr/bin/python3
""" A python modeule that queries Reddit API and retruns
the number of subscribers of a given subreddit
"""


import requests


def number_of_subscribers(subreddit):
    if subreddit:
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        headers = {
            "User-Agent": "Subreddit Subscriber Checker"
        }
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                subscribers = data["data"]["subscribers"]
                return subscribers
            else:
                return 0
        except Exception:
            pass
