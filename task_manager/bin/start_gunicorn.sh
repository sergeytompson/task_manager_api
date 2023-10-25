#!/bin/bash
source /home/www/code/project1/env/bin/activate
exec gunicorn -c "/home/sergey/code/task_manager/gunicorn_config.py" task_manager.wsgi
