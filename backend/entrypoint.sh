#! /bin/sh
#
# entrypoint.sh
# Copyright (C) 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.
#

python parser/parser.py
python manage.py migrate
gunicorn -w 4 --bind 0.0.0.0:80 perktree.wsgi:application

