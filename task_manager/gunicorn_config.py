command = '/home/sergey/code/task_manager/venv/bin/gunicorn'
pythonpath = '/home/sergey/code/task_manager'
bind = '127.0.0.1:8000'
workers = 3
user = 'sergey'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=task_manager.settings'
