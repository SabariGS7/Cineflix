from apscheduler.schedulers.background import BackgroundScheduler

from django.utils import timezone

from subscriptions.models import UserSubscription




def print_hello():

    print('hello world')



def scheduler_job():

    scheduler=BackgroundScheduler()

    scheduler.add_job(print_hello,'interval',minutes=1)