from locust import HttpLocust, TaskSet, task
from random import randint
from book.models import Author


class AuthorTest(TaskSet):

    count_author_obj = Author.objects.count()

    @task(1)
    def get_authors(self):
        self.client.get('api/authors/')

    @task(2)
    def retrieve_author(self):
        self.client.get(f'api/authors{randint(1, self.count_author_obj)}')


class WebsiteUser(HttpLocust):
    task_set = AuthorTest
    min_wait = 50
    max_wait = 70
