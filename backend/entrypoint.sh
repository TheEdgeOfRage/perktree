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
if not User.objects.filter(base_user__username='${DJANGO_ADMIN_USER}').count() :
	base_admin = AuthUser.objects.get(username='${DJANGO_ADMIN_USER}')
	admin = User(base_user=base_admin)
	admin.save()

if not AuthUser.objects.filter(username='user').count() :
	base_user = AuthUser('user', 'user@example.com', 'user')
	base_user.save()
if not User.objects.filter(base_user__username='user').count() :
	base_user = AuthUser.objects.get(username='user')
	user = User(base_user=base_user)
	user.save()
" | python manage.py shell

gunicorn -w 4 --bind 0.0.0.0:80 perktree.wsgi:application

