#!/usr/bin/python3
"""
Querying reddit API
"""
from credentials import USERNAME, PASSWORD
import requests

CLIENT_ID = "SVe5BCuAok6qOTVn23R2SA"
SECRET_KEY = "N19GAR7xI5RdVZCofw7WNR61uLIUyQ"


def number_of_subscribers(subreddit):
    """
    querying reddit to get number of subs of a subreddit
    returns:
        - number of subscribers
    """
    # Authenticate
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
    data = {
            'grant_type': 'password',
            'username': USERNAME,
            'password': PASSWORD
            }
    headers = {'User-Agent': 'A red automation script 1.1 by Uss'}

    # get token access id
    ACCESS_URL = "https://www.reddit.com/api/v1/access_token"
    res = requests.post(ACCESS_URL, data=data, headers=headers, auth=auth)
    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization': f'bearer {TOKEN}'}}

    URL_API = "https://oauth.reddit.com/r/{}/about".format(subreddit)
    resp = requests.get(URL_API, headers=headers)
    if resp.status_code == 200:
        subs_count = resp.json()['data']['subscribers']
        return subs_count
    return 0


if __name__ == "__main__":
    number_of_subscribers("programming")
