"""
Module: celerybeat_schedule

This module defines the schedule for Celery beat tasks in the mini_blog project.

Variables:
    - CELERYBEAT_SCHEDULE: Dictionary containing the schedule for Celery beat tasks.

Classes:
    - crontab: Class representing a cron schedule, used to schedule tasks at specific times.

"""

from celery.schedules import crontab


CELERYBEAT_SCHEDULE = {
    # Internal tasks
    "clearsessions": {
        "schedule": crontab(hour=3, minute=0),
        "task": "users.tasks.clearsessions",
    },
}
