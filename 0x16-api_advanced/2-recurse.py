#!/usr/bin/python3
"""A python module that query the reddit api recursively
<<<<<<< HEAD
Return:
    a list containing titles of all hot articles
    otherwise None for invalid subreddit
=======
>>>>>>> 5278669fc56dfe4916e68cce532c57e43385a0de
"""


import requests


def recurse(subreddit, hot_list=[], i=0, after=None):

    if subreddit:
        reddit_url = "https://www.reddit.com"
        hot = 'hot'
        limit = 30
        url = "{}/r/{}/.json?sort={}&limit={}&count={}&after={}".format(
                    reddit_url, subreddit, hot, limit, i,
                    after if after else '')

        headers = {
            "User-Agent": "Subreddit articles Viewer"
        }
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            item = data["data"]["children"]
            count = len(item)
            after = data["data"]["after"]
            hot_list.extend(list(map(lambda x: x['data']['title'], item)))
            if after:
                return recurse(subreddit, hot_list, i + count, after)
            else:
                return hot_list if hot_list else None
        else:
            return None
