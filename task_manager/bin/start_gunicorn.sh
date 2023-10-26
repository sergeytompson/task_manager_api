#!/bin/bash
source /home/sergey/code/task_manager/venv/bin/activate
exec gunicorn -c "/home/sergey/code/task_manager/gunicorn_config.py" task_manager.wsgi
