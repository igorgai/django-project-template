import os

from fabric.contrib import django
from fabric.operations import local
from fabric.utils import puts

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
django.settings_module('{{ project_name }}.settings')

import django
django.setup()


# def add_foo():
#     pass


def initial_data():
    puts('==> Hi there! :)')
    puts('==> Installing the requirements...')
    local('pip install -r requirements/dev.txt ')
    puts('==> Creating the db...')
    local('python manage.py migrate')
    local('python manage.py bower install')
    puts('==> Adding initial data...')
    # add_foo()
    puts('==> All done. Please do your thing and leave :)')
