
from celery import shared_task
from time import sleep



@shared_task
def add(x,y):
    sleep(10)
    for x in range(x,y):
        result =x+y
        x = x+1

    return result