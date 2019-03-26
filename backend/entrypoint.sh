#! /bin/sh
#
# entrypoint.sh
# Copyright (C) 2019 pavle <pavle.portic@tilda.center>
#
# Distributed under terms of the BSD-3-Clause license.
#

sleep 5
python manage.py migrate

echo "
from django.contrib.auth.models import User as AuthUser;
from perks.models import User;
if not AuthUser.objects.filter(username='${DJANGO_ADMIN_USER}').count() :
	AuthUser.objects.create_superuser('${DJANGO_ADMIN_USER}', '${DJANGO_ADMIN_MAIL}', '${DJANGO_ADMIN_PASS}')
" | python manage.py shell

gunicorn -w 4 --bind 0.0.0.0:80 perktree.wsgi:application

