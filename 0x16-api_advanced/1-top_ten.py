#!/usr/bin/python3
""" A python modeule that queries Reddit API and prints
the titles of the first 10 hot posts from a subreddit
"""


import requests


def top_ten(subreddit):
    if subreddit:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        headers = {
            "User-Agent": "Subreddit Post Viewer"
        }
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                for post in data["data"]["children"][:10]:
                    print(post["data"]["title"])
            else:
                print(None)
        except Exception:
            pass
