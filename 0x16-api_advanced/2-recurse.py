#!/usr/bin/python3
"""
Get top 10 hot posts from subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    prints the titles of the first 10 hot posts
    If you want to make many requests, first make sure you have oauth set up.
    Then make requests to oauth.reddit.com/r/[subreddit]/hot
    If it's on a small scale or just for testing
    use reddit.com/r/[subreddit]/hot.json
    Basically you can take any normal reddit url and either
    add a oauth at the beginning or .json at the end
    """
    URL = "https://www.reddit.com/r/{}/hot.json?".format(subreddit)
    headers = {"User-Agent": "MyAPI/1.1 by Uss"}
    resp = requests.get(URL, headers=headers, allow_redirects=False,
                        params={"after": after})
    after = resp.json().get("data").get("after")
    all = hot_list
    if resp.status_code >= 400:
        return None
    if after:
        posts = resp.json().get("data").get("children")
        for post in posts:
            all.append(post.get("data").get("title"))
        return recurse(subreddit, all, after)
    else:
        return all


if __name__ == "__main__":
    recurse("programming")
