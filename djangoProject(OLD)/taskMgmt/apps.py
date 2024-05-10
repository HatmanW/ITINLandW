# apps.py
from django.apps import AppConfig

class TaskMgmtConfig(AppConfig):
    name = 'taskMgmt'

    def ready(self):
        print("taskmgmt app is ready")
        import taskMgmt.signals