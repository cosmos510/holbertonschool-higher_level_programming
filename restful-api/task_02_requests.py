#!/user/bin/python3
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
    if response.status_code == 200:
        posts = response.json()
        post_list = []
        for post in posts:
            post_dict = {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            post_list.append(post_dict)
            with open('posts.csv', 'w', newline='') as csvfile:
                fieldnames = ['id', 'title', 'body']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(post_list)

