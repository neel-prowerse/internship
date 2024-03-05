from django.apps import AppConfig


class TaskappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'taskapp'
    def ready(self):
        try:
            from django_task.utils import revoke_pending_tasks
            revoke_pending_tasks()
        except Exception as e:
            print(e)
            