from .models import Task
import datetime as dt


def get_tasks(user_id):
    today = dt.date.today()
    date = str(today)
    tasks_db = Task.objects.filter(date__gt=date, user=user_id)
    tasks = {}
    for task in tasks_db:
        task_date = str(task.date)
        if task_date in tasks.keys():
            tasks[task_date].append([task.id, task.title, task.description, task.is_finished])
        else:
            tasks[task_date] = [[task.id, task.title, task.description, task.is_finished]]
    return tasks