#!/bin/sh

pip3 install -r requirements/dev.txt
python manage.py migrate
