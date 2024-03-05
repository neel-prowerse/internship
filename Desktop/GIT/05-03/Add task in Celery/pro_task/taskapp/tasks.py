from celery import shared_task
@shared_task
def add(x,y):
    result = x + y
    return result
@shared_task
def mul(x, y):
    return x * y
