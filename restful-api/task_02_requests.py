#!/use/bin/python3
""" Module that makes a request to a RESTful API """
import requests
import csv


def fetch_and_print_posts():
    """ Fetches posts from a RESTful API and prints them """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    posts = response.json()
    print("Status Code: {}".format(response.status_code))
    for post in posts:
        print(post.get("title"))


def fetch_and_save_posts():
    """ Fetches posts from a RESTful API and saves them to a file """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    posts = response.json()
    with open("posts.csv", "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for post in posts:
            writer.writerow([post.get("id"),
                             post.get("title"), post.get("body")])
