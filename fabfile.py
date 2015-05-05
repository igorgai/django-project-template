import os

from fabric.contrib import django
from fabric.operations import local
from fabric.utils import puts

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
django.settings_module('{{ project_name }}.settings')

import django
django.setup()

from django.contrib.auth import get_user_model

ADMIN_EMAIL_ADDRESS = 'admin@example.com'


def add_admin():
    user_model = get_user_model()
    admin = user_model(email=ADMIN_EMAIL_ADDRESS)
    admin.is_superuser = True
    admin.is_staff = True
    admin.set_password('admin')
    admin.save()


# def add_foo():
#     pass


def initial_data():
    puts('==> Hi there! :)')
    puts('==> Installing the requirements...')
    local('pip install -r requirements/dev.txt ')
    puts('==> Creating the db...')
    local('python manage.py migrate')
    local('python manage.py bower install')
    puts('==> Creating the superuser...')
    add_admin()
    puts('==> Adding initial data...')
    # add_foo()
    puts('==> All done. Please do your thing and leave :)')
