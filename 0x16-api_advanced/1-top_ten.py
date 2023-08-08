#!/usr/bin/python3
"""
Get top 10 hot posts from subreddit
"""

import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts
    If you want to make many requests, first make sure you have oauth set up.
    Then make requests to oauth.reddit.com/r/[subreddit]/hot
    If it's on a small scale or just for testing
    use reddit.com/r/[subreddit]/hot.json
    Basically you can take any normal reddit url and either
    add a oauth at the beginning or .json at the end
    """
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "MyAPI/1.1 by Uss"}
    resp = requests.get(URL, headers=headers)
    if resp.status_code == 200:
        posts = resp.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)


if __name__ == "__main__":
    top_ten("programming")
