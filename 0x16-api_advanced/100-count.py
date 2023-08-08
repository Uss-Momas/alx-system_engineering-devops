#!/usr/bin/python3
"""
Using recursion
"""
import requests


def count_words(subreddit, word_list):
    """count words in a word list"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "MyAPI/1.1 by Uss"}
    resp = requests.get(URL, headers=headers, allow_redirects=False)
    if resp.status_code != 200:
        return None
    posts = resp.json().get("data").get("children")
    titles = [post.get("data").get("title") for post in posts]
    for title in titles:
        splited_title = title.split()


if __name__ == "__main__":
    count_words("programming", "java")
