#!/usr/bin/env zsh

# shellcheck disable=SC2164
cd /home/projects/python_pro/typeidea/typeidea
# shellcheck disable=SC1090
source ~/.virtualenvs/django3.2/bin/activate
python manage.py runserver 0.0.0.0:8000
