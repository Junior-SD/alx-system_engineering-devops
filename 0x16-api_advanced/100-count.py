#!/usr/bin/python3
"""A python module that queries the Reddit API, parses the
title of all hot articles, and prints a sorted count of
given keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not)
"""


import requests


def count_words(subreddit, word_list, hot_list=[], i=0, after=None):
    if subreddit:
        reddit_url = "https://www.reddit.com"
        hot = 'hot'
        limit = 30
        url = "{}/r/{}/.json?sort={}&limit={}&count={}&after={}".format(
            reddit_url, subreddit, hot, limit, i, after if after else '')

        headers = {
            "User-Agent": "Subreddit articles Viewer"
        }
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get("data")
            item = data.get("children")
            count = len(item)
            after = data.get("after")
            hot_list.extend(list(map(lambda x: x['data']['title'], item)))
            if after:
                return count_words(subreddit, word_list, hot_list,
                                   i + count, after)
            else:
                return printer(hot_list, word_list, word_list)
        else:
            return


def printer(hot_list, word_list, take, it=0, printed=[]):
    all_text = ' '.join(hot_list)
    all_words = all_text.lower().split()
    if it < len(take):
        word = word_list[it]
        temp = all_words.count(word)
        if temp and word not in printed:
            printed.append({word: temp})
            # word_list.pop(0)
            return printer(hot_list, word_list, take, it + 1, printed)
        else:
            return printer(hot_list, word_list, take, it + 1, printed)
    else:
        sorted_printed = sorted(printed, key=lambda
                                item: (-list(item.values())[0],
                                       list(item.keys())[0]))
        return output(sorted_printed)


def output(printed, left=0):
    i = len(printed)
    if left < i:
        word = list(printed[left].keys())[0]
        count = list(printed[left].values())[0]
        print(f"{word}: {count}")
        return output(printed, left + 1)
